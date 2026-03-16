<script setup lang="ts">
interface ProcessStep {
  id: number
  title: string
  description: string
  icon: string
}

const steps: ProcessStep[] = [
  {
    id: 1,
    title: "Discovery Call",
    description: "We start with a free consultation to understand your vision, goals, and requirements.",
    icon: "i-lucide-message-square",
  },
  {
    id: 2,
    title: "Strategy & Planning",
    description: "A practical roadmap is created with milestones, architecture direction, and timeline.",
    icon: "i-lucide-lightbulb",
  },
  {
    id: 3,
    title: "Design & Development",
    description: "Your solution is designed and engineered with clean, scalable code and clear UX.",
    icon: "i-lucide-code-xml",
  },
  {
    id: 4,
    title: "Testing & Launch",
    description: "We run quality validation and ship with deployment confidence.",
    icon: "i-lucide-rocket",
  },
  {
    id: 5,
    title: "Ongoing Support",
    description: "Post-launch support, performance monitoring, and continuous improvements.",
    icon: "i-lucide-headphones",
  },
]

const timelineRef = ref<HTMLElement | null>(null)
const progress = ref(0)
let frame = 0

// Convert scroll position to 0..1 progress used by the vertical track and nodes.
const updateProgress = () => {
  if (!timelineRef.value || !import.meta.client) return

  const rect = timelineRef.value.getBoundingClientRect()
  const viewport = window.innerHeight
  const start = viewport * 0.5
  const end = rect.height + viewport * 0.35
  const ratio = (start - rect.top) / end
  progress.value = Math.max(0, Math.min(1, ratio))
}

// Marks each step active once scroll progress reaches its position threshold.
const isActive = (index: number) => {
  if (steps.length <= 1) return progress.value > 0
  const threshold = index / (steps.length - 1)
  return progress.value >= threshold
}

const scheduleProgressUpdate = () => {
  if (frame) return
  frame = window.requestAnimationFrame(() => {
    frame = 0
    updateProgress()
  })
}

onMounted(() => {
  updateProgress()
  window.addEventListener("scroll", scheduleProgressUpdate, { passive: true })
  window.addEventListener("resize", scheduleProgressUpdate)
})

onBeforeUnmount(() => {
  if (frame) {
    window.cancelAnimationFrame(frame)
  }
  window.removeEventListener("scroll", scheduleProgressUpdate)
  window.removeEventListener("resize", scheduleProgressUpdate)
})
</script>

<template>
  <!-- Alternating timeline cards with a central progress rail. -->
  <section class="py-16">
    <UContainer>
      <div class="mb-8 flex flex-col items-center gap-3 text-center">
        <h2 class="text-2xl font-extrabold text-slate-900 md:text-3xl">Delivery Process</h2>
        <span class="h-1 w-16 rounded-full bg-primary-500" />
      </div>

      <div ref="timelineRef" class="relative px-2 py-4 md:px-6">
        <div class="process-track" />
        <div class="process-track-progress" :style="{ height: `${progress * 100}%` }" />

        <div class="space-y-12 md:space-y-16">
          <div
            v-for="(step, index) in steps"
            :key="step.id"
            class="relative grid items-center gap-8 md:grid-cols-2"
          >
            <div :class="index % 2 === 0 ? 'md:pr-12' : 'md:order-2 md:pl-12'">
              <article class="timeline-card" :class="isActive(index) ? 'active' : ''">
                <div class="mb-3 flex items-center gap-3 text-slate-600">
                  <UIcon :name="step.icon" class="text-lg" />
                  <span class="text-3xl font-extrabold text-slate-500">{{ String(step.id).padStart(2, "0") }}</span>
                </div>
                <h3 class="mb-2 text-xl font-bold text-slate-900">{{ step.title }}</h3>
                <p class="text-slate-900/85">{{ step.description }}</p>
              </article>
            </div>
            <div v-if="index % 2 !== 0" class="hidden md:block" />
            <span
              class="process-node"
              :class="isActive(index) ? 'active' : 'inactive'"
              :style="{ top: '50%' }"
            >
              {{ String(step.id).padStart(2, "0") }}
            </span>
          </div>
        </div>
      </div>
    </UContainer>
  </section>
</template>
