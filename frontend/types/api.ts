export interface ServiceItem {
  id: number
  title: string
  summary: string
  description: string
  icon: string
  display_order: number
  is_featured: boolean
}

export interface TechnologyItem {
  id: number
  name: string
  icon: string
}

export interface ProjectItem {
  id: number
  title: string
  description: string
  category: string
  github_link: string | null
  live_demo_link: string | null
  is_featured: boolean
  created_at: string
  technologies_used: TechnologyItem[]
  image_url: string | null
}

export interface BlogListItem {
  id: number
  title: string
  slug: string
  excerpt: string
  tags: string[]
  published_at: string | null
  created_at: string
  cover_image_url: string | null
}

export interface BlogPostDetail extends BlogListItem {
  content: string
  updated_at: string
}

export interface SiteConfig {
  profile: {
    name: string
    title: string
    tagline: string
    about: string
  }
  cta: {
    calendly_url: string
    whatsapp_number: string
    whatsapp_text: string
    contact_email: string
  }
  social: {
    linkedin_url: string
    github_url: string
    x_url: string
  }
}

export interface LandingPayload {
  services: ServiceItem[]
  featured_projects: ProjectItem[]
  latest_posts: BlogListItem[]
}
