<script lang="ts">
  import type { LayoutProps } from './$types';
  import { page } from '$app/state';
  import SiteHeader from '$lib/components/SiteHeader.svelte';
  import SiteFooter from '$lib/components/SiteFooter.svelte';
  import { pages } from '$lib/content/pages';
  import { site } from '$lib/content/site';
  import '$lib/styles/fonts.css';
  import '$lib/styles/tokens.css';
  import '$lib/styles/site.css';
  let { children }: LayoutProps = $props();
  const metadata = $derived(pages[page.url.pathname] ?? { title: `Pagină indisponibilă | ${site.name}`, description: site.role });
  const canonical = $derived(`${site.origin}${page.url.pathname}`);
</script>

<svelte:head>
  <title>{metadata.title}</title>
  <meta name="description" content={metadata.description} />
  <meta name="author" content={site.name} />
  <meta name="theme-color" content="#f7f7f2" />
  <meta property="og:type" content="website" />
  <meta property="og:locale" content="ro_RO" />
  <meta property="og:site_name" content={site.name} />
  <meta property="og:title" content={metadata.title} />
  <meta property="og:description" content={metadata.description} />
  <meta property="og:url" content={canonical} />
  <meta property="og:image" content={`${site.origin}/images/og.png`} />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:alt" content={`${site.name} — ${site.role}`} />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:image" content={`${site.origin}/images/og.png`} />
  <link rel="icon" href="/favicon.svg" type="image/svg+xml" />
  <link rel="preload" href="/fonts/Figtree-Variable.woff2" as="font" type="font/woff2" crossorigin="anonymous" />
  <link rel="canonical" href={canonical} />
</svelte:head>

<a class="skip-link" href="#continut">Sari direct la conținut</a>
<SiteHeader />
<main id="continut" tabindex="-1">{@render children()}</main>
<SiteFooter />
