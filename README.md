# angheldiana.ro

SvelteKit 2 / Svelte 5 website for Dr. Anghel Andreea-Diana, migrated from `.old/codex-version`. TypeScript, server-side rendering, and `@sveltejs/adapter-node`. No additional application dependencies, UI libraries, external fonts, analytics, or cookie storage.

## Run locally

```sh
npm install
npm run dev
```

## Check and run the Node build

```sh
npm run check
npm run build
HOST=127.0.0.1 PORT=3000 ORIGIN=http://localhost:3000 npm start
```

`npm start` runs the generated `build/index.js` server. For hosting, set `ORIGIN` to the public HTTPS origin and set `HOST`/`PORT` for your environment. The Node adapter is already configured in `vite.config.ts` using the installed SvelteKit Vite configuration API. No separate `svelte.config.js` is required by this scaffold.

## Structure

```text
src/
  routes/
    +layout.svelte       # Site shell and reactive page metadata
    +layout.ts           # SSR enabled; prerendering disabled
    +page.svelte         # Homepage
    despre-mine/
    viziunea-mea/
    servicii/
    unde-ma-gasiti/
    intrebari-frecvente/
    articole/
    politica-de-confidentialitate/
    politica-de-cookie-uri/
    informatii-legale/
  lib/
    ui/                  # Button, Container, Section, PageHeader, Badge, Accordion
    components/          # SiteHeader, SiteFooter, ClinicCard, CityCard
    content/             # Typed clinic data, navigation, metadata, professional facts
    styles/
      tokens.css         # Shared color, typography, spacing, and radius tokens
      site.css           # Reference layouts, responsive rules, and shared foundations
  hooks.server.ts        # Permanent redirects from known legacy .html URLs
static/
  favicon.svg            # Served as /favicon.svg
  images/                # Served as /images/...
  fonts/                 # Self-hosted Figtree variable fonts and license
```

Each page is a native `+page.svelte` route with semantic markup, rendered on the server on direct requests. SvelteKit handles subsequent client navigation; metadata updates with the route. Mobile navigation and native FAQ disclosures also remain usable with JavaScript disabled. FAQ fragment links open the matching answer after hydration.

Edit reusable primitives in `src/lib/ui`, page compositions in `src/routes`, and site-specific cards/navigation in `src/lib/components`. See [`src/lib/ui/README.md`](src/lib/ui/README.md) for component APIs. Images and favicon are served directly from `static/`, without asset imports.

## Content and publication status

The source is `.old/codex-version`; archives are historical references and are not part of the app build. Its Romanian copy, visual identity, five clinic records, service exclusions, and article preparation state are preserved. The active pages are now Svelte files; the archived Python generator does not regenerate this app.

Approved source text remains in `.old/codex-version/content/`. Outstanding editorial decisions are carried into [`NOTE-DE-APROBAT.md`](NOTE-DE-APROBAT.md). The three legal pages retain their existing draft notices and `[de completat]` fields. No deployment has been performed.
