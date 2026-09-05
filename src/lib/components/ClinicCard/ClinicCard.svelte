<script lang="ts">
  import type { Clinic } from '$lib/content/clinics';
  import Button from '$lib/ui/Button';
  import Badge from '$lib/ui/Badge';
  let { clinic }: { clinic: Clinic } = $props();
</script>

<article class="clinic plate">
  <h3>{clinic.name}</h3>
  <address>{clinic.address}</address>
  {#if clinic.cas}<p><Badge>Consultații disponibile și prin CAS</Badge></p>{/if}
  <div class="actions">
    {#each clinic.phones as phone, index (phone.href)}
      {#if index === 0}
        <Button href={phone.href} aria-label={`Sunați la ${clinic.name}: ${phone.label}`}>{phone.label}</Button>
      {:else}
        <a class="alt" href={phone.href}>{phone.label}</a>
      {/if}
    {/each}
    <a class="alt" href={clinic.website.href} target="_blank" rel="noopener noreferrer">{clinic.website.label}<span class="sr-only"> (se deschide într-o filă nouă)</span></a>
  </div>
</article>
