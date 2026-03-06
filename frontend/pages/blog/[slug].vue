<script setup lang="ts">
import type { BlogPostDetail } from "~/types/api"

const route = useRoute()
const slug = route.params.slug as string

const { apiFetch } = useApi()
const { data: post } = await useAsyncData(`blog-${slug}`, () => apiFetch<BlogPostDetail>(`/blog/${slug}/`))

if (!post.value) {
  throw createError({ statusCode: 404, statusMessage: "Blog post not found" })
}

useSeoMeta({
  title: post.value.title,
  description: post.value.excerpt,
})

const blogThumbnail = computed(() => {
  if (post.value?.cover_image_url) return post.value.cover_image_url
  return "https://images.unsplash.com/photo-1455390582262-044cdead277a?auto=format&fit=crop&w=1200&q=80"
})
</script>

<template>
  <section class="py-14">
    <UContainer class="max-w-4xl space-y-4">
      <UButton to="/blog" variant="ghost" color="neutral" icon="i-lucide-arrow-left">Back</UButton>

      <UCard class="border-slate-200 card-hover-contrast">
        <img :src="blogThumbnail" :alt="post?.title" class="h-72 w-full rounded-xl object-cover" />

        <div class="mt-5 space-y-4">
          <h1 class="text-3xl font-black text-slate-900 md:text-4xl">{{ post?.title }}</h1>
          <p class="text-lg text-slate-900/85">{{ post?.excerpt }}</p>

          <p class="text-xs font-semibold uppercase tracking-wide text-slate-700">
            {{ post?.published_at ? new Date(post.published_at).toLocaleDateString() : "Draft" }}
          </p>

          <div class="flex flex-wrap gap-2">
            <UBadge v-for="tag in post?.tags" :key="tag" variant="soft" color="primary">{{ tag }}</UBadge>
          </div>

          <div class="whitespace-pre-line leading-8 text-slate-900/80">
            {{ post?.content }}
          </div>
        </div>
      </UCard>
    </UContainer>
  </section>

  <CallToAction />
</template>
