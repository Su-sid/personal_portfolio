<script setup lang="ts">
const route = useRoute()

const links = [
  { label: "Home", to: "/" },
  { label: "Services", to: "/services" },
  { label: "Projects", to: "/projects" },
  { label: "Blog", to: "/blog" },
  { label: "Contact", to: "/contact" },
]
</script>

<template>
  <header class="sticky top-0 z-40 border-b border-slate-200/70 bg-white/85 backdrop-blur">
    <UContainer class="flex items-center justify-between gap-4 py-4">
      <NuxtLink to="/" class="text-lg font-extrabold tracking-tight text-slate-900">David Sudi</NuxtLink>

      <nav class="hidden items-center gap-1 md:flex">
        <NuxtLink
          v-for="link in links"
          :key="link.to"
          :to="link.to"
          class="rounded-xl px-3 py-2 text-sm font-semibold transition"
          :class="route.path === link.to ? 'bg-slate-900 text-white' : 'text-slate-600 hover:bg-slate-100 hover:text-slate-900'"
        >
          {{ link.label }}
        </NuxtLink>
      </nav>

      <UButton to="/contact" color="primary" variant="solid" size="md" class="font-bold whitespace-nowrap">
        Book a Meet
      </UButton>
    </UContainer>
  </header>
</template>
