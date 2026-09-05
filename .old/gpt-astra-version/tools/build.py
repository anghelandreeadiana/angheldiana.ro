# -*- coding: utf-8 -*-
"""Regenerează paginile HTML din textele aprobate aflate în `content/`.

Site-ul funcționează fără acest script: paginile HTML sunt fișiere obișnuite, care
pot fi editate direct. Scriptul este util atunci când se modifică textele din
`content/` și trebuie reconstruite toate paginile deodată.

    python3 tools/build.py

Paginile juridice sunt recitite din fișierele HTML existente și doar reîmbrăcate în
antetul și subsolul site-ului, deci textul lor se editează direct în HTML.
"""

import html
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
SRC = os.path.join(OUT, "content")
GPT = OUT  # paginile juridice se recitesc din propriile fișiere

NAME = "Dr. Anghel Andreea-Diana"
ROLE = "Medic specialist dermatovenerologie"

NAV = [
    ("despre-mine.html", "Despre mine"),
    ("servicii.html", "Servicii"),
    ("unde-ma-gasiti.html", "Locații"),
    ("intrebari-frecvente.html", "Întrebări frecvente"),
]

# ---------------------------------------------------------------- markdown ---

def read_md(name):
    with open(os.path.join(SRC, name), encoding="utf-8") as fh:
        return fh.read()


def inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    return text


def blocks(chunk):
    """Transformă un fragment de markdown în paragrafe și liste HTML."""
    out = []
    for raw in re.split(r"\n\s*\n", chunk.strip()):
        raw = raw.strip()
        if not raw or raw.startswith("<!--") or raw.startswith("**Statut:**"):
            continue
        if raw.startswith("- "):
            items = "".join(
                "<li>%s</li>" % inline(line[2:].strip())
                for line in raw.splitlines()
                if line.strip().startswith("- ")
            )
            out.append("<ul>%s</ul>" % items)
        else:
            out.append("<p>%s</p>" % inline(" ".join(raw.split())))
    return out


def sections(name):
    """Împarte un fișier markdown în secțiuni de nivel ##."""
    text = re.sub(r"<!--.*?-->", "", read_md(name), flags=re.S)
    parts = re.split(r"^## ", text, flags=re.M)[1:]
    result = []
    for part in parts:
        head, _, body = part.partition("\n")
        result.append((head.strip(), blocks(body)))
    return result


def body_only(name):
    text = re.sub(r"<!--.*?-->", "", read_md(name), flags=re.S)
    text = re.sub(r"^# .*\n", "", text, count=1)
    return blocks(text)


def slug(text):
    table = {"ă": "a", "â": "a", "î": "i", "ș": "s", "ş": "s", "ț": "t", "ţ": "t"}
    text = "".join(table.get(ch, ch) for ch in text.lower())
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")[:96].rstrip("-")


# ------------------------------------------------------------------ chrome ---

def head(title, description, page, extra=""):
    canonical = "https://angheldiana.ro/" if page == "index.html" else "https://angheldiana.ro/%s" % page
    return """<!doctype html>
<html lang="ro">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<meta name="author" content="%s">
<meta property="og:type" content="website">
<meta property="og:locale" content="ro_RO">
<meta property="og:site_name" content="%s">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:url" content="%s">
<meta property="og:image" content="https://angheldiana.ro/assets/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Dr. Anghel Andreea-Diana — medic specialist dermatovenerologie">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://angheldiana.ro/assets/og.png">
<meta name="theme-color" content="#204e52">
<link rel="canonical" href="%s">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="assets/fonts/space-grotesk-variable.ttf" as="font" type="font/ttf" crossorigin>
<link rel="stylesheet" href="styles.css">
%s</head>
<body>
<a class="skip-link" href="#continut">Sari direct la conținut</a>

<header class="masthead">
  <div class="wrap">
    <a class="wordmark" href="index.html" aria-label="Dr. Anghel Andreea-Diana — pagina principală">
      <span class="brand-mark" aria-hidden="true">a<span>d</span></span>
      <span class="name">%s</span>
      <span class="role">%s</span>
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav">
      <span class="bars" aria-hidden="true"><i></i><i></i></span>
      <span class="label">Meniu</span>
      <span class="sr-only">de navigare</span>
    </button>
    <nav class="nav" id="nav" data-open="false" aria-label="Navigare principală">
%s
      <a class="btn btn--sm" href="unde-ma-gasiti.html#programari">Programări</a>
    </nav>
  </div>
</header>

<main id="continut">
""" % (
        html.escape(title), html.escape(description), NAME, NAME,
        html.escape(title), html.escape(description), canonical, canonical, extra,
        NAME, ROLE, nav_links(page),
    )


