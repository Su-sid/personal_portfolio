<script setup lang="ts">
defineProps<{
  title?: string
  description?: string
}>()
</script>

<template>
  <section class="py-10">
    <UContainer>
      <UCard class="overflow-hidden border-slate-900/15 bg-gradient-to-r from-slate-900 to-slate-700 text-white card-hover-contrast">
        <template #default>
          <div class="flex flex-col items-start justify-between gap-4 md:flex-row md:items-center">
            <div class="space-y-2">
              <h3 class="text-2xl font-bold md:text-3xl">{{ title || "Ready to turn your idea into a reliable product?" }}</h3>
              <p class="max-w-3xl text-slate-200">
                {{ description || "Let us discuss your project goals, priorities, and a delivery roadmap tailored to your business." }}
              </p>
            </div>
            <UButton to="/contact" color="primary" variant="solid" size="xl" class="font-bold whitespace-nowrap">
              Book a Meet for Free Consultation
            </UButton>
          </div>
        </template>
      </UCard>
    </UContainer>
  </section>
</template>
