// Transforme [[slug]] en lien vers /notes/<slug>/.
const WIKI = /\[\[([a-z0-9-]+)\]\]/g;

export function remarkWikiLinks({ base = "" } = {}) {
  const walk = (node) => {
    if (!node.children) return;
    const out = [];
    for (const child of node.children) {
      if (child.type !== "text" || !WIKI.test(child.value)) {
        walk(child);
        out.push(child);
        continue;
      }
      WIKI.lastIndex = 0;
      let last = 0;
      for (const m of child.value.matchAll(WIKI)) {
        if (m.index > last) out.push({ type: "text", value: child.value.slice(last, m.index) });
        out.push({
          type: "link",
          url: `${base}/notes/${m[1]}/`,
          children: [{ type: "text", value: m[1] }],
        });
        last = m.index + m[0].length;
      }
      if (last < child.value.length) out.push({ type: "text", value: child.value.slice(last) });
    }
    node.children = out;
  };
  return (tree) => walk(tree);
}
