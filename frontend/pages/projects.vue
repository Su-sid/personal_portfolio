<script setup lang="ts">
import type { ProjectItem } from "~/types/api"

useSeoMeta({ title: "Projects" })

const { apiFetch } = useApi()
const { data: projects } = await useAsyncData("projects", () => apiFetch<ProjectItem[]>("/projects/"))

const projectThumbnail = (project: ProjectItem) => {
  if (project.image_url) return project.image_url
  const sourceUrl = project.live_demo_link || project.github_link
  if (sourceUrl) {
    return `https://image.thum.io/get/width/1200/crop/800/noanimate/${sourceUrl}`
  }
  return "https://images.unsplash.com/photo-1518773553398-650c184e0bb3?auto=format&fit=crop&w=1200&q=80"
}
</script>

<template>
  <section class="py-14">
    <UContainer class="space-y-6">
      <UCard
        v-for="project in projects"
        :id="`project-${project.id}`"
        :key="project.id"
        class="overflow-hidden border-slate-200 card-hover-contrast"
      >
        <div class="grid gap-5 md:grid-cols-[320px_1fr] md:items-center">
          <img :src="projectThumbnail(project)" :alt="project.title" class="h-56 w-full rounded-xl object-cover" />

          <div class="space-y-4">
            <h2 class="text-2xl font-extrabold text-slate-900">{{ project.title }}</h2>
            <p class="text-slate-900/85">{{ project.description }}</p>
            <div class="flex flex-wrap items-center gap-2">
              <UBadge variant="subtle" color="neutral">{{ project.category }}</UBadge>
              <UBadge v-for="tech in project.technologies_used.slice(0, 4)" :key="tech.id" variant="soft" color="primary">
                {{ tech.name }}
              </UBadge>
            </div>

            <div class="flex flex-wrap gap-3">
              <UButton
                v-if="project.github_link"
                :to="project.github_link"
                target="_blank"
                color="neutral"
                variant="soft"
                icon="i-lucide-github"
              >
                View Source
              </UButton>
              <UButton
                v-if="project.live_demo_link"
                :to="project.live_demo_link"
                target="_blank"
                color="primary"
                variant="solid"
                icon="i-lucide-external-link"
              >
                View Live Build
              </UButton>
            </div>
          </div>
        </div>
      </UCard>
    </UContainer>
  </section>

  <CallToAction />
</template>
