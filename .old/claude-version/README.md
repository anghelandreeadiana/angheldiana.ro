# angheldiana.ro — varianta Claude

Website static de prezentare pentru **Dr. Anghel Andreea-Diana**, medic specialist
dermatovenerologie. HTML, CSS și un singur fișier JavaScript. Fără framework, fără
compilare, fără bază de date.

## Cum îl deschideți local

**Varianta simplă.** Deschideți `index.html` direct în browser.

**Varianta recomandată (navigare completă).** În VS Code, instalați extensia
*Live Server*, deschideți `index.html` și apăsați **Go Live**.
Alternativ, din terminal, în acest folder:

```
python3 -m http.server 8000
```

apoi deschideți `http://127.0.0.1:8000`.

## Paginile

| Fișier | Pagina |
| --- | --- |
| `index.html` | Acasă |
| `despre-mine.html` | Despre mine |
| `viziunea-mea.html` | Viziunea mea |
| `servicii.html` | Servicii și consultații |
| `unde-ma-gasiti.html` | Unde mă găsiți și programări |
| `intrebari-frecvente.html` | Întrebări frecvente |
| `articole.html` | Articole (secțiune în pregătire) |
| `politica-de-confidentialitate.html` | Politica de confidențialitate |
| `politica-de-cookie-uri.html` | Politica de cookie-uri |
| `informatii-legale.html` | Informații legale |

Restul fișierelor: `styles.css` (identitatea vizuală), `script.js` (meniul pentru
telefon), `assets/` (fotografiile), `content/` (textele aprobate, în format Markdown).

## Confidențialitate: ce face și ce nu face site-ul

- Nu încarcă niciun fișier de pe alt server: fără fonturi Google, fără hărți
  încorporate, fără biblioteci externe, fără instrumente de analiză.
- Nu setează cookie-uri și nu folosește `localStorage`.
- Nu conține formulare, conturi, newsletter sau programare online.
- Programările se fac telefonic, direct la clinici.

Aceste alegeri sunt cele care fac ca politica de cookie-uri să poată spune, corect,
că site-ul nu are nevoie de un banner de consimțământ. Dacă se adaugă ulterior o hartă,
un videoclip încorporat, un font extern sau un instrument de analiză, politicile
trebuie actualizate.

## Accesibilitate

- Un singur `h1` pe pagină și o ierarhie corectă a titlurilor.
- Link „Sari direct la conținut”, contur vizibil la navigarea cu tastatura.
- Meniul de pe telefon funcționează cu tastatura și se închide cu `Esc`.
- Contrastul textului respectă nivelul AA.
- `prefers-reduced-motion` este respectat. Site-ul nu are animații decorative.

## Înainte de publicare

1. Completați marcajele `[de completat]` din cele trei pagini juridice: identitatea
   operatorului, adresa profesională, adresa de e-mail administrativă, furnizorul de
   găzduire și durata păstrării jurnalelor tehnice.
2. Cereți validarea juridică a celor trei pagini.
3. Reverificați telefonic adresele, numerele și linkurile clinicilor.
4. Citiți `NOTE-DE-APROBAT.md` și confirmați textele scrise pentru site.
5. Configurați HTTPS, domeniul, copiile de siguranță și înregistrările DNS.
6. După instalarea pe server, verificați din nou dacă platforma de găzduire
   introduce cookie-uri sau servicii externe.

## Statut

Proiect local. Site-ul nu a fost publicat și nicio configurare DNS nu a fost modificată.
