<script lang="ts">
  import Container from '$lib/ui/Container';
  import { site, footerNavigation } from '$lib/content/site';
</script>

<footer class="site-foot">
  <Container>
    <div class="top">
      <div class="who"><span class="name">{site.name}</span><p>{site.role}</p></div>
      <nav aria-label="Pagini suplimentare și juridice">
        {#each footerNavigation as item (item.href)}<a href={item.href}>{item.label}</a>{/each}
      </nav>
    </div>
    <div class="notes">
      <p>Informațiile de pe acest site au caracter educativ și nu înlocuiesc consultația, diagnosticul sau tratamentul medical personalizat.</p>
      <p><strong>În situații care pun în pericol viața sau sănătatea, apelați 112.</strong></p>
    </div>
  </Container>
</footer>
