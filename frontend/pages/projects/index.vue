
<template>
  <!-- Project catalog: each card is clickable and opens full project content. -->
  <section class="py-14">
    <UContainer class="space-y-6">
      <NuxtLink v-for="project in projects" :key="project.id" :to="`/projects/${project.id}`" class="group block">
        <UCard class="surface-card overflow-hidden card-hover-contrast">
          <div class="grid gap-5 md:grid-cols-[320px_1fr] md:items-center">
            <img :src="projectThumbnail(project)" :alt="project.title" class="h-56 w-full rounded-xl object-cover" />

            <div class="space-y-4">
              <h2 class="text-2xl font-extrabold text-slate-900">{{ project.title }}</h2>
              <!-- Excerpt prevents long descriptions from expanding list cards. -->
              <p class="text-slate-900/85">{{ project.excerpt }}</p>
              <div class="flex flex-wrap items-center gap-2">
                <UBadge variant="solid" color="primary">{{ project.category.toUpperCase() }}</UBadge>
                <UBadge v-for="tech in project.technologies_used.slice(0, 4)" :key="tech.id" variant="subtle" color="neutral">
                  {{ tech.name }}
                </UBadge>
              </div>
              <div class="flex items-center justify-end">
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
<script setup lang="ts">
import type { ProjectItem } from "~/types/api"

useSeoMeta({ title: "Projects" })

const { apiFetch } = useApi()
// Listing page keeps cards lightweight (excerpt) and links to per-project detail pages.
const { data: projects } = await useAsyncData("projects", () => apiFetch<ProjectItem[]>("/projects/"))

// Prefer explicit project image, then screenshot URL fallback, then a static fallback.
const projectThumbnail = (project: ProjectItem) => {
  if (project.image_url) return project.image_url
  const sourceUrl = project.live_demo_link || project.github_link
  if (sourceUrl) {
    return `https://image.thum.io/get/width/1200/crop/800/noanimate/${sourceUrl}`
  }
  return "https://images.unsplash.com/photo-1518773553398-650c184e0bb3?auto=format&fit=crop&w=1200&q=80"
}
</script>
