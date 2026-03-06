<script setup lang="ts">
import type { SiteConfig } from "~/types/api"

const { apiFetch } = useApi()
const { data: config } = await useAsyncData("site-config", () => apiFetch<SiteConfig>("/config/"))

const whatsappLink = computed(() => {
  if (!config.value?.cta.whatsapp_number) return "#"
  const text = encodeURIComponent(config.value.cta.whatsapp_text || "Hi David")
  return `https://wa.me/${config.value.cta.whatsapp_number}?text=${text}`
})
</script>

<template>
  <div class="main-shell">
    <SiteHeader />
    <main>
      <slot />
    </main>
    <SiteFooter />

    <a
      v-if="config?.cta.whatsapp_number"
      class="fixed bottom-4 right-4 z-50 flex h-14 w-14 items-center justify-center rounded-full bg-green-500 text-white shadow-xl transition hover:scale-105"
      :href="whatsappLink"
      target="_blank"
      rel="noreferrer"
      aria-label="Open WhatsApp chat"
      title="Chat on WhatsApp"
    >
      <UIcon name="i-lucide-message-circle" class="text-2xl" />
    </a>
  </div>
</template>
