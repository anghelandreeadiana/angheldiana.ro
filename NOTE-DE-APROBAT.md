> Migration note: these editorial decisions are carried forward from `.old/codex-version`. References to `.html` pages now correspond to the extensionless routes in `src/routes`. Approved Markdown remains in `.old/codex-version/content`; active public copy is in the Svelte pages.

# Texte care au nevoie de aprobarea dumneavoastră

## Elemente de prezentare adăugate în varianta Codex

Pentru noua ierarhie vizuală au fost adăugate câteva formulări scurte, alcătuite
exclusiv din informații care apar deja în textele de lucru. Vă rugăm să confirmați
și aceste formulări înainte de publicare:

- „Dermatologie · București · Ploiești / Păuleștii Noi · Buzău”;
- „Medic specialist · Dermatovenerologie”;
- „Formare internațională · România · Germania · Franța”;
- „Consultații în cabinet · București · zona Ploiești · Buzău”.

Imaginea de distribuire pe rețele sociale conține numai numele profesional și
titlul „Medic specialist dermatovenerologie”. Portretul folosit în această imagine
este o prelucrare grafică realizată pornind de la fotografia furnizată și trebuie,
de asemenea, aprobat înainte de publicare.

Textele din `content/*.md` sunt preluate **cuvânt cu cuvânt** pe site și nu au fost
modificate. Verificarea automată confirmă că fiecare propoziție aprobată apare identic
în paginile HTML.

Lista de mai jos cuprinde **numai textele scrise pentru site** — titluri de secțiune,
propoziții de legătură, butoane și descrieri pentru motoarele de căutare. Vă rog să le
confirmați, să le corectați sau să le eliminați înainte de publicare.

---

## Acasă (`index.html`)

- „Consult în București, Ploiești și Buzău.” — propoziție nouă; a doua parte a
  paragrafului („Consultațiile se desfășoară în cabinet, pe baza unei programări.”)
  este preluată din răspunsul aprobat despre consultațiile online.
- Titluri de secțiune: „Consultații și servicii”, „Unde mă găsiți”,
  „Întrebări frecvente”, „Articole”.
- „Fiecare recomandare pornește de la consultație și de la evaluarea situației
  individuale.”
- „Disponibilitatea consultațiilor și programările se confirmă direct la recepția
  clinicii.” — adaptare a notei editoriale din `content/locatii-si-programari.md`.
- „Răspunsuri la întrebările pe care pacienții le adresează cel mai des înaintea unei
  consultații.”
- „Pregătesc materiale de educație medicală despre sănătatea pielii, a părului și a
  unghiilor. Fiecare material este documentat și verificat înainte de publicare.”
- Blocul final: „Programările se fac direct la clinică.” și „Alegeți clinica potrivită
  pentru dumneavoastră și contactați recepția pentru disponibilitate și programare.”
- Citatul evidențiat este preluat identic din „Viziunea mea”.

## Despre mine (`despre-mine.html`)

- Blocul „Ce urmează”, care trimite către pagina „Viziunea mea”.
- În rest, pagina conține numai textul aprobat. Nu am adăugat niciun subtitlu:
  pagina începe direct cu propriile dumneavoastră cuvinte.

## Viziunea mea (`viziunea-mea.html`)

- Blocul „Ce urmează”, care trimite către servicii și locații.
- În rest, pagina conține numai textul aprobat.

## Servicii și consultații (`servicii.html`)

- Subtitlu: „Indicația pentru orice investigație sau procedură se stabilește în urma
  consultației și a evaluării medicale individuale.”
- Blocul final: „Nu sunteți sigur ce fel de consultație vă este necesară?” și
  „Consultația dermatologică este punctul de plecare: în cadrul ei stabilim împreună ce
  evaluări sau proceduri sunt potrivite.”

  Formularea „Nu sunteți sigur” folosește masculinul generic. Dacă preferați o formulare
  neutră, o variantă posibilă este „Nu știți ce fel de consultație vă este necesară?”.

## Întrebări frecvente (`intrebari-frecvente.html`)

- Subtitlu: „Informațiile de mai jos au caracter general. Ele nu înlocuiesc consultația
  și evaluarea individuală.”
- Blocul final: „Aveți o întrebare la care nu ați găsit răspuns?” și „Recepția clinicii
  vă poate oferi detalii despre programare, iar restul întrebărilor le putem discuta în
  cadrul consultației.”
- Întrebarea despre urgențe este scoasă din lista pliabilă și afișată permanent, ca să
  fie vizibilă fără niciun clic. Textul răspunsului este neschimbat.

## Unde mă găsiți (`unde-ma-gasiti.html`)

- Subtitlu: „Consult în București, Ploiești și Buzău. Programările și disponibilitatea
  consultațiilor se confirmă direct la recepția clinicii alese.”
- Eticheta „Consultații disponibile și prin CAS”, afișată la Ana Medical Care și
  Renew Institute.
- Secțiunea „Înainte de a suna”:
  - „Clinicile sunt entități independente și își administrează propriile programe,
    tarife și proceduri de programare. Programul meu nu este publicat pe acest site:
    recepția clinicii vă poate spune care sunt intervalele disponibile.”
  - „Nu ofer consultații online și nu stabilesc diagnostice pe baza fotografiilor sau a
    mesajelor. Vă rugăm să nu transmiteți informații medicale sau imagini prin canale
    nesecurizate.” — reformulare a răspunsului aprobat despre consultațiile online.
- Secțiunea „În caz de urgență” reia, cuvânt cu cuvânt, primul și al doilea paragraf din
  răspunsul aprobat despre urgențe.

## Articole (`articole.html`)

- Subtitlu și cele trei paragrafe din caseta „În pregătire”.

## Subsolul fiecărei pagini

- „Informațiile de pe acest site au caracter educativ și nu înlocuiesc consultația,
  diagnosticul sau tratamentul medical personalizat.”
- „În situații care pun în pericol viața sau sănătatea, apelați 112.”

## Titluri și descrieri pentru motoarele de căutare

Fiecare pagină are un `<title>` și o descriere proprie, vizibile în rezultatele
căutărilor. Se găsesc în primele rânduri ale fiecărui fișier HTML, în etichetele
`<title>` și `<meta name="description">`.

## Date structurate (`index.html`)

Pagina principală conține o fișă `Person` în format JSON-LD, cu: numele profesional,
titlul de medic specialist dermatovenerologie, universitatea absolvită, cele trei
societăți profesionale și cele trei orașe. Toate datele provin din textul aprobat
„Despre mine”. Fișa poate fi ștearsă fără niciun efect asupra site-ului.

---

## Rămân de verificat de dumneavoastră

- Adresele, numerele de telefon și linkurile celor cinci clinici.
- Dacă eticheta „Consultații disponibile și prin CAS” este corectă și în acest moment.
- Numărul secundar de la Renew Institute, `021 9035`, este scris în link ca
  `+40219035`. Merită testat de pe un telefon.
- Dacă doriți o pagină separată „Contact și programări” sau păstrăm programările în
  pagina locațiilor, așa cum sunt acum.