def nav_links(page):
    rows = []
    for href, label in NAV:
        current = ' aria-current="page"' if href == page else ""
        rows.append('      <a href="%s"%s>%s</a>' % (href, current, label))
    return "\n".join(rows)


FOOT = """</main>

<footer class="site-foot">
  <div class="wrap">
    <div class="top">
      <div class="who">
        <span class="name">%s</span>
        <p>%s</p>
      </div>
      <nav aria-label="Pagini utile și informații juridice">
        <a href="viziunea-mea.html">Viziunea mea</a>
        <a href="articole.html">Articole</a>
        <a href="unde-ma-gasiti.html">Locații și programări</a>
        <a href="politica-de-confidentialitate.html">Confidențialitate</a>
        <a href="politica-de-cookie-uri.html">Cookie-uri</a>
        <a href="informatii-legale.html">Informații legale</a>
      </nav>
    </div>
    <p class="footer-signature" aria-hidden="true">anghel diana.</p>
    <div class="notes">
      <p>Informațiile de pe acest site au caracter educativ și nu înlocuiesc consultația, diagnosticul sau tratamentul medical personalizat.</p>
      <p><strong>În situații care pun în pericol viața sau sănătatea, apelați 112.</strong></p>
    </div>
  </div>
</footer>

<script src="script.js"></script>
</body>
</html>
""" % (NAME, ROLE)


def write(filename, body):
    with open(os.path.join(OUT, filename), "w", encoding="utf-8") as fh:
        fh.write(body)
    print("scris  %s" % filename)


def page_head(title, lead=None, updated=None):
    parts = ['<section class="page-head">', '  <div class="wrap">',
             '    <p class="page-kicker">Dr. Anghel · Dermatovenerologie</p>',
             "    <h1>%s</h1>" % title]
    if lead:
        parts.append('    <p class="lead">%s</p>' % lead)
    if updated:
        parts.append('    <p class="updated">%s</p>' % updated)
    parts += ["  </div>", "</section>"]
    return "\n".join(parts) + "\n"


# ------------------------------------------------------------------- date ----

CITIES = [
    ("București", [
        {
            "name": "Ana Medical Care",
            "address": "Str. Brebu nr. 5, Sector 2, București",
            "phones": [("0752 443 626", "+40752443626")],
            "cas": True,
            "link": ("https://anamedicalcare.ro", "Site-ul clinicii"),
        },
        {
            "name": "Renew Institute",
            "address": "Str. Intrarea Căpriorilor nr. 1, Sector 1, București",
            "phones": [("0371 71 31 31", "+40371713131"), ("021 9035", "+40219035")],
            "cas": True,
            "link": ("https://renewinstitute.ro/dr-anghel-diana/", "Profil profesional"),
        },
    ]),
    ("Ploiești", [
        {
            "name": "Roua Medical Center",
            "address": "Str. Principală nr. 12, Păuleștii Noi, Prahova",
            "phones": [("0799 948 200", "+40799948200")],
            "cas": False,
            "link": ("https://clinicaroua.ro/", "Site-ul clinicii"),
        },
    ]),
    ("Buzău", [
        {
            "name": "Angi San",
            "address": "Str. Patriei nr. 88, Buzău",
            "phones": [("0744 344 588", "+40744344588")],
            "cas": False,
            "link": ("https://angisan.ro/", "Site-ul clinicii"),
        },
        {
            "name": "Laurus Medical Buzău – Medicover",
            "address": "Bd. Stadionului nr. 7A, parter, Buzău",
            "phones": [("0371 478 888", "+40371478888")],
            "cas": False,
            "link": ("https://www.medicover.ro/medici/andreea-diana-anghel%2C4585%2Cd%2C256",
                     "Profil profesional"),
        },
    ]),
]

