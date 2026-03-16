<script setup lang="ts">
import type { ServiceItem } from "~/types/api"

useSeoMeta({ title: "Services" })

const { apiFetch } = useApi()
// Listing page shows service excerpts and routes into full service detail pages.
const { data: services } = await useAsyncData("services", () => apiFetch<ServiceItem[]>("/services/"))

const serviceImage = (_service: ServiceItem) => "/images/placeholders/service.svg"
</script>

<template>
  <!-- Services catalog: summary cards only, full copy lives on detail pages. -->
  <section class="py-14">
    <UContainer class="space-y-6">
      <NuxtLink v-for="service in services" :key="service.id" :to="`/services/${service.id}`" class="group block">
        <UCard class="surface-card overflow-hidden card-hover-contrast">
          <div class="grid gap-5 md:grid-cols-[320px_1fr] md:items-center">
            <img
              :src="serviceImage(service)"
              :alt="service.title"
              class="h-56 w-full rounded-xl object-cover"
              loading="lazy"
              decoding="async"
            />
            <div class="space-y-3">
              <h2 class="text-2xl font-extrabold text-slate-900">{{ service.title }}</h2>
              <!-- Excerpt keeps card heights stable even when full copy is long. -->
              <p class="text-slate-900/85">{{ service.excerpt }}</p>
              <div class="flex items-center justify-between gap-2 text-slate-500">
                <div class="flex items-center gap-2">
                  <UIcon :name="service.icon.startsWith('i-') ? service.icon : 'i-lucide-sparkles'"
                    class="text-lg animate-pulse text-neutral-900" />
                  <span class="text-sm font-semibold uppercase tracking-wide">Specialized delivery</span>
                </div>
                <UIcon name="i-lucide-arrow-up-right" class="text-primary-500" />
              </div>
            </div>
          </div>
        </UCard>
      </NuxtLink>
    </UContainer>
  </section>

  <CallToAction />
</template>
