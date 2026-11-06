#!/usr/bin/env python3
"""Consistency checks for the APVS YAML and the generated Markdown.  python3 tools/check.py
Exit code 1 when anything fails. Run it after editing yaml/ and after tools/render_md.py."""
import glob, os, re, sys
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errors = []
err = errors.append


def load(p):
    with open(p, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


ids, sections = {}, set()
for f in sorted(glob.glob(os.path.join(ROOT, "yaml", "[0-9][0-9]-*.yaml"))):
    name = os.path.basename(f)
    d = load(f)
    if name.startswith("00-"):
        intro = d.get("introduction") or {}
        for k in ("version", "title", "status", "sections"):
            if not intro.get(k):
                err(f"{name}: introduction.{k} is empty")
        for k in ("headline", "intro_page", "chapter_pages", "appendix_page"):
            if not (intro.get("status") or {}).get(k):
                err(f"{name}: status.{k} is empty")
        known = {"{version}", "{total}", "{l1}", "{l2}", "{l3}", "{appendix_file}", "{appendix_label}"}
        for s in intro.get("sections") or []:
            for b in s.get("blocks") or []:
                if not any(k in b for k in ("text", "levels", "chapters_table", "bullets")):
                    err(f"{name}: section '{s.get('heading')}' has a block of unknown type {sorted(b)}")
                for tok in re.findall(r"\{[a-z0-9_]+\}", str(b)):
                    if tok not in known:
                        err(f"{name}: unknown token {tok} in section '{s.get('heading')}'")
        continue
    if name.startswith("99-"):
        continue
    c = d["chapter"]
    for k in ("number", "slug", "title", "summary", "preface", "sections"):
        if not c.get(k):
            err(f"{name}: chapter.{k} is empty")
    for s in c["sections"]:
        if not s.get("explanation"):
            err(f"{name}: section {s['id']} has no explanation")
        if not s["requirements"]:
            err(f"{name}: section {s['id']} has no requirements")
        sections.add(s["id"])
        for r in s["requirements"]:
            rid = r["id"]
            if set(r) != {"id", "title", "requirement", "guidance", "verification", "level", "type"}:
                err(f"{rid}: unexpected or missing keys {sorted(r)}")
            if rid in ids:
                err(f"duplicate requirement id {rid}")
            ids[rid] = r
            if not rid.startswith(s["id"] + "."):
                err(f"{rid} is listed under section {s['id']}")
            if r["level"] not in ("L1", "L2", "L3"):
                err(f"{rid}: level {r['level']!r}")
            if r["type"] not in ("APP", "SYS"):
                err(f"{rid}: type {r['type']!r}")
            for k in ("title", "requirement"):
                if not r[k]:
                    err(f"{rid}: {k} is empty")
            for k in ("title", "requirement", "guidance", "verification"):
                for m in re.finditer(r"(?<![\w.])(\d{1,2}\.\d{1,2}(?:\.\d{1,2})?)(?![\w])", r[k] or ""):
                    if m.group(1) not in ids and m.group(1) not in sections:
                        pending = (rid, k, m.group(1))
                        errors_pending = globals().setdefault("pending_refs", [])
                        errors_pending.append(pending)

valid = set(ids) | sections
for rid, k, ref in globals().get("pending_refs", []):
    if ref not in valid:
        err(f"{rid}.{k}: reference {ref} points to nothing")

for f in glob.glob(os.path.join(ROOT, "yaml", "99-*.yaml")):
    m = load(f)["mapping"]
    for key, items in (("gdpr", "articles"), ("ccpa_cpra", "provisions")):
        for it in m[key][items]:
            if it["coverage"] not in ("direct", "partial", "supporting"):
                err(f"mapping {key}: bad coverage {it['coverage']!r}")
            for a in it["apvs"]:
                if a["id"] not in ids:
                    err(f"mapping {key}: unknown requirement {a['id']}")

docs = sorted(glob.glob(os.path.join(ROOT, "docs", "*.md")))
anchors, links = set(), []
for f in docs:
    with open(f, encoding="utf-8") as fh:
        t = fh.read()
    b = os.path.basename(f)
    anchors |= {(b, a) for a in re.findall(r'<a id="([^"]+)"', t)}
    links += [(b, l) for l in re.findall(r"\]\(([^)]+)\)", t) + re.findall(r'href="([^"]+)"', t)]
for rid in ids:
    n = sum(open(f, encoding="utf-8").read().count(f'<a id="req-{rid.replace(".", "-")}"></a>') for f in docs)
    if n != 1:
        err(f"docs: requirement {rid} appears {n} times (rerun tools/render_md.py?)")
for src, l in links:
    if l.startswith(("http", "mailto", "{")):
        continue
    tgt, _, frag = l.partition("#")
    tgt = tgt or src
    if not os.path.exists(os.path.join(ROOT, "docs", tgt)):
        err(f"{src}: link to missing file {l}")
    elif frag and (tgt, frag) not in anchors:
        err(f"{src}: link to missing anchor {l}")

print(f"{len(ids)} requirements, {len(sections)} sections, {len(docs)} markdown files")
print("OK" if not errors else f"{len(errors)} problem(s)")
for e in errors:
    print(" -", e)
sys.exit(1 if errors else 0)