PERSON_LD = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Dr. Anghel Andreea-Diana",
  "jobTitle": "Medic specialist dermatovenerologie",
  "url": "https://angheldiana.ro/",
  "image": "https://angheldiana.ro/assets/dr-anghel-andreea-diana.jpg",
  "alumniOf": "Universitatea de Medicină și Farmacie „Carol Davila” din București",
  "memberOf": [
    "Academia Europeană de Dermatologie și Venerologie",
    "Societatea Română de Dermatologie",
    "Société Française de Dermatologie"
  ],
  "areaServed": ["București", "Ploiești", "Buzău"]
}
</script>
"""

CTA = """<section class="band band--plum band--tight">
  <div class="wrap">
    <p class="kicker">Programări</p>
    <h2>%s</h2>
    <p class="measure">%s</p>
    <div class="btn-row">
      <a class="btn btn--light" href="unde-ma-gasiti.html#programari">Vedeți clinicile și telefoanele</a>
    </div>
  </div>
</section>
"""


def cta(title, text):
    return CTA % (title, text)


# ------------------------------------------------------------- pagina 1: acasă

def build_index():
    services = sections("servicii-si-consultatii.md")
    items = "\n".join(
        '<li><a href="servicii.html#%s"><span class="service-index" aria-hidden="true">%02d</span><h3>%s</h3><span class="card-arrow" aria-hidden="true">↗</span></a></li>'
        % (slug(title), index, title)
        for index, (title, _) in enumerate(services, 1)
    )
    cities = "\n".join(
        '<a class="city-card" href="unde-ma-gasiti.html#%s"><span class="city-number" aria-hidden="true">0%s</span><span class="city-arrow" aria-hidden="true">↗</span><h3>%s</h3><p>%s</p></a>'
        % (slug(city), index, "Ploiești / Păuleștii Noi" if city == "Ploiești" else city, " · ".join(c["name"] for c in clinics))
        for index, (city, clinics) in enumerate(CITIES, 1)
    )
    faq = "\n".join(
        '<details><summary><span>%s</span><span class="chev" aria-hidden="true"></span></summary><div class="answer">%s</div></details>'
        % (question, "\n".join(paragraphs))
        for question, paragraphs in sections("intrebari-frecvente.md")[:4]
    )
    with open(os.path.join(HERE, "templates", "home.html"), encoding="utf-8") as fh:
        template = fh.read()
    body = head(
        "%s | %s în București, Ploiești și Buzău" % (NAME, ROLE),
        "Dr. Anghel Andreea-Diana, medic specialist dermatovenerologie. "
        "Consultații dermatologice, dermatoscopie, oncodermatologie și proceduri "
        "dermatologice în București, Ploiești și Buzău.",
        "index.html", PERSON_LD,
    )
    body += template.replace("{services}", items).replace("{cities}", cities).replace("{faq}", faq)
    body += cta(
        "Programările se fac direct la clinică.",
        "Alegeți clinica potrivită pentru dumneavoastră și contactați recepția pentru disponibilitate și programare.",
    )
    write("index.html", body + FOOT)


# ------------------------------------------------------- pagini de text lung ---

def build_prose(filename, page_title, h1, lead, md, meta, closing):
    body = head(page_title, meta, filename)
    body += page_head(h1, lead)
    body += '<div class="wrap">\n  <article class="prose">\n%s\n  </article>\n</div>\n\n' % "\n".join(
        "    " + block for block in body_only(md)
    )
    body += closing
    body += FOOT
    write(filename, body)


# ------------------------------------------------------------ pagina servicii ---

def build_services():
    body = head(
        "Servicii și consultații | %s" % NAME,
        "Consultație dermatologică pentru adulți și copii, dermatoscopie, afecțiuni ale "
        "părului și unghiilor, infecții cu transmitere sexuală, oncodermatologie, "
        "chirurgie dermatologică și dermatologie regenerativă.",
        "servicii.html",
    )
    body += page_head(
        "Servicii și consultații",
        "Indicația pentru orice investigație sau procedură se stabilește în urma "
        "consultației și a evaluării medicale individuale.",
    )
    rows = []
    for index, (title, paragraphs) in enumerate(sections("servicii-si-consultatii.md"), 1):
        rows.append(
            '  <section class="service" id="%s">\n    <span class="service-number" aria-hidden="true">%02d</span>\n    <h2>%s</h2>\n    <div>\n%s\n    </div>\n  </section>'
            % (slug(title), index, title, "\n".join("      " + p for p in paragraphs))
        )
    body += '<div class="services wrap">\n%s\n</div>\n\n' % "\n".join(rows)
    body += cta(
        "Nu știți ce fel de consultație vă este necesară?",
        "Consultația dermatologică este punctul de plecare: în cadrul ei stabilim "
        "împreună ce evaluări sau proceduri sunt potrivite.",
    )
    body += FOOT
    write("servicii.html", body)


# ---------------------------------------------------------------- pagina FAQ ---

def build_faq():
    entries = sections("intrebari-frecvente.md")
    normal = entries[:-1]
    question, answer = entries[-1]

    body = head(
        "Întrebări frecvente | %s" % NAME,
        "Durata consultației, pregătirea pentru consultație, dermatoscopia, "
        "confidențialitatea consultațiilor de venerologie și situațiile care necesită "
        "evaluare urgentă.",
        "intrebari-frecvente.html",
    )
    body += page_head(
        "Întrebări frecvente",
        "Informațiile de mai jos au caracter general. Ele nu înlocuiesc consultația "
        "și evaluarea individuală.",
    )

    rows = []
    for q, paragraphs in normal:
        rows.append(
            """  <details id="%s">
    <summary><span>%s</span><span class="chev" aria-hidden="true"></span></summary>
    <div class="answer">
