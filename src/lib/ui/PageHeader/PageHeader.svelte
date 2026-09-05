<script lang="ts">
  import Container from '../Container';
  let { title, lead, updated, eyebrow }: { title: string; lead?: string; updated?: string; eyebrow?: string } = $props();
</script>

<section class="page-head">
  <Container>
    {#if eyebrow}<p class="page-kicker">{eyebrow}</p>{/if}
    <h1>{title}</h1>
    {#if lead}<p class="lead">{lead}</p>{/if}
    {#if updated}<p class="updated">{updated}</p>{/if}
  </Container>
</section>
