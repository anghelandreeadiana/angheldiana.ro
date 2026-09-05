<script lang="ts">
  let { href, title, description }: { href: string; title: string; description: string } = $props();
</script>

<a class="city-card" {href}>
  <h3>{title}</h3>
  <p>{description}</p>
  <span class="city-arrow" aria-hidden="true">↗</span>
</a>
