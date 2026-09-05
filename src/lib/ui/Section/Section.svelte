<script lang="ts">
  import type { Snippet } from 'svelte';
  import type { HTMLAttributes } from 'svelte/elements';
  import Container from '../Container';
  let { children, tone = 'paper', compact = false, class: className = '', ...attributes }: HTMLAttributes<HTMLElement> & {
    children: Snippet; tone?: 'paper' | 'lavender' | 'mint' | 'sky'; compact?: boolean;
  } = $props();
  const tones = { paper: '', lavender: 'band--stone', mint: 'band--blush', sky: 'band--plum' };
</script>

<section {...attributes} class={`band ${tones[tone]} ${compact ? 'band--tight' : ''} ${className}`}>
  <Container>{@render children()}</Container>
</section>
