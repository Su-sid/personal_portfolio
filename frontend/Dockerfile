FROM node:22-alpine AS base

WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci

FROM base AS dev
COPY . .
EXPOSE 3000
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "3000"]

FROM base AS build
COPY . .
RUN npm run build

FROM node:22-alpine AS prod
ENV NODE_ENV=production
ENV NITRO_PORT=3000
ENV NITRO_HOST=0.0.0.0

WORKDIR /app
RUN addgroup -S nuxt && adduser -S nuxt -G nuxt
COPY --from=build /app/.output ./.output

USER nuxt
EXPOSE 3000
CMD ["node", ".output/server/index.mjs"]
