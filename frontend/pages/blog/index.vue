<script setup lang="ts">
import type { BlogListItem } from "~/types/api"

useSeoMeta({ title: "Blog" })

const route = useRoute()
// Keep search query in sync with URL so results are shareable/bookmarkable.
const query = computed(() => (typeof route.query.q === "string" ? route.query.q : ""))

const { apiFetch } = useApi()
// Refetch list whenever `q` changes in the route query string.
const { data: posts } = await useAsyncData(
  "blog-list",
  () => apiFetch<BlogListItem[]>("/blog/", { query: query.value ? { q: query.value } : {} }),
  { watch: [query] },
)

// Stable card image fallback for posts without uploaded cover images.
const blogThumbnail = (post: BlogListItem) => {
  if (post.cover_image_url) return post.cover_image_url
  return "/images/placeholders/blog.svg"
}
</script>

<template>
  <!-- Blog listing with optional search filter. -->
  <section class="py-14">
    <UContainer class="space-y-6">
      <div class="space-y-2">
        <h1 class="text-3xl font-black text-slate-900 md:text-4xl">Latest Writing</h1>
        <p class="text-slate-700">Insights, lessons, and practical notes from recent builds.</p>
      </div>

      <UCard class="surface-card card-hover-contrast">
        <form method="get" class="flex flex-col gap-3 md:flex-row md:items-center">
          <UInput name="q" type="search" :default-value="query" placeholder="Search articles" icon="i-lucide-search" class="w-full" />
          <UButton type="submit" color="primary" variant="solid" class="font-semibold">Search</UButton>
        </form>
      </UCard>

      <div class="grid gap-6 md:grid-cols-4">
        <NuxtLink v-for="post in posts" :key="post.id" :to="`/blog/${post.slug}`" class="group block">
          <UCard class="surface-card h-full overflow-hidden card-hover-contrast">
            <img
              :src="blogThumbnail(post)"
              :alt="post.title"
              class="h-44 w-full rounded-xl object-cover"
              loading="lazy"
              decoding="async"
            />
            <div class="mt-4 space-y-2">
              <h2 class="text-xl font-extrabold text-slate-900">{{ post.title }}</h2>
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