%s
    </div>
  </details>""" % (slug(q), q, "\n".join("      " + p for p in paragraphs))
        )

    urgent = []
    for index, paragraph in enumerate(answer):
        if index == len(answer) - 1:
            urgent.append('    <p class="fineprint">%s</p>' % paragraph[3:-4])
        else:
            urgent.append("    " + paragraph)

    body += """<div class="wrap">
<div class="faq">
%s
  <section class="urgent" id="%s">
    <h2>%s</h2>
%s
  </section>
</div>
</div>

""" % ("\n".join(rows), slug(question), question, "\n".join(urgent))

    body += cta(
        "Aveți o întrebare la care nu ați găsit răspuns?",
        "Recepția clinicii vă poate oferi detalii despre programare, iar restul "
        "întrebărilor le putem discuta în cadrul consultației.",
    )
    body += FOOT
    write("intrebari-frecvente.html", body)


# ----------------------------------------------------------- pagina locațiilor ---

def build_locations():
    body = head(
        "Unde mă găsiți | %s" % NAME,
        "Clinicile în care consult și numerele de telefon pentru programări, "
        "în București, Ploiești și Buzău.",
        "unde-ma-gasiti.html",
    )
    body += page_head(
        "Unde mă găsiți",
        "Consult în București, Ploiești și Buzău. Programările și disponibilitatea "
        "consultațiilor se confirmă direct la recepția clinicii alese.",
    )

    body += """<nav class="city-jump wrap" aria-label="Salt rapid la oraș">
  <a href="#bucuresti">București</a>
  <a href="#ploiesti">Ploiești / Păuleștii Noi</a>
  <a href="#buzau">Buzău</a>
