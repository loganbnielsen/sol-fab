import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://sol-fab.dev',
  output: 'static',
  build: { format: 'directory' },
  integrations: [sitemap()],
});
