<script lang="ts">
  import { page } from '$app/state';
  import PageHeader from '$lib/ui/PageHeader';
  import Section from '$lib/ui/Section';
  import Button from '$lib/ui/Button';
</script>

<svelte:head><meta name="robots" content="noindex" /></svelte:head>
<PageHeader title={page.status === 404 ? 'Pagina nu a fost găsită' : 'Pagina nu este disponibilă'} />
<Section compact>
  <p>{page.status === 404 ? 'Verificați adresa sau reveniți la pagina principală.' : 'Încercați să reîncărcați pagina.'}</p>
  <Button href="/">Pagina principală</Button>
</Section>
