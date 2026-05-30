import { defineConfig } from "astro/config";
import tailwind from "@astrojs/tailwind";
import sentry from "@sentry/astro";

export default defineConfig({
  site: 'https://cv.rmnjs.org',
  base: '/',
  trailingSlash: 'always',
  integrations: [
    tailwind(),
    sentry({
      dsn: "https://544bee4c777ee8697e6bcf63b586d1a3@o4511478654631936.ingest.de.sentry.io/4511478661447760",
      sourceMapsUploadOptions: {
        project: "javascript-astro",
        authToken: process.env.SENTRY_AUTH_TOKEN,
      },
    }),
  ],
});
