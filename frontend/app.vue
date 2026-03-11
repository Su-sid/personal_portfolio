<template>
  <!-- Global UI provider wraps all pages/components with Nuxt UI context. -->
  <UApp>
    <!-- Layout resolves shared chrome (header/footer) around routed page content. -->
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </UApp>
</template>
