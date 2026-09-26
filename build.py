from pathlib import Path
import html

ROOT = Path(__file__).parent
RESEARCH = ROOT / "research"
SITE = ROOT / "site"

NAV = [
    ("index.html","Overview"),
    ("01-changing-industry-landscape.html","Market"),
    ("02-business-landscape.html","Customers"),
    ("06-competitor-analysis.html","Competition"),
    ("08-sv-whitespace.html","Positioning"),
    ("11-website-ia.html","Website"),
    ("16-customer-intelligence-map.html","Intelligence Map"),
]

def markdown_to_html(text):
    out=[]
    for line in text.splitlines():
        if line.startswith("# "): out.append(f"<h1>{html.escape(line[2:])}</h1>")
        elif line.startswith("## "): out.append(f"<h2>{html.escape(line[3:])}</h2>")
        elif line.startswith("### "): out.append(f"<h3>{html.escape(line[4:])}</h3>")
        elif line.startswith("- "): out.append(f"<li>{html.escape(line[2:])}</li>")
        elif line.strip(): out.append(f"<p>{html.escape(line)}</p>")
    return "\n".join(out)

def build():
    SITE.mkdir(parents=True, exist_ok=True)
    for md in sorted(RESEARCH.glob("*.md")):
        if md.name == "README.md": continue
        target = SITE / (md.stem + ".html")
        body = markdown_to_html(md.read_text(encoding="utf-8"))
        nav = "".join(f'<a href="{href}">{label}</a>' for href,label in NAV)
        target.write_text(
            f'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(md.stem)} | SV Strategy</title><link rel="stylesheet" href="assets/style.css"></head><body><header class="top"><a class="brand" href="index.html">SV<span>Strategy</span></a><nav>{nav}</nav></header><main class="wrap"><div class="prose">{body}</div></main><footer class="footer">Research cut-off: 26 Sep 2026</footer></body></html>',
            encoding="utf-8"
        )

if __name__ == "__main__":
    build()
