# Astro 7 exige Node ≥ 22.22 : tag précis pour ne pas réutiliser une image 22 en cache plus ancienne
FROM node:22.23-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
# Umami (optionnel) : injecté dans le HTML au build si fourni
ARG PUBLIC_UMAMI_SRC
ARG PUBLIC_UMAMI_WEBSITE_ID
ENV PUBLIC_UMAMI_SRC=$PUBLIC_UMAMI_SRC \
    PUBLIC_UMAMI_WEBSITE_ID=$PUBLIC_UMAMI_WEBSITE_ID
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
