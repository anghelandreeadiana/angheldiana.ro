# UI primitives

Small Svelte 5 components with TypeScript props and snippets. No UI framework or class-name utility dependency.

```svelte
<script lang="ts">
  import { Button, Section, PageHeader, Accordion, Badge } from '$lib/ui';
</script>

<PageHeader title="Consultații" lead="Informații pentru pacienți." />
<Section tone="lavender" compact>
  <Button href="/unde-ma-gasiti#programari">Vedeți clinicile</Button>
  <Button variant="ghost" onclick={() => console.log('clicked')}>Acțiune</Button>
  <Badge>Informație</Badge>
  <Accordion id="pregatire" title="Cum mă pregătesc?">
    <p>Conținutul răspunsului.</p>
  </Accordion>
</Section>
```

Individual imports also work: `import Button from '$lib/ui/Button'`.

| Component | Props / behavior |
| --- | --- |
| `Button` | `href` renders a real link; otherwise a native button (default type `button`). `variant`: `primary`, `ghost`, `light`; `size`: `default`, `sm`. Native attributes and event handlers are forwarded with TypeScript checking. |
| `Container` | Centers children at the shared maximum width with responsive gutters. Accepts standard div attributes and `class`. |
| `Section` | Section with a Container. `tone`: `paper`, `lavender`, `mint`, `sky`; optional `compact`. Accepts section attributes. |
| `PageHeader` | `title` (the page's h1), optional `lead`, `updated`, and `eyebrow`. Use once per page. |
| `Badge` | Compact informational label with snippet children. |
| `Accordion` | Native details/summary; required unique `id` and `title`, snippet answer. Keyboard interaction works without JavaScript; matching hash opens it after hydration. |

Tokens live in `../styles/tokens.css`. Button, Badge, and Accordion own their CSS; containers, section compositions and page headings use shared responsive foundations from `../styles/site.css`, imported by the root layout. Class names retained from the reference allow its visual identity to be maintained centrally. Keep medical content and clinic records outside generic UI primitives.
