<script setup lang="ts">
import type { ProjectItem } from "~/types/api"

const route = useRoute()
// Dynamic route param drives the project detail fetch.
const projectId = route.params.id as string

const { apiFetch } = useApi()
const { data: project } = await useAsyncData(`project-${projectId}`, () => apiFetch<ProjectItem>(`/projects/${projectId}/`))

if (!project.value) {
  throw createError({ statusCode: 404, statusMessage: "Project not found" })
}

useSeoMeta({
  title: project.value.title,
  description: project.value.excerpt,
})

// Same fallback strategy as listing page to keep image behavior consistent.
const projectThumbnail = computed(() => {
  if (!project.value) return ""
  if (project.value.image_url) return project.value.image_url
  const sourceUrl = project.value.live_demo_link || project.value.github_link
  if (sourceUrl) {
    return `https://image.thum.io/get/width/1200/crop/800/noanimate/${sourceUrl}`
  }
  return "https://images.unsplash.com/photo-1518773553398-650c184e0bb3?auto=format&fit=crop&w=1200&q=80"
})
</script>

<template>
  <!-- Project detail view with full description and optional external links. -->
  <section class="py-14">
    <UContainer class="max-w-4xl space-y-4">
      <UButton to="/projects" variant="soft" color="neutral" icon="i-lucide-arrow-left">Back</UButton>

      <UCard class="surface-card card-hover-contrast">
        <img :src="projectThumbnail" :alt="project?.title" class="h-72 w-full rounded-xl object-cover" />

        <div class="mt-5 space-y-4">
          <h1 class="text-3xl font-black text-slate-900 md:text-4xl">{{ project?.title }}</h1>
          <!-- Lead summary mirrors blog-detail structure for consistent reading flow. -->
          <p class="text-lg text-slate-900/85">{{ project?.excerpt }}</p>

          <div class="flex flex-wrap items-center gap-2">
            <UBadge variant="solid" color="primary">{{ project?.category.toUpperCase() }}</UBadge>
            <UBadge v-for="tech in project?.technologies_used.slice(0, 8)" :key="tech.id" variant="soft" color="neutral">
              {{ tech.name }}
            </UBadge>
          </div>

          <div class="whitespace-pre-line leading-8 text-slate-900/80">
            {{ project?.description }}
          </div>

          <!-- Optional outbound links are rendered only when provided for this project. -->
          <div class="flex flex-wrap gap-3">
            <UButton
              v-if="project?.github_link"
              :to="project.github_link"
              target="_blank"
              color="neutral"
              variant="soft"
              icon="i-lucide-github"
            >
              View Source
            </UButton>
            <UButton
              v-if="project?.live_demo_link"
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
      </UCard>
    </UContainer>
  </section>

  <CallToAction />
</template>
