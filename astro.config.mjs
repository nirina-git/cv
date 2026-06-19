import { defineConfig } from "astro/config";
import tailwind from "@astrojs/tailwind";

export default defineConfig({
  site: 'https://cv.rmnjs.org',
  base: '/',
  trailingSlash: 'always',
  integrations: [
    tailwind(),
  ],
});
