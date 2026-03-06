<script setup lang="ts">
import type { SiteConfig } from "~/types/api"

useSeoMeta({ title: "Contact" })

interface ContactState {
  full_name: string
  email: string
  message: string
}

const { apiFetch } = useApi()
const { data: config } = await useAsyncData("site-config-contact", () => apiFetch<SiteConfig>("/config/"))

useHead({
  script: [
    {
      src: "https://assets.calendly.com/assets/external/widget.js",
      async: true,
      type: "text/javascript",
    },
  ],
})

const scheduleUrl = computed(() => config.value?.cta.calendly_url || "https://calendly.com/davidsudi20/30min")

const state = reactive<ContactState>({
  full_name: "",
  email: "",
  message: "",
})

const isSubmitting = ref(false)
const statusMessage = ref("")
const statusType = ref<"success" | "error" | "">("")

const validate = (value: ContactState) => {
  const errors: Array<{ name: keyof ContactState; message: string }> = []

  if (!value.full_name.trim()) {
    errors.push({ name: "full_name", message: "Full name is required." })
  }

  if (!value.email.trim()) {
    errors.push({ name: "email", message: "Email is required." })
  } else if (!/^\S+@\S+\.\S+$/.test(value.email)) {
    errors.push({ name: "email", message: "Enter a valid email address." })
  }

  if (!value.message.trim()) {
    errors.push({ name: "message", message: "Project details are required." })
  }

  return errors
}

const submit = async () => {
  isSubmitting.value = true
  statusMessage.value = ""
  statusType.value = ""

  try {
    await apiFetch("/contact/", {
      method: "POST",
      body: state,
    })

    statusType.value = "success"
    statusMessage.value = "Message sent successfully. I will get back to you soon."

    state.full_name = ""
    state.email = ""
    state.message = ""
  } catch (_error) {
    statusType.value = "error"
    statusMessage.value = "Unable to send your message right now. Please use WhatsApp instead."
  } finally {
    isSubmitting.value = false
  }
}
</script>

<template>
  <section class="py-14">
    <UContainer class="space-y-6">
      <UCard class="border-slate-200 card-hover-contrast">
        <template #header>
          <h1 class="text-2xl font-black text-slate-900">Contact Us</h1>
        </template>

        <UForm :state="state" :validate="validate" class="space-y-4" @submit="submit">
          <UFormField name="full_name" label="Full Name" required>
            <UInput v-model="state.full_name" placeholder="Your full name" class="w-full" />
          </UFormField>

          <UFormField name="email" label="Email" required>
            <UInput v-model="state.email" type="email" placeholder="you@example.com" class="w-full" />
          </UFormField>

          <UFormField name="message" label="Project Details" required>
            <UTextarea v-model="state.message" :rows="6" placeholder="Share your goals, timeline, and budget range." class="w-full" />
          </UFormField>

          <UButton type="submit" color="primary" variant="solid" size="lg" class="font-bold" :loading="isSubmitting">
            Send Message
          </UButton>

          <p v-if="statusMessage" :class="statusType === 'success' ? 'text-emerald-700' : 'text-red-700'" class="font-medium">
            {{ statusMessage }}
          </p>
        </UForm>
      </UCard>

      <UCard class="border-slate-200 card-hover-contrast">
        <template #header>
          <h2 class="text-xl font-bold text-slate-900">Schedule a Free Consultation</h2>
        </template>

        <div class="calendly-inline-widget" :data-url="scheduleUrl" style="min-width:320px;height:700px;" />
      </UCard>
    </UContainer>
  </section>

  <CallToAction />
</template>
