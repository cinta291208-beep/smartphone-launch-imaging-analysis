from pathlib import Path
import re, sys

root = Path(__file__).resolve().parents[1]
skill = root / "SKILL.md"
errors = []
if not skill.exists():
    errors.append("SKILL.md missing")
else:
    text = skill.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append("YAML frontmatter missing")
    m = re.search(r"^name:\s*(.+)$", text, re.M)
    if not m or m.group(1).strip() != root.name:
        errors.append("name must match directory")
    name = m.group(1).strip() if m else ""
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        errors.append("invalid kebab-case name")
    d = re.search(r"^description:\s*(.+)$", text, re.M)
    if not d or len(d.group(1).strip()) > 1024:
        errors.append("description missing or too long")
    for heading in ["## Use When","## Don't Use When","## Workflow","## Rules","## Examples","## Edge Cases","## References"]:
        if heading not in text:
            errors.append(f"missing {heading}")
for rel in [
    "references/research-method.md","references/imaging-analysis-framework.md",
    "references/creator-review-framework.md","references/web-design-system.md",
    "references/page-structure.md","assets/report-template.html"
]:
    if not (root/rel).exists():
        errors.append(f"missing {rel}")
if errors:
    print("\n".join("ERROR: "+e for e in errors)); sys.exit(1)
print("OK: package structure and basic SKILL.md checks passed")
