import { defineConfig } from "astro/config";
import { remarkWikiLinks } from "./src/lib/remark-wikilinks.mjs";

// GitHub Pages : https://aannet.github.io/brain-pro/
const base = "/brain-pro";

export default defineConfig({
  site: "https://aannet.github.io",
  base,
  trailingSlash: "always",
  markdown: {
    remarkPlugins: [[remarkWikiLinks, { base }]],
  },
});
