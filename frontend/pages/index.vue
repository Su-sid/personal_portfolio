<script setup lang="ts">
import type { BlogListItem, LandingPayload, ProjectItem, ServiceItem, SiteConfig } from "~/types/api"

useSeoMeta({
  title: "Home",
  description: "Software development, AI solutions, and technical consulting portfolio for David Sudi.",
})

const { apiFetch } = useApi()

const [{ data: config }, { data: landing }] = await Promise.all([
  useAsyncData("site-config-home", () => apiFetch<SiteConfig>("/config/")),
  useAsyncData("landing", () => apiFetch<LandingPayload>("/landing/")),
])

const heroRef = ref<HTMLElement | null>(null)
const spot = reactive({ x: 45, y: 35 })

const handleHeroMove = (event: MouseEvent) => {
  if (!heroRef.value) return
  const rect = heroRef.value.getBoundingClientRect()
  if (!rect.width || !rect.height) return

  spot.x = Math.max(0, Math.min(100, ((event.clientX - rect.left) / rect.width) * 100))
  spot.y = Math.max(0, Math.min(100, ((event.clientY - rect.top) / rect.height) * 100))
}

const resetHeroSpotlight = () => {
  spot.x = 45
  spot.y = 35
}

const serviceImage = (service: ServiceItem) => {
  const key = `${service.title} ${service.summary}`.toLowerCase()
  if (key.includes("ai") || key.includes("automation")) {
    return "https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=1200&q=80"
  }
  if (key.includes("consult")) {
    return "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=1200&q=80"
  }
  return "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?auto=format&fit=crop&w=1200&q=80"
}

const projectThumbnail = (project: ProjectItem) => {
  if (project.image_url) return project.image_url
  const sourceUrl = project.live_demo_link || project.github_link
  if (sourceUrl) {
    return `https://image.thum.io/get/width/1200/crop/800/noanimate/${sourceUrl}`
  }
  return "https://images.unsplash.com/photo-1518773553398-650c184e0bb3?auto=format&fit=crop&w=1200&q=80"
}

const blogThumbnail = (post: BlogListItem) => {
  if (post.cover_image_url) return post.cover_image_url
  return "https://images.unsplash.com/photo-1455390582262-044cdead277a?auto=format&fit=crop&w=1200&q=80"
}
</script>

