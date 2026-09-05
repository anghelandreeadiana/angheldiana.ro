<script lang="ts">
  import type { Snippet } from 'svelte';
  import './badge.css';
  let { children }: { children: Snippet } = $props();
</script>

<span class="ui-badge">{@render children()}</span>
