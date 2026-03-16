<template>
  <!-- Hero section with animated background and interactive spotlight. -->
  <section ref="heroRef"
    class="hero-surface border-b border-slate-200 bg-linear-to-br from-slate-950 via-slate-900 to-slate-800 text-white"
    :style="{ '--spot-x': `${spot.x}%`, '--spot-y': `${spot.y}%` }" @mousemove="handleHeroMove"
    @mouseleave="resetHeroSpotlight">
    <div class="hero-pattern">
      <span v-for="star in heroStars" :key="star.id" class="hero-star" :style="{
        top: star.top,
        left: star.left,
        width: star.size,
        height: star.size,
        '--star-min-opacity': star.minOpacity,
        '--star-delay': star.delay,
        '--star-duration': star.duration,
      }" />
    </div>
    <div class="hero-spotlight" />

    <UContainer class="relative z-10 grid gap-10 py-16 md:grid-cols-[1.3fr_1fr] md:py-20">
      <div class="space-y-6">
        <UBadge color="neutral" variant="subtle" class="font-bold">Software . AI Delivery</UBadge>
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
        <!-- Quick metrics derived from landing payload collections. -->
        <p class="text-base font-semibold text-slate-100/95">
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

  <!-- Services preview: excerpt-only cards with conditional "View All" entry point. -->
  <section class="py-14">
    <UContainer>
      <div class="relative mb-7">
        <div class="flex flex-col items-center gap-3 text-center">
          <h2 class="text-2xl font-extrabold text-slate-900 md:text-3xl">Services</h2>
          <span class="h-1 w-16 rounded-full bg-primary-500" />
        </div>
        <div v-if="landing?.services_has_more"
          class="mt-4 flex justify-center md:absolute md:right-0 md:top-1/2 md:mt-0 md:-translate-y-1/2">
          <UButton to="/services" variant="soft" color="neutral" trailing-icon="i-lucide-arrow-right">
            VIEW ALL
          </UButton>
        </div>
      </div>

      <div class="grid gap-6 md:grid-cols-4">
        <NuxtLink v-for="service in landing?.services" :key="service.id" :to="`/services/${service.id}`"
          class="group block h-full">
          <UCard class="h-full surface-card card-hover-contrast" :ui="{
            root: 'h-full grid grid-rows-[auto_1fr_auto]',
            body: 'p-4 sm:p-6',
            footer: 'p-4 sm:px-6'
          }">
            <img
              :src="serviceImage(service)"
              :alt="service.title"
              class="mb-4 h-44 w-full rounded-xl object-cover"
              loading="lazy"
              decoding="async"
            />

            <div>
              <h3 class="text-lg font-bold text-slate-900">
                {{ service.title }}
              </h3>

              <p class="line-clamp-3 text-sm text-slate-900/85">
                {{ service.excerpt }}
              </p>
            </div>

            <template #footer>
              <div class="text-sm font-semibold text-slate-700">
                <span>Explore service</span>
                <UIcon name="i-lucide-arrow-up-right" class="text-primary-500" />
              </div>
            </template>
          </UCard>
        </NuxtLink>
      </div>
    </UContainer>
  </section>

  <!-- Scroll-reactive process component explains engagement stages. -->
  <ProcessTimeline />

  <!-- Selected builds: capped list on home, full content on project detail pages. -->
  <section class="py-14">
    <UContainer>
      <div class="mb-6 flex items-center justify-between gap-4">
        <h2 class="text-2xl font-extrabold text-slate-900 md:text-3xl">Selected Builds</h2>
        
        <UButton to="/projects" variant="soft" color="neutral" trailing-icon="i-lucide-arrow-right">VIEW ALL</UButton>
      </div>

      <div class="grid gap-6 md:grid-cols-3">
        <NuxtLink v-for="project in landing?.featured_projects" :key="project.id" :to="`/projects/${project.id}`"
          class="group block">
          <UCard class="surface-card h-full overflow-hidden card-hover-contrast">
            <img
              :src="projectThumbnail(project)"
              :alt="project.title"
              class="h-52 w-full rounded-xl object-cover"
              loading="lazy"
              decoding="async"
            />
            <div class="mt-4 space-y-3">
              <h3 class="text-xl font-bold text-slate-900">{{ project.title }}</h3>
              <p class="text-sm text-slate-900/85">{{ project.excerpt }}</p>
              <div class="flex flex-wrap gap-2">
                <UBadge v-for="tech in project.technologies_used.slice(0, 4)" :key="tech.id" variant="subtle"
                  color="neutral">{{ tech.name }}</UBadge>
              </div>
            </div>
          </UCard>
        </NuxtLink>
      </div>
    </UContainer>
  </section>

  <!-- Latest writing cards route to full blog posts. -->
  <section class="py-14">
    <UContainer>
      <div class="mb-6 flex items-center justify-between gap-4">
        <h2 class="text-2xl font-extrabold text-slate-900 md:text-3xl">Latest Writing</h2>
        <UButton to="/blog" variant="soft" color="neutral" trailing-icon="i-lucide-arrow-right">VIEW ALL</UButton>
      </div>

      <div class="grid gap-6 md:grid-cols-3">
        <NuxtLink v-for="post in landing?.latest_posts" :key="post.id" :to="`/blog/${post.slug}`" class="group block">
          <UCard class="surface-card h-full overflow-hidden card-hover-contrast">
            <img
              :src="blogThumbnail(post)"
              :alt="post.title"
              class="h-44 w-full rounded-xl object-cover"
              loading="lazy"
              decoding="async"
            />
            <div class="mt-4 space-y-3">
              <h3 class="text-lg font-bold text-slate-900">{{ post.title }}</h3>
              <p class="text-sm text-slate-900/85">{{ post.excerpt }}</p>
              <p class="text-xs font-semibold uppercase tracking-wide text-slate-900">
                {{ post.published_at ? new Date(post.published_at).toLocaleDateString() : "Draft" }}
              </p>
            </div>
          </UCard>
        </NuxtLink>
      </div>
    </UContainer>
  </section>

  <!-- Reusable CTA closes the page with a contact conversion path. -->
  <CallToAction />
