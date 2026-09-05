<script lang="ts">
  import { afterNavigate } from '$app/navigation';
  import { page } from '$app/state';
  import { onMount } from 'svelte';
  import Button from '$lib/ui/Button';
  import Container from '$lib/ui/Container';
  import { site, navigation } from '$lib/content/site';
  let open = $state(false);
  let ready = $state(false);
  let toggle: HTMLButtonElement;
  let header: HTMLElement;
  afterNavigate(() => { open = false; });
  onMount(() => { ready = true; });
  function onKeydown(event: KeyboardEvent) {
    if (event.key === 'Escape' && open) { open = false; toggle.focus(); }
  }
  function closeOutside(event: MouseEvent) {
    if (event.target instanceof Node && !header.contains(event.target)) open = false;
  }
</script>

<svelte:window onkeydown={onKeydown} onclick={closeOutside} onresize={() => { if (window.innerWidth > 1080) open = false; }} />
<header class="masthead" class:enhanced={ready} bind:this={header}>
  <Container>
    <a class="wordmark" href="/" aria-label={`${site.name} — pagina principală`}>
      <span class="name">{site.name}</span><span class="role">{site.role}</span>
    </a>
    <button class="nav-toggle" type="button" aria-label={open ? 'Închide meniul de navigare' : 'Deschide meniul de navigare'} aria-expanded={open} aria-controls="nav" onclick={() => { open = !open; }} bind:this={toggle}>
      <span class="bars" aria-hidden="true"><i></i><i></i></span>
      <span class="label">{open ? 'Închide' : 'Meniu'}</span><span class="sr-only">de navigare</span>
    </button>
    <nav class="nav" id="nav" data-open={open} aria-label="Navigare principală">
      {#each navigation as item (item.href)}
        <a href={item.href} aria-current={page.url.pathname === item.href ? 'page' : undefined}>{item.label}</a>
      {/each}
      <Button size="sm" href="/unde-ma-gasiti#programari">Programări</Button>
    </nav>
  </Container>
</header>
