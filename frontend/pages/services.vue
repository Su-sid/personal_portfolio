<script setup lang="ts">
import type { ServiceItem } from "~/types/api"

useSeoMeta({ title: "Services" })

const { apiFetch } = useApi()
const { data: services } = await useAsyncData("services", () => apiFetch<ServiceItem[]>("/services/"))

const serviceImage = (service: ServiceItem) => {
  const key = `${service.title} ${service.summary}`.toLowerCase()
  if (key.includes("ai") || key.includes("automation")) {
    return "https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=1200&q=80"
  }
  if (key.includes("consult")) {
    return "https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=1200&q=80"
  }
  return "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=1200&q=80"
}
</script>

<template>
  <section class="py-14">
    <UContainer class="space-y-6">
      <UCard
        v-for="service in services"
        :id="`service-${service.id}`"
        :key="service.id"
        class="overflow-hidden border-slate-200 card-hover-contrast"
      >
        <div class="grid gap-5 md:grid-cols-[320px_1fr] md:items-center">
          <img :src="serviceImage(service)" :alt="service.title" class="h-56 w-full rounded-xl object-cover" />
          <div class="space-y-3">
            <h2 class="text-2xl font-extrabold text-slate-900">{{ service.title }}</h2>
            <p class="text-slate-900/85">{{ service.description }}</p>
            <div class="flex items-center gap-2 text-slate-500">
              <UIcon :name="service.icon.startsWith('i-') ? service.icon : 'i-lucide-sparkles'" class="text-lg" />
              <span class="text-sm font-semibold uppercase tracking-wide">Specialized delivery</span>
            </div>
          </div>
        </div>
      </UCard>
    </UContainer>
  </section>

  <CallToAction />
</template>
