export const useApi = () => {
  const config = useRuntimeConfig()
  const baseURL = import.meta.server ? config.apiBaseUrl : config.public.apiBaseUrl

  const apiFetch = <T>(path: string, options: Parameters<typeof $fetch<T>>[1] = {}) => {
    return $fetch<T>(path, {
      baseURL,
      ...options,
    })
  }

  return { apiFetch }
}