<template>
  <section
    ref="heroRef"
    class="hero-surface border-b border-slate-200 bg-gradient-to-br from-slate-950 via-slate-900 to-slate-800 text-white"
    :style="{ '--spot-x': `${spot.x}%`, '--spot-y': `${spot.y}%` }"
    @mousemove="handleHeroMove"
    @mouseleave="resetHeroSpotlight"
  >
    <div class="hero-pattern" />
    <div class="hero-spotlight" />

    <UContainer class="relative z-10 grid gap-10 py-16 md:grid-cols-[1.3fr_1fr] md:py-20">
      <div class="space-y-6">
        <UBadge color="neutral" variant="subtle" class="font-bold">Software + AI Delivery</UBadge>
        <h1 class="text-4xl font-black leading-tight md:text-6xl">
          {{ config?.profile?.name }}
        </h1>
        <p class="max-w-2xl text-lg text-slate-100 md:text-xl">{{ config?.profile?.tagline }}</p>

        <UButton to="/contact" color="primary" variant="solid" size="xl" class="font-bold whitespace-nowrap">
          Book a Meet for Free Consultation
        </UButton>
      </div>

      <UCard class="border-white/20 bg-white/10 text-white backdrop-blur card-hover-contrast">
        <template #header>
          <h2 class="text-lg font-bold">Delivery Snapshot</h2>
        </template>
        <p class="hero-about text-base font-semibold">
          {{ config?.profile?.about }}
        </p>
        <div class="mt-6 grid grid-cols-3 gap-3 text-center">
          <div class="rounded-xl border border-white/20 bg-white/10 p-3">
            <p class="text-2xl font-extrabold">{{ landing?.services.length || 0 }}</p>
            <p class="text-xs text-slate-100">Offers</p>
          </div>
          <div class="rounded-xl border border-white/20 bg-white/10 p-3">
            <p class="text-2xl font-extrabold">{{ landing?.featured_projects.length || 0 }}</p>
            <p class="text-xs text-slate-100">Builds</p>
          </div>
          <div class="rounded-xl border border-white/20 bg-white/10 p-3">
            <p class="text-2xl font-extrabold">{{ landing?.latest_posts.length || 0 }}</p>
            <p class="text-xs text-slate-100">Articles</p>
          </div>
        </div>
      </UCard>
    </UContainer>
  </section>

  <section class="py-14">
    <UContainer>
      <div class="mb-7 flex flex-col items-center gap-3 text-center">
        <h2 class="text-2xl font-extrabold text-slate-900 md:text-3xl">Services</h2>
        <span class="h-1 w-16 rounded-full bg-primary-500" />
      </div>

      <div class="grid gap-6 md:grid-cols-3">
        <NuxtLink
          v-for="service in landing?.services"
          :key="service.id"
          :to="`/services#service-${service.id}`"
          class="group block"
        >
          <UCard class="h-full overflow-hidden border-slate-200 card-hover-contrast">
            <img :src="serviceImage(service)" :alt="service.title" class="h-44 w-full rounded-xl object-cover" />
            <div class="mt-4 space-y-3">
              <h3 class="text-lg font-bold text-slate-900">{{ service.title }}</h3>
              <p class="text-sm text-slate-900/85">{{ service.summary }}</p>
              <div class="flex items-center justify-between text-sm font-semibold text-slate-700">
                <span>Explore service</span>
                <UIcon name="i-lucide-arrow-up-right" class="text-slate-700" />
              </div>
            </div>
          </UCard>
        </NuxtLink>
      </div>
    </UContainer>
  </section>

  <ProcessTimeline />

  <section class="py-14">
    <UContainer>
      <div class="mb-6 flex items-center justify-between gap-4">
        <h2 class="text-2xl font-extrabold text-slate-900 md:text-3xl">Selected Builds</h2>
        <UButton to="/projects" variant="soft" color="neutral" trailing-icon="i-lucide-arrow-right">VIEW ALL</UButton>
      </div>

      <div class="grid gap-6 md:grid-cols-2">
        <NuxtLink
          v-for="project in landing?.featured_projects"
          :key="project.id"
          :to="`/projects#project-${project.id}`"
          class="group block"
        >
          <UCard class="h-full overflow-hidden border-slate-200 card-hover-contrast">
            <img :src="projectThumbnail(project)" :alt="project.title" class="h-52 w-full rounded-xl object-cover" />
            <div class="mt-4 space-y-3">
              <h3 class="text-xl font-bold text-slate-900">{{ project.title }}</h3>
              <p class="text-sm text-slate-900/85">{{ project.description }}</p>
              <div class="flex flex-wrap gap-2">
                <UBadge v-for="tech in project.technologies_used.slice(0, 4)" :key="tech.id" variant="subtle" color="neutral">{{ tech.name }}</UBadge>
              </div>
            </div>
          </UCard>
        </NuxtLink>
      </div>
    </UContainer>
  </section>

  <section class="py-14">
    <UContainer>
      <div class="mb-6 flex items-center justify-between gap-4">
        <h2 class="text-2xl font-extrabold text-slate-900 md:text-3xl">Latest Writing</h2>
        <UButton to="/blog" variant="soft" color="neutral" trailing-icon="i-lucide-arrow-right">VIEW ALL</UButton>
      </div>

      <div class="grid gap-6 md:grid-cols-3">
        <NuxtLink v-for="post in landing?.latest_posts" :key="post.id" :to="`/blog/${post.slug}`" class="group block">
          <UCard class="h-full overflow-hidden border-slate-200 card-hover-contrast">
            <img :src="blogThumbnail(post)" :alt="post.title" class="h-44 w-full rounded-xl object-cover" />
            <div class="mt-4 space-y-3">
              <h3 class="text-lg font-bold text-slate-900">{{ post.title }}</h3>
              <p class="text-sm text-slate-900/85">{{ post.excerpt }}</p>
              <p class="text-xs font-semibold uppercase tracking-wide text-slate-700">
                {{ post.published_at ? new Date(post.published_at).toLocaleDateString() : "Draft" }}
              </p>
            </div>
          </UCard>
        </NuxtLink>
      </div>
    </UContainer>
  </section>

  <CallToAction />
</template>
