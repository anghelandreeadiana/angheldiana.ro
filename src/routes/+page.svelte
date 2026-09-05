<script lang="ts">
	import { person } from '$lib/content/person';
	import Button from '$lib/ui/Button';
	import CityCard from '$lib/components/CityCard';
	import Container from '$lib/ui/Container';
	import Section from '$lib/ui/Section';
</script>

<svelte:head>
	<!-- This JSON contains only local, reviewed data; escape HTML delimiters. -->
	{@html `<script type="application/ld+json">${JSON.stringify(person).replace(/</g, '\\u003c')}</script>`}
</svelte:head>

<section class="opening">
  <Container>
    <div>
      <p class="hero-kicker">Dermatologie · București · Ploiești / Păuleștii Noi · Buzău</p>
      <h1><span>Dr. Anghel</span><span class="accent">Andreea-Diana</span></h1>
      <p class="role">Medic specialist dermatovenerologie</p>
      <p class="lead">Sunt medic specialist dermatovenerologie, cu formare în România, Germania și Franța.</p>
      <p class="lead">Consult în București, Ploiești și Buzău. Consultațiile se desfășoară în cabinet, pe baza unei programări.</p>
      <div class="btn-row">
        <Button href="/unde-ma-gasiti#programari">Unde mă găsiți</Button>
        <a href="/despre-mine">Parcursul meu profesional</a>
      </div>
    </div>
    <figure class="portrait">
      <img src="/images/dr-anghel-andreea-diana.jpg" width="1536" height="2048" fetchpriority="high" decoding="async" alt="Portret: Dr. Anghel Andreea-Diana, medic specialist dermatovenerologie">
    </figure>
  </Container>
</section>

<section class="fact-bar" aria-label="Pe scurt">
  <Container>
    <p><strong>Medic specialist</strong><small>Dermatovenerologie</small></p>
    <p><strong>Formare internațională</strong><small>România · Germania · Franța</small></p>
    <p><strong>Consultații în cabinet</strong><small>București · zona Ploiești · Buzău</small></p>
  </Container>
</section>

<Section tone="lavender" class="home-services">
    <div class="band-head">
      <h2>Consultații și servicii</h2>
      <p>Fiecare recomandare pornește de la consultație și de la evaluarea situației individuale.</p>
    </div>
    <ul class="index-list">
    <li><a href="/servicii#consultatie-dermatologica-pentru-adulti-si-copii">Consultație dermatologică pentru adulți și copii</a></li>
    <li><a href="/servicii#dermatoscopie-si-evaluarea-alunitelor">Dermatoscopie și evaluarea alunițelor</a></li>
    <li><a href="/servicii#afectiunile-parului-si-ale-unghiilor">Afecțiunile părului și ale unghiilor</a></li>
    <li><a href="/servicii#infectii-cu-transmitere-sexuala">Infecții cu transmitere sexuală</a></li>
    <li><a href="/servicii#proceduri-si-chirurgie-dermatologica">Proceduri și chirurgie dermatologică</a></li>
    <li><a href="/servicii#dermatologie-regenerativa-si-proceduri-estetice-minim-invazive">Dermatologie regenerativă și proceduri estetice minim invazive</a></li>
    <li><a href="/servicii#oncodermatologie-si-reactii-cutanate-asociate-tratamentelor-oncologice">Oncodermatologie și reacții cutanate asociate tratamentelor oncologice</a></li>
    <li><a href="/servicii#afectiuni-ale-mucoasei-ano-genitale">Afecțiuni ale mucoasei ano-genitale</a></li>
    </ul>
  </Section>

<Section tone="mint">
    <figure class="pull">
      <blockquote>„Un diagnostic nu ar trebui doar comunicat, ci și explicat.”</blockquote>
      <figcaption><a href="/viziunea-mea">Viziunea mea despre relația medic–pacient</a></figcaption>
    </figure>
  </Section>

<Section>
    <div class="band-head">
      <h2>Unde mă găsiți</h2>
      <p>Disponibilitatea consultațiilor și programările se confirmă direct la recepția clinicii.</p>
    </div>
    <div class="city-row">
      <CityCard href="/unde-ma-gasiti#bucuresti" title="București" description="Ana Medical Care · Renew Institute" />
      <CityCard href="/unde-ma-gasiti#ploiesti" title="Ploiești" description="Roua Medical Center" />
      <CityCard href="/unde-ma-gasiti#buzau" title="Buzău" description="Angi San · Laurus Medical Buzău – Medicover" />
    </div>
    <div class="btn-row">
      <Button href="/unde-ma-gasiti" variant="ghost">Adrese și numere de telefon</Button>
    </div>
  </Section>

<Section tone="lavender">
    <div class="band-head">
      <h2>Întrebări frecvente</h2>
      <p>Răspunsuri la întrebările pe care pacienții le adresează cel mai des înaintea unei consultații.</p>
    </div>
    <ul class="index-list">
    <li><a href="/intrebari-frecvente#cat-dureaza-o-consultatie-dermatologica">Cât durează o consultație dermatologică?</a></li>
    <li><a href="/intrebari-frecvente#cum-ma-pregatesc-pentru-consultatia-dermatologica">Cum mă pregătesc pentru consultația dermatologică?</a></li>
    <li><a href="/intrebari-frecvente#este-necesara-o-consultatie-inaintea-unei-proceduri-dermatologice">Este necesară o consultație înaintea unei proceduri dermatologice?</a></li>
    <li><a href="/intrebari-frecvente#cand-este-recomandata-dermatoscopia">Când este recomandată dermatoscopia?</a></li>
    </ul>
    <div class="btn-row">
      <Button href="/intrebari-frecvente" variant="ghost">Toate întrebările</Button>
    </div>
  </Section>

<Section compact>
    <div class="two-up">
      <h2>Articole</h2>
      <div>
        <p>Pregătesc materiale de educație medicală despre sănătatea pielii, a părului și a unghiilor. Fiecare material este documentat și verificat înainte de publicare.</p>
        <p><a href="/articole">Despre secțiunea de articole</a></p>
      </div>
    </div>
  </Section>

<Section tone="sky" compact>
    <p class="kicker">Programări</p>
    <h2>Programările se fac direct la clinică.</h2>
    <p class="measure">Alegeți clinica potrivită pentru dumneavoastră și contactați recepția pentru disponibilitate și programare.</p>
    <div class="btn-row">
      <Button href="/unde-ma-gasiti#programari" variant="light">Vedeți clinicile și telefoanele</Button>
    </div>
  </Section>
