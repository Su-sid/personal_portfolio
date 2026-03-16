
<template>
  <!-- Project catalog: each card is clickable and opens full project content. -->
  <section class="py-14">
    <UContainer class="space-y-6">
      <NuxtLink v-for="project in projects" :key="project.id" :to="`/projects/${project.id}`" class="group block">
        <UCard class="surface-card overflow-hidden card-hover-contrast">
          <div class="grid gap-5 md:grid-cols-[320px_1fr] md:items-center">
            <img
              :src="projectThumbnail(project)"
              :alt="project.title"
              class="h-56 w-full rounded-xl object-cover"
              loading="lazy"
              decoding="async"
            />

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

// Prefer uploaded project media and keep the fallback local.
const projectThumbnail = (project: ProjectItem) => {
  if (project.image_url) return project.image_url
  return "/images/placeholders/project.svg"
}
</script>
