import { defineCollection } from "astro:content";
import { glob } from "astro/loaders";
import { z } from "astro/zod";

// Les fiches restent dans ../notes ; le site les lit sans les déplacer.
// Doit rester aligné avec schema/note.schema.json.
const date = z.union([z.date(), z.string().regex(/^\d{4}-\d{2}-\d{2}$/)]).transform((d) =>
  typeof d === "string" ? d : d.toISOString().slice(0, 10),
);

const notes = defineCollection({
  loader: glob({ pattern: "*.md", base: "../notes" }),
  schema: z
    .object({
      title: z.string().min(3),
      url: z.string().url(),
      type: z.enum(["article", "paper", "blog", "doc", "talk", "video", "repo", "book"]),
      authors: z.array(z.string()).default([]),
      published: date.nullable().optional(),
      added: date,
      tags: z.array(z.string().regex(/^[a-z0-9]+(-[a-z0-9]+)*$/)).min(1).max(6),
      status: z.enum(["inbox", "read", "deep-dive"]),
      rating: z.number().int().min(1).max(5).nullable().optional(),
      tldr: z.string().min(10).max(280),
      related: z.array(z.string()).default([]),
    })
    .strict(),
});

export const collections = { notes };
