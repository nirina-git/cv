import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  site: 'https://nirina.rmnjs.org',
  base: '/',
  trailingSlash: 'always',
  // Astro 7 compresse par défaut à la manière de JSX (espaces entre éléments
  // en ligne supprimés : « @ Tech » devenait « @Tech ») ; on garde l'ancien mode.
  compressHTML: true,
  i18n: {
    defaultLocale: 'fr',
    locales: ['fr', 'en'],
    routing: {
      prefixDefaultLocale: false,
    },
  },
  integrations: [sitemap()],
  vite: {
    plugins: [tailwindcss()],
    // Minifieur CSS d'Astro 4/5 : celui de Vite 8 (Lightning CSS) supprime des
    // déclarations de repli (ex. width: fit-content suivi de -moz-fit-content
    // dans hotkeypad) et casse la mise en page de la palette Cmd+K.
    build: { cssMinify: 'esbuild' },
  },
});
