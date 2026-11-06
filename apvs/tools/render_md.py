#!/usr/bin/env python3
"""Regenerate the Markdown pages in docs/ from the YAML files in yaml/.

    python3 tools/render_md.py [--version 0.6]

Inputs  yaml/00-introduction.yaml (introduction text, version, status banner)
        yaml/NN-*.yaml  (NN = 01..98, top key "chapter")   -> docs/NN-*.md
        yaml/99-*.yaml  (top key "mapping", the appendix)   -> docs/99-*.md
        (the introduction page docs/00-introduction.md is generated from the chapter files)
Needs   Python 3.9+, PyYAML, Jinja2   (pip install -r tools/requirements.txt)
The YAML files are the source of truth; edit those and rerun. Files in docs/ are overwritten.
"""
import argparse, glob, os, re, sys
import yaml
from jinja2 import Environment, FileSystemLoader

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, "tools")

LEVELS = {"L1": ("#1a7f37", "rgba(26,127,55,.14)", "Level 1, basic hygiene"),
          "L2": ("#9a6700", "rgba(154,103,0,.14)", "Level 2, standard baseline"),
          "L3": ("#8250df", "rgba(130,80,223,.14)", "Level 3, sensitive data at scale")}
TYPES = {"APP": ("#0969da", "rgba(9,105,218,.12)", "Application-specific"),
         "SYS": ("#57606a", "rgba(87,96,106,.16)", "System-wide")}
DOTS = {"L1": "\U0001F7E2 L1", "L2": "\U0001F7E1 L2", "L3": "\U0001F7E3 L3"}
COVERAGE = {"direct": "**●●● Direct**", "partial": "**●●○ Partial**",
            "supporting": "**●○○ Supporting**"}


