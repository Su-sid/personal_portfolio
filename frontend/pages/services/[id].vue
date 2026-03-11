<script setup lang="ts">
import type { ServiceItem } from "~/types/api"

const route = useRoute()
// Dynamic route param drives the service detail fetch.
const serviceId = route.params.id as string

const { apiFetch } = useApi()
const { data: service } = await useAsyncData(`service-${serviceId}`, () => apiFetch<ServiceItem>(`/services/${serviceId}/`))

if (!service.value) {
  throw createError({ statusCode: 404, statusMessage: "Service not found" })
}

useSeoMeta({
  title: service.value.title,
  description: service.value.excerpt,
})

// Mirror list-page image logic so cards and detail stay visually consistent.
const serviceImage = computed(() => {
  if (!service.value) return ""
  const key = `${service.value.title} ${service.value.summary}`.toLowerCase()
  if (key.includes("ai") || key.includes("automation")) {
    return "https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=1200&q=80"
  }
  if (key.includes("consult")) {
    return "https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=1200&q=80"
  }
  return "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=1200&q=80"
})
</script>

<template>
  <!-- Service detail page showing full description text. -->
  <section class="py-14">
    <UContainer class="max-w-4xl space-y-4">
      <UButton to="/services" variant="soft" color="neutral" icon="i-lucide-arrow-left">Back</UButton>

      <UCard class="surface-card card-hover-contrast">
        <img :src="serviceImage" :alt="service?.title" class="h-72 w-full rounded-xl object-cover" />

        <div class="mt-5 space-y-4">
          <h1 class="text-3xl font-black text-slate-900 md:text-4xl">{{ service?.title }}</h1>
          <!-- Lead summary mirrors blog-detail structure for consistency. -->
          <p class="text-lg text-slate-900/85">{{ service?.excerpt }}</p>

          <div class="flex items-center gap-2 text-slate-500">
            <UIcon :name="service?.icon?.startsWith('i-') ? service.icon : 'i-lucide-sparkles'" class="text-lg" />
            <span class="text-sm font-semibold uppercase tracking-wide">Specialized delivery</span>
          </div>

          <div class="whitespace-pre-line leading-8 text-slate-900/80">
            {{ service?.description }}
          </div>
        </div>
      </UCard>
    </UContainer>
  </section>

  <CallToAction />
</template>
