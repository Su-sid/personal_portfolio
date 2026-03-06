<script setup lang="ts">
import type { BlogListItem } from "~/types/api"

useSeoMeta({ title: "Blog" })

const route = useRoute()
const query = computed(() => (typeof route.query.q === "string" ? route.query.q : ""))

const { apiFetch } = useApi()
const { data: posts } = await useAsyncData(
  "blog-list",
  () => apiFetch<BlogListItem[]>("/blog/", { query: query.value ? { q: query.value } : {} }),
  { watch: [query] },
)

const blogThumbnail = (post: BlogListItem) => {
  if (post.cover_image_url) return post.cover_image_url
  return "https://images.unsplash.com/photo-1455390582262-044cdead277a?auto=format&fit=crop&w=1200&q=80"
}
</script>

<template>
  <section class="py-14">
    <UContainer class="space-y-6">
      <UCard class="border-slate-200 card-hover-contrast">
        <template #header>
          <h2 class="text-lg font-bold text-slate-900">Find Articles</h2>
        </template>

        <form method="get" class="flex flex-col gap-3 md:flex-row md:items-center">
          <UInput name="q" type="search" :default-value="query" placeholder="Search articles" icon="i-lucide-search" class="w-full" />
          <UButton type="submit" color="primary" variant="solid" class="font-semibold">Search</UButton>
        </form>
      </UCard>

      <div class="grid gap-6 md:grid-cols-3">
        <NuxtLink v-for="post in posts" :key="post.id" :to="`/blog/${post.slug}`" class="group block">
          <UCard class="h-full overflow-hidden border-slate-200 card-hover-contrast">
            <img :src="blogThumbnail(post)" :alt="post.title" class="h-44 w-full rounded-xl object-cover" />
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