def read_yaml(path):
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def write(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(re.sub(r"\n{3,}", "\n\n", text))
    print("wrote", os.path.relpath(path, ROOT))


def liquid_safe(t):
    return "{% raw %}" + t + "{% endraw %}" if ("{{" in t or "{%" in t) else t


def md(t):
    lines = (t or "").replace("\r\n", "\n").strip().split("\n")
    out = [l + ("  " if l.strip() and i + 1 < len(lines) and lines[i + 1].strip() else "") for i, l in enumerate(lines)]
    return liquid_safe("\n".join(out))


def cell(t):
    return liquid_safe(" ".join((t or "").split()).replace("|", "\\|"))


def badge(table, v):
    fg, bg, tip = table[v]
    return (f'<span title="{tip}" style="display:inline-block;padding:0 .55em;border-radius:1em;'
            f'font-size:.85em;font-weight:600;color:{fg};background:{bg};border:1px solid {fg}">{v}</span>')


def anchor(t, pre):
    return pre + "-" + re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


def cite(t):
    S = "§"
    t = re.sub(r"Cal\. Civ\. Code (?=\d)", lambda m: "Cal. Civ. Code " + S + " ", t)
    t = re.sub(r"tit\. 11, (\d+ (?:to|and) \d+)", lambda m: "tit. 11, " + S + S + " " + m.group(1), t)
    return re.sub(r"tit\. 11, (?=\d)", lambda m: "tit. 11, " + S + " ", t)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", help="override the version set in yaml/00-introduction.yaml")
    args = ap.parse_args()
    intro = read_yaml(os.path.join(ROOT, "yaml", "00-introduction.yaml"))["introduction"]
    version = args.version or str(intro["version"])

    env = Environment(loader=FileSystemLoader(TOOLS), keep_trailing_newline=True)
    env.filters.update(md=md, cell=cell, badge_level=lambda v: badge(LEVELS, v), badge_type=lambda v: badge(TYPES, v),
                       dot_level=lambda v: DOTS[v], anchor=anchor, cov=lambda v: COVERAGE[v], para=lambda t: liquid_safe((t or "").strip()))
    os.makedirs(os.path.join(ROOT, "docs"), exist_ok=True)

    chapters = []
    for f in sorted(glob.glob(os.path.join(ROOT, "yaml", "[0-9][0-9]-*.yaml"))):
        if os.path.basename(f).startswith(("00-", "99-")):
            continue
        c = read_yaml(f)["chapter"]
        c["file"] = os.path.basename(f)[:-5] + ".md"
        chapters.append(c)
    mapf = sorted(glob.glob(os.path.join(ROOT, "yaml", "99-*.yaml")))
    appendix = {"file": os.path.basename(mapf[0])[:-5] + ".md" if mapf else "99-regulatory-mapping.md",
                "label": "Appendix A: Regulatory mapping"}

    reqs, where = {}, {}
    for c in chapters:
        for s in c["sections"]:
            for r in s["requirements"]:
                if r["id"] in reqs:
                    sys.exit(f"duplicate requirement id {r['id']}")
                reqs[r["id"]], where[r["id"]] = r, c["file"]

    stats = []
    for c in chapters:
        rq = [r for s in c["sections"] for r in s["requirements"]]
        stats.append({**c, "n": len(rq), **{k: sum(1 for r in rq if r["level"] == k.upper()) for k in ("l1", "l2", "l3")}})
    total = sum(x["n"] for x in stats)
    sums = {k: sum(x[k] for x in stats) for k in ("l1", "l2", "l3")}
    tokens = {"{version}": version, "{total}": str(total), "{l1}": str(sums["l1"]), "{l2}": str(sums["l2"]),
              "{l3}": str(sums["l3"]), "{appendix_file}": appendix["file"], "{appendix_label}": appendix["label"]}

    def fill(x):
        if isinstance(x, str):
            for k, v in tokens.items():
                x = x.replace(k, v)
            return x
        if isinstance(x, list):
            return [fill(i) for i in x]
        if isinstance(x, dict):
            return {k: fill(v) for k, v in x.items()}
        return x
    intro = fill(intro)
    status = intro["status"]
    write(os.path.join(ROOT, "docs", "00-introduction.md"),
          env.get_template("intro.md.j2").render(intro=intro, status=status, chapters=stats, total=total,
                                                 appendix=appendix, **sums))
    tpl = env.get_template("chapter.md.j2")
    for i, c in enumerate(chapters):
        write(os.path.join(ROOT, "docs", c["file"]),
              tpl.render(c=c, status=status, appendix=appendix,
                         prev=chapters[i - 1] if i else None, next=chapters[i + 1] if i + 1 < len(chapters) else None))

    if mapf:
        m = read_yaml(mapf[0])["mapping"]
        for key, items in (("gdpr", "articles"), ("ccpa_cpra", "provisions")):
            for it in m[key][items]:
                for a in it["apvs"]:
                    if a["id"] not in reqs:
                        sys.exit(f"{mapf[0]}: unknown requirement {a['id']}")
            m[key]["groups"] = list(dict.fromkeys(it["group"] for it in m[key][items]))
        for it in m["ccpa_cpra"]["provisions"] + m["ccpa_cpra"].get("not_covered", []):
            it["citation"] = cite(it["citation"])
        rev = {"gdpr": {}, "ccpa": {}}
        for it in m["gdpr"]["articles"]:
            for x in it["apvs"]:
                rev["gdpr"].setdefault(x["id"], []).append(it["article"])
        for it in m["ccpa_cpra"]["provisions"]:
            for x in it["apvs"]:
                rev["ccpa"].setdefault(x["id"], []).append(it["citation"])
        env.filters["reqlink"] = lambda i: f"{where[i]}#req-{i.replace('.', '-')}"
        write(os.path.join(ROOT, "docs", appendix["file"]),
              env.get_template("mapping.md.j2").render(m=m, reqs=reqs, rev=rev, status=status, prev=chapters[-1]))
    else:
        print("no yaml/99-*.yaml found, appendix skipped")


if __name__ == "__main__":
    main()