</template>
<script setup lang="ts">
import type { BlogListItem, LandingPayload, ProjectItem, ServiceItem, SiteConfig } from "~/types/api"

useSeoMeta({
  title: "Home",
  description: "Software development, AI solutions, and technical consulting portfolio for David Sudi.",
})

const { apiFetch } = useApi()

// Load site profile copy and landing collections together to reduce page wait time.
const [{ data: config }, { data: landing }] = await Promise.all([
  useAsyncData("site-config", () => apiFetch<SiteConfig>("/config/"), {
    dedupe: "defer",
  }),
  useAsyncData("landing", () => apiFetch<LandingPayload>("/landing/")),
])

const heroRef = ref<HTMLElement | null>(null)
const spot = reactive({ x: 45, y: 35 })
let spotlightFrame = 0
let pendingSpot = { x: 45, y: 35 }
// Pre-compute decorative stars so the template stays lightweight.
const heroStars = Array.from({ length: 64 }, (_, index) => {
  const id = index + 1
  return {
    id,
    top: `${(id * 47) % 100}%`,
    left: `${(id * 73) % 100}%`,
    size: `${1 + ((id * 13) % 3)}px`,
    minOpacity: `${0.2 + ((id * 19) % 50) / 100}`,
    delay: `${((id * 7) % 40) / 10}s`,
    duration: `${4 + ((id * 11) % 50) / 10}s`,
  }
})

// Move the spotlight center based on cursor position inside the hero container.
const handleHeroMove = (event: MouseEvent) => {
  if (!heroRef.value) return
  const rect = heroRef.value.getBoundingClientRect()
  if (!rect.width || !rect.height) return

  pendingSpot = {
    x: Math.max(0, Math.min(100, ((event.clientX - rect.left) / rect.width) * 100)),
    y: Math.max(0, Math.min(100, ((event.clientY - rect.top) / rect.height) * 100)),
  }

  if (spotlightFrame) return
  spotlightFrame = window.requestAnimationFrame(() => {
    spotlightFrame = 0
    spot.x = pendingSpot.x
    spot.y = pendingSpot.y
  })
}

const resetHeroSpotlight = () => {
  if (spotlightFrame) {
    window.cancelAnimationFrame(spotlightFrame)
    spotlightFrame = 0
  }
  spot.x = 45
  spot.y = 35
  pendingSpot = { x: 45, y: 35 }
}

const serviceImage = (_service: ServiceItem) => "/images/placeholders/service.svg"

// Keep project thumbnails local when no uploaded image exists.
const projectThumbnail = (project: ProjectItem) => {
  if (project.image_url) return project.image_url
  return "/images/placeholders/project.svg"
}

// Blog cards use a stable fallback image when no cover image is uploaded.
const blogThumbnail = (post: BlogListItem) => {
  if (post.cover_image_url) return post.cover_image_url
  return "/images/placeholders/blog.svg"
}
</script>
