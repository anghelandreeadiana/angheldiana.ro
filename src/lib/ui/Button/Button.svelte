<script lang="ts">
  import type { Snippet } from 'svelte';
  import type { HTMLAnchorAttributes, HTMLButtonAttributes } from 'svelte/elements';
  import './button.css';
  type Shared = { children: Snippet; variant?: 'primary' | 'ghost' | 'light'; size?: 'default' | 'sm'; class?: string };
  type Props = Shared & (
    | (Omit<HTMLAnchorAttributes, 'children'> & { href: string })
    | (Omit<HTMLButtonAttributes, 'children'> & { href?: never })
  );
  let { children, variant = 'primary', size = 'default', class: className = '', ...attributes }: Props = $props();
  const classes = $derived(`btn ${variant === 'primary' ? '' : `btn--${variant}`} ${size === 'sm' ? 'btn--sm' : ''} ${className}`);
</script>

{#if attributes.href !== undefined}
  <a {...attributes as HTMLAnchorAttributes} class={classes}>{@render children()}</a>
{:else}
  <button type="button" {...attributes as HTMLButtonAttributes} class={classes}>{@render children()}</button>
{/if}
