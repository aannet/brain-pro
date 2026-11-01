import { getCollection, type CollectionEntry } from "astro:content";

export type Note = CollectionEntry<"notes">;

export const STATUS_LABEL: Record<string, string> = {
  inbox: "À lire",
  read: "Lu",
  "deep-dive": "Approfondi",
};

export const href = (path: string) => `${import.meta.env.BASE_URL.replace(/\/$/, "")}${path}`;

export async function getNotes(): Promise<Note[]> {
  const notes = await getCollection("notes");
  return notes.sort((a, b) => b.data.added.localeCompare(a.data.added));
}

export function allTags(notes: Note[]): [string, number][] {
  const counts = new Map<string, number>();
  for (const n of notes) for (const t of n.data.tags) counts.set(t, (counts.get(t) ?? 0) + 1);
  return [...counts.entries()].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]));
}

/** Items de la section « À ne pas faire », découpés en [anti-pattern, conséquence]. */
export function antiPatterns(note: Note): { what: string; why: string }[] {
  const body = note.body ?? "";
  const start = body.search(/^## À ne pas faire\s*$/m);
  if (start === -1) return [];
  const rest = body.slice(start).split("\n").slice(1);
  const end = rest.findIndex((l) => /^## /.test(l));
  return rest
    .slice(0, end === -1 ? undefined : end)
    .filter((l) => /^- \S/.test(l))
    .map((l) => {
      const [what, ...why] = l.slice(2).split("→");
      return { what: what.trim(), why: why.join("→").trim() };
    });
}

/** Rendu minimal du Markdown inline (`code`, **gras**) pour les extraits hors rendu complet. */
export function inline(md: string): string {
  return md
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/`([^`]+)`/g, "<code>$1</code>")
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
}
