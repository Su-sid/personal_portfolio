<script setup lang="ts">
import type { SiteConfig } from "~/types/api"

const { apiFetch } = useApi()
// Pull global CTA settings once for all pages rendered inside this layout.
const { data: config } = await useAsyncData("site-config", () => apiFetch<SiteConfig>("/config/"))

// Build WhatsApp deep-link with optional prefilled message from site config.
const whatsappLink = computed(() => {
  if (!config.value?.cta.whatsapp_number) return "#"
  const text = encodeURIComponent(config.value.cta.whatsapp_text || "Hi Sudi")
  return `https://wa.me/${config.value.cta.whatsapp_number}?text=${text}`
})
</script>

<template>
  <div class="main-shell">
    <!-- Shared site chrome. -->
    <SiteHeader />
    <main>
      <slot />
    </main>
    <SiteFooter />

    <!-- Sticky WhatsApp shortcut appears only when a number is configured. -->
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
