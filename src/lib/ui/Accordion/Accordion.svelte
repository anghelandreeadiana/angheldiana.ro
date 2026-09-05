<script lang="ts">
  import type { Snippet } from 'svelte';
  import { onMount } from 'svelte';
  import './accordion.css';
  let { id, title, children }: { id: string; title: string; children: Snippet } = $props();
  let details: HTMLDetailsElement;
  function openFromHash() {
    if (window.location.hash.slice(1) === id) details.open = true;
  }
  onMount(openFromHash);
</script>

<svelte:window onhashchange={openFromHash} />
<details class="ui-accordion" {id} bind:this={details}>
  <summary><span>{title}</span><span class="chev" aria-hidden="true"></span></summary>
  <div class="answer">{@render children()}</div>
</details>
