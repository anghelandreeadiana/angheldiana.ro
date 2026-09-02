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
    ("viziunea-mea.html", "Viziunea mea"),
    ("servicii.html", "Servicii"),
    ("unde-ma-gasiti.html", "Locații"),
    ("intrebari-frecvente.html", "Întrebări frecvente"),
    ("articole.html", "Articole"),
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
    return text.strip("-")[:60]


# ------------------------------------------------------------------ chrome ---

def head(title, description, page, extra=""):
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
<link rel="stylesheet" href="styles.css">
%s</head>
<body>
<a class="skip-link" href="#continut">Sari direct la conținut</a>

<header class="masthead">
  <div class="wrap">
    <a class="wordmark" href="index.html">
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
        html.escape(title), html.escape(description), extra,
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
      <nav aria-label="Pagini juridice">
        <a href="unde-ma-gasiti.html">Locații și programări</a>
        <a href="politica-de-confidentialitate.html">Confidențialitate</a>
        <a href="politica-de-cookie-uri.html">Cookie-uri</a>
        <a href="informatii-legale.html">Informații legale</a>
      </nav>
    </div>
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
  "image": "https://angheldiana.ro/assets/dr-anghel-andreea-diana-edited.png",
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
    vision = "Un diagnostic nu ar trebui doar comunicat, ci și explicat."

    items = "\n".join(
        '    <li><a href="servicii.html#%s">%s</a></li>' % (slug(title), title)
        for title, _ in services
    )

    cities = "\n".join(
        """      <div>
        <h3>%s</h3>
        <p>%s</p>
      </div>""" % (city, " · ".join(c["name"] for c in clinics))
        for city, clinics in CITIES
    )

    faq = sections("intrebari-frecvente.md")
    faq_links = "\n".join(
        '    <li><a href="intrebari-frecvente.html#%s">%s</a></li>' % (slug(q), q)
        for q, _ in faq[:4]
    )

    body = head(
        "%s | %s în București, Ploiești și Buzău" % (NAME, ROLE),
        "Dr. Anghel Andreea-Diana, medic specialist dermatovenerologie. "
        "Consultații dermatologice, dermatoscopie, oncodermatologie și proceduri "
        "dermatologice în București, Ploiești și Buzău.",
        "index.html",
        PERSON_LD,
    )

    body += """<section class="opening">
  <div class="wrap">
    <div>
      <h1>%s</h1>
      <p class="role">%s</p>
      <p class="lead">Sunt medic specialist dermatovenerologie, cu formare în România, Germania și Franța.</p>
      <p class="lead">Consult în București, Ploiești și Buzău. Consultațiile se desfășoară în cabinet, pe baza unei programări.</p>
      <div class="btn-row">
        <a class="btn" href="unde-ma-gasiti.html#programari">Unde mă găsiți</a>
        <a href="despre-mine.html">Parcursul meu profesional</a>
      </div>
    </div>
    <figure class="portrait">
      <img src="assets/dr-anghel-andreea-diana-edited.png" width="1024" height="1536"
           alt="Portret: Dr. Anghel Andreea-Diana, medic specialist dermatovenerologie">
    </figure>
  </div>
</section>

<section class="band band--stone">
  <div class="wrap">
    <div class="band-head">
      <h2>Consultații și servicii</h2>
      <p>Fiecare recomandare pornește de la consultație și de la evaluarea situației individuale.</p>
    </div>
    <ul class="index-list">
%s
    </ul>
  </div>
</section>

<section class="band band--blush">
  <div class="wrap">
    <figure class="pull">
      <blockquote>„%s”</blockquote>
      <figcaption><a href="viziunea-mea.html">Viziunea mea despre relația medic–pacient</a></figcaption>
    </figure>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="band-head">
      <h2>Unde mă găsiți</h2>
      <p>Disponibilitatea consultațiilor și programările se confirmă direct la recepția clinicii.</p>
    </div>
    <div class="city-row">
%s
    </div>
    <div class="btn-row">
      <a class="btn btn--ghost" href="unde-ma-gasiti.html">Adrese și numere de telefon</a>
    </div>
  </div>
</section>

<section class="band band--stone">
  <div class="wrap">
    <div class="band-head">
      <h2>Întrebări frecvente</h2>
      <p>Răspunsuri la întrebările pe care pacienții le adresează cel mai des înaintea unei consultații.</p>
    </div>
    <ul class="index-list">
%s
    </ul>
    <div class="btn-row">
      <a class="btn btn--ghost" href="intrebari-frecvente.html">Toate întrebările</a>
    </div>
  </div>
</section>

<section class="band band--tight">
  <div class="wrap">
    <div class="two-up">
      <h2>Articole</h2>
      <div>
        <p>Pregătesc materiale de educație medicală despre sănătatea pielii, a părului și a unghiilor. Fiecare material este documentat și verificat înainte de publicare.</p>
        <p><a href="articole.html">Despre secțiunea de articole</a></p>
      </div>
    </div>
  </div>
</section>

""" % (NAME, ROLE, items, vision, cities, faq_links)

    body += cta(
        "Programările se fac direct la clinică.",
        "Alegeți clinica potrivită pentru dumneavoastră și contactați recepția pentru "
        "disponibilitate și programare.",
    )
    body += FOOT
    write("index.html", body)


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
    for title, paragraphs in sections("servicii-si-consultatii.md"):
        rows.append(
            '  <section class="service" id="%s">\n    <h2>%s</h2>\n    <div>\n%s\n    </div>\n  </section>'
            % (slug(title), title, "\n".join("      " + p for p in paragraphs))
        )
    body += '<div class="services wrap">\n%s\n</div>\n\n' % "\n".join(rows)
    body += cta(
        "Nu sunteți sigur ce fel de consultație vă este necesară?",
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
