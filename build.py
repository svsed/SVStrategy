from pathlib import Path
import html

ROOT = Path(__file__).parent
RESEARCH = ROOT / "research"
SITE = ROOT / "site"

PARTS = [
    ("01-changing-industry-landscape.html","Changing Industry Landscape"),
    ("02-business-landscape.html","Business Landscape"),
    ("03-geo-political-scenarios.html","Geo-Political Scenarios"),
    ("04-real-customer-needs.html","Real Customer Needs"),
    ("05-solutioning-examples.html","Solutioning Examples"),
    ("06-competitor-analysis.html","Competitor Analysis"),
    ("07-collated-insights.html","Collated Insights"),
    ("08-sv-whitespace.html","Systems Valley Whitespace"),
    ("09-winning-narrative.html","Systems Valley Winning Narrative"),
    ("10-digital-touchpoints.html","Digital Touchpoints"),
    ("11-website-ia.html","Website IA"),
    ("12-interactions-stories-flow.html","Interactions, Stories & Flow"),
    ("13-case-studies.html","Case Studies"),
    ("14-commercial-funnel.html","Commercial Funnel"),
    ("15-thumb-rule.html","Underlying ThumbRule"),
    ("16-customer-intelligence-map.html","Systems Valley Customer Intelligence Map"),
]

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
        source = md.read_text(encoding="utf-8").replace("SV Strategy", "Systems Valley Strategy").replace("SV", "Systems Valley")
        body = markdown_to_html(source)
        nav = "".join(f'<a href="{href}">{label}</a>' for href,label in NAV)
        current = md.stem + ".html"
        idx = next((i for i,(href,_) in enumerate(PARTS) if href == current), -1)
        sidebar_items = "".join(
            f'<a class="rail-item {"active" if href == current else ""}" href="{href}"><span>{i+1:02d}</span>{label}</a>'
            for i,(href,label) in enumerate(PARTS)
        )
        sidebar = f'<aside class="strategy-rail"><div class="rail-title">16-part strategy</div><a class="rail-overview" href="index.html">Overview</a><div class="rail-list">{sidebar_items}</div></aside>'
        prevnext = ""
        if idx >= 0:
            prev_link = "index.html" if idx == 0 else PARTS[idx-1][0]
            prev_label = "Overview" if idx == 0 else PARTS[idx-1][1]
            next_link = PARTS[idx+1][0] if idx < len(PARTS)-1 else "index.html"
            next_label = PARTS[idx+1][1] if idx < len(PARTS)-1 else "Overview"
            prevnext = f'<div class="sequence-nav"><a href="{prev_link}">← {prev_label}</a><a href="{next_link}">{next_label} →</a></div>'
        target.write_text(
            f'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(md.stem)} | Systems Valley Strategy</title><link rel="stylesheet" href="assets/style.css"></head><body><header class="top"><a class="brand" href="index.html">Systems Valley<span>Strategy</span></a><nav>{nav}</nav></header><div class="strategy-layout">{sidebar}<main class="strategy-content"><div class="prose">{body}</div>{prevnext}</main></div><footer class="footer">Research cut-off: 26 Sep 2026</footer></body></html>',
            encoding="utf-8"
        )

if __name__ == "__main__":
    build()