</nav>
"""

    city_blocks = []
    for city, clinics in CITIES:
        cards = []
        for clinic in clinics:
            phones = clinic["phones"]
            actions = ['<a class="btn" href="tel:%s">%s</a>' % (phones[0][1], phones[0][0])]
            for label, number in phones[1:]:
                actions.append('<a class="alt" href="tel:%s">sau %s</a>' % (number, label))
            href, label = clinic["link"]
            actions.append(
                '<a class="alt" href="%s" target="_blank" rel="noopener noreferrer">%s</a>'
                % (href, label)
            )
            cas = '\n      <p><span class="cas">Consultații disponibile și prin CAS</span></p>' if clinic["cas"] else ""
            cards.append(
                """    <article class="clinic plate">
      <h3>%s</h3>
      <address>%s</address>%s
      <div class="actions">%s</div>
    </article>""" % (clinic["name"], clinic["address"], cas, "".join("\n        " + a for a in actions) + "\n      ")
            )
        city_blocks.append(
            '  <section class="city" id="%s">\n    <h2>%s</h2>\n    <div class="clinics">\n%s\n    </div>\n  </section>'
            % (slug(city), city, "\n".join(cards))
        )

    body += '<div class="cities wrap" id="programari">\n%s\n</div>\n\n' % "\n".join(city_blocks)

    body += """<section class="band band--stone band--tight">
  <div class="wrap">
    <div class="measure">
      <h2>Înainte de a suna</h2>
      <p>Clinicile sunt entități independente și își administrează propriile programe, tarife și proceduri de programare. Programul meu nu este publicat pe acest site: recepția clinicii vă poate spune care sunt intervalele disponibile.</p>
      <p>Nu ofer consultații online și nu stabilesc diagnostice pe baza fotografiilor sau a mesajelor. Vă rugăm să nu transmiteți informații medicale sau imagini prin canale nesecurizate.</p>
    </div>
  </div>
</section>

<section class="band band--tight">
  <div class="wrap">
    <div class="measure">
      <h2>În caz de urgență</h2>
      <p>Dacă simptomele sunt severe, apar brusc sau se agravează rapid, solicitați fără întârziere o evaluare medicală într-un serviciu de urgență. Dacă situația poate pune în pericol viața, integritatea sau sănătatea și este necesară intervenția imediată, apelați 112.</p>
      <p><a href="intrebari-frecvente.html#%s">Semnele care pot indica o urgență dermatologică</a></p>
    </div>
  </div>
</section>

""" % slug("Ce trebuie să fac într-o posibilă urgență dermatologică?")

    body += FOOT
    write("unde-ma-gasiti.html", body)


# ------------------------------------------------------------ pagina articole ---

def build_articles():
    body = head(
        "Articole | %s" % NAME,
        "Materiale de educație medicală despre sănătatea pielii, a părului și a "
        "unghiilor, în pregătire.",
        "articole.html",
    )
    body += page_head(
        "Articole",
        "Materiale de educație medicală despre sănătatea pielii, a părului și a "
        "unghiilor, scrise pentru pacienți.",
    )
    body += """<div class="wrap">
<div class="soon">
  <div class="plate">
    <h2>În pregătire</h2>
    <p>Articolele vor explica, pe înțelesul tuturor, subiecte frecvente din dermatologie și venerologie: ce înseamnă un diagnostic, ce presupune o investigație și când este momentul unei consultații.</p>
    <p>Fiecare material va fi documentat pe baza unor surse medicale credibile, va menționa data publicării și va fi verificat înainte de a apărea pe site.</p>
    <p>Informațiile publicate vor avea caracter general și nu vor înlocui consultația, diagnosticul sau tratamentul medical personalizat.</p>
  </div>
