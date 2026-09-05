<script lang="ts">
	import ClinicCard from '$lib/components/ClinicCard';
	import Container from '$lib/ui/Container';
	import PageHeader from '$lib/ui/PageHeader';
	import Section from '$lib/ui/Section';
	import { clinics } from '$lib/content/clinics';
</script>

<PageHeader eyebrow="Dr. Anghel · Dermatovenerologie" title="Unde mă găsiți" lead="Consult în București, Ploiești și Buzău. Programările și disponibilitatea consultațiilor se confirmă direct la recepția clinicii alese." />
<nav class="city-jump wrap" aria-label="Salt rapid la oraș">
  <a href="#bucuresti">București</a>
  <a href="#ploiesti">Ploiești / Păuleștii Noi</a>
  <a href="#buzau">Buzău</a>
</nav>
<Container class="cities" id="programari">
  <section class="city" id="bucuresti">
    <h2>București</h2>
    <div class="clinics">
    <ClinicCard clinic={clinics["Ana Medical Care"]} />
    <ClinicCard clinic={clinics["Renew Institute"]} />
    </div>
  </section>
  <section class="city" id="ploiesti">
    <h2>Ploiești</h2>
    <div class="clinics">
    <ClinicCard clinic={clinics["Roua Medical Center"]} />
    </div>
  </section>
  <section class="city" id="buzau">
    <h2>Buzău</h2>
    <div class="clinics">
    <ClinicCard clinic={clinics["Angi San"]} />
    <ClinicCard clinic={clinics["Laurus Medical Buzău – Medicover"]} />
    </div>
  </section>
</Container>

<Section tone="lavender" compact>
    <div class="measure">
      <h2>Înainte de a suna</h2>
      <p>Clinicile sunt entități independente și își administrează propriile programe, tarife și proceduri de programare. Programul meu nu este publicat pe acest site: recepția clinicii vă poate spune care sunt intervalele disponibile.</p>
      <p>Nu ofer consultații online și nu stabilesc diagnostice pe baza fotografiilor sau a mesajelor. Vă rugăm să nu transmiteți informații medicale sau imagini prin canale nesecurizate.</p>
    </div>
  </Section>

<Section compact>
    <div class="measure">
      <h2>În caz de urgență</h2>
      <p>Dacă simptomele sunt severe, apar brusc sau se agravează rapid, solicitați fără întârziere o evaluare medicală într-un serviciu de urgență. Dacă situația poate pune în pericol viața, integritatea sau sănătatea și este necesară intervenția imediată, apelați 112.</p>
      <p><a href="/intrebari-frecvente#ce-trebuie-sa-fac-intr-o-posibila-urgenta-dermatologica">Semnele care pot indica o urgență dermatologică</a></p>
    </div>
  </Section>

