export default defineNuxtConfig({
  compatibilityDate: "2026-03-07",
  srcDir: ".",
  devtools: { enabled: process.env.NUXT_DEVTOOLS === "true" || process.env.NODE_ENV !== "production" },
  modules: ["@nuxt/ui"],
  css: ["~/assets/css/main.css"],
  runtimeConfig: {
    apiBaseUrl: process.env.API_BASE_URL || process.env.NUXT_PUBLIC_API_BASE_URL || "http://localhost:8000/api",
    public: {
      apiBaseUrl: process.env.NUXT_PUBLIC_API_BASE_URL || "http://localhost:8000/api",
      siteName: process.env.NUXT_PUBLIC_SITE_NAME || "David Sudi",
    },
  },
  app: {
    head: {
      titleTemplate: "%s | Sudi",
      meta: [
        {
          name: "description",
          content: "Portfolio website for David Sudi - software developer focused on delivering high-performing custom software and AI solutions.",
        },
      ],
    },
  },
})