</div>
</div>

"""
    body += cta(
        "Pentru o evaluare individuală este necesară consultația.",
        "Un articol poate explica un context general, dar nu poate ține locul examinării clinice.",
    )
    body += FOOT
    write("articole.html", body)


# ------------------------------------------------------------ pagini juridice ---

def legal_body(source):
    with open(os.path.join(GPT, source), encoding="utf-8") as fh:
        raw = fh.read()
    inner = re.search(r'<article class="legal(?:-content)?">(.*?)</article>', raw, re.S).group(1)
    inner = inner.replace('<aside class="legal-draft">', '<aside class="draft">')
    inner = inner.replace(' class="text-link"', "")
    inner = inner.replace(' <span aria-hidden="true">↗</span>', "")
    return inner.strip()


def build_legal(filename, title, meta, updated, source):
    body = head("%s | %s" % (title, NAME), meta, filename)
    body += page_head(title, None, updated)
    body += '<div class="wrap">\n<article class="legal">\n%s\n</article>\n</div>\n\n' % legal_body(source)
    body += FOOT
    write(filename, body)


# ------------------------------------------------------------------- execuție ---

build_index()

build_prose(
    "despre-mine.html",
    "Despre mine | %s" % NAME,
    "Despre mine",
    None,
    "despre-mine.md",
    "Parcursul profesional al Dr. Anghel Andreea-Diana: formare în dermatovenerologie "
    "în România, stagii în Germania și Franța, dermato-oncologie, apartenență la "
    "societăți medicale de specialitate.",
    """<section class="band band--stone band--tight">
  <div class="wrap">
    <div class="measure">
      <h2>Ce urmează</h2>
      <p><a href="viziunea-mea.html">Viziunea mea despre relația medic–pacient</a> explică felul în care se desfășoară o consultație și ce puteți aștepta de la ea.</p>
    </div>
  </div>
</section>

""",
)

build_prose(
    "viziunea-mea.html",
    "Viziunea mea | %s" % NAME,
    "Viziunea mea",
    None,
    "viziunea-mea.md",
    "Viziunea Dr. Anghel Andreea-Diana asupra relației medic–pacient: ascultare activă, "
    "explicarea diagnosticului, obiective realiste și decizii luate împreună.",
    """<section class="band band--stone band--tight">
  <div class="wrap">
    <div class="measure">
      <h2>Ce urmează</h2>
      <p>Vedeți <a href="servicii.html">consultațiile și serviciile</a> sau <a href="unde-ma-gasiti.html#programari">clinicile în care consult</a>.</p>
    </div>
  </div>
</section>

""",
)

build_services()
build_faq()
build_locations()
build_articles()

build_legal(
    "politica-de-confidentialitate.html",
    "Politica de confidențialitate",
    "Informații privind protecția datelor personale pe website-ul Dr. Anghel Andreea-Diana.",
    "Ultima actualizare a variantei de lucru: 1 septembrie 2026",
    "politica-de-confidentialitate.html",
)
build_legal(
    "politica-de-cookie-uri.html",
    "Politica de cookie-uri",
    "Informații despre utilizarea cookie-urilor pe website-ul Dr. Anghel Andreea-Diana.",
    "Ultima actualizare a variantei de lucru: 1 septembrie 2026",
    "politica-de-cookie-uri.html",
)
build_legal(
    "informatii-legale.html",
    "Informații legale",
    "Informații legale și condiții de utilizare pentru website-ul Dr. Anghel Andreea-Diana.",
    "Ultima actualizare a variantei de lucru: 1 septembrie 2026",
    "informatii-legale.html",
)

print("\ngata.")
