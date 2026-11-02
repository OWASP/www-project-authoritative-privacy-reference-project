# Regenerating the APVS pages

The YAML files in `yaml/` are the source of truth. The Markdown in `docs/` is generated from them and is overwritten on every run.

```
pip install -r tools/requirements.txt
python3 tools/render_md.py            # rebuilds docs/*.md  (add --version 0.7 to change the version shown)
python3 tools/check.py                # validates yaml/ and the links in docs/
```

What reads what:

| Input | Output |
|---|---|
| `yaml/00-introduction.yaml` (top key `introduction`) | `docs/00-introduction.md`, plus the version and the status banner on every page |
| `yaml/01-*.yaml` to `yaml/98-*.yaml` (top key `chapter`) | one chapter page each, `docs/NN-*.md` |
| the same chapter files | the chapter table and level counts in the introduction |
| `yaml/99-*.yaml` (top key `mapping`) | the appendix `docs/99-*.md` |

All wording is edited in `yaml/`, never in `tools/`. That includes the introduction text, the version, the status banners and the appendix lead and coverage legend (`lead`, `coverage_legend` in `99-*.yaml`). In the introduction, a block is `text`, `levels`, `chapters_table` or `bullets`, and the tokens `{version}`, `{total}`, `{l1}`, `{l2}`, `{l3}`, `{appendix_file}` and `{appendix_label}` are filled in at build time. The layout itself lives in the `.j2` templates. The level and type colours are at the top of `render_md.py`.

Adding a chapter is a new `yaml/06-name.yaml` with the same shape as the others. Requirement ids must start with their section id, and `check.py` flags duplicates, bad level or type values, references to ids that do not exist, and broken links.
