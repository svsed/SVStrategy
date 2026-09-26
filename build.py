from pathlib import Path
import html, re

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
    out=[]; table=[]; in_table=False; in_list=False
    def flush_table():
        nonlocal table, in_table
        if not table: return
        headers=table[0]; rows=table[1:]
        out.append('<div class="table-scroll"><table><thead><tr>'+''.join(f"<th>{html.escape(x)}</th>" for x in headers)+'</tr></thead><tbody>')
        for row in rows:
            out.append("<tr>"+''.join(f"<td>{inline(x)}</td>" for x in row)+'</tr>')
        out.append("</tbody></table></div>"); table=[]; in_table=False
    for raw in text.splitlines():
        line=raw.strip()
        if line.startswith("|") and "---" not in line:
            in_table=True; table.append([x.strip() for x in line.strip("|").split("|")]); continue
        if in_table: flush_table()
        if not line:
            if in_list: out.append("</ul>"); in_list=False
            continue
        if line.startswith("# "): out.append(f"<h1>{inline(line[2:])}</h1>")
        elif line.startswith("## "): out.append(f"<h2>{inline(line[3:])}</h2>")
        elif line.startswith("### "): out.append(f"<h3>{inline(line[4:])}</h3>")
        elif line.startswith("- "):
            if not in_list: out.append("<ul>"); in_list=True
            out.append(f"<li>{inline(line[2:])}</li>")
        elif line.startswith("> "): out.append(f"<blockquote>{inline(line[2:])}</blockquote>")
        else:
            if in_list: out.append("</ul>"); in_list=False
            if "→" in line and len(line)<180:
                parts=[x.strip() for x in line.split("→") if x.strip()]
                out.append('<div class="md-flow">'+''.join(f"<span>{inline(x)}</span>" for x in parts)+'</div>')
            else: out.append(f"<p>{inline(line)}</p>")
    if in_table: flush_table()
    if in_list: out.append("</ul>")
    return "\n".join(out)

def inline(s):
    s=html.escape(str(s))
    s=re.sub(r"\*\*(.+?)\*\*",r"<strong>\1</strong>",s)
    return s

SUMMARIES = [
"Why the market is moving, and what that means for the business model.",
"Choose customers by economic shape, not industry alone.",
"The same transformation behaves differently across regions.",
"Translate AI requests into the business constraint underneath.",
"The workflow is the core design object.",
"Where the market is crowded, and where it is still open.",
"The conclusions that survive the evidence.",
"The category Systems Valley can credibly own.",
"The story from business pain to measurable proof.",
"A 90-day system for making the category visible and converting interest.",
"A website that behaves like the product it claims to build.",
"The interactions that turn curiosity into a diagnostic conversation.",
"Three anchor stories, designed around measurable business movement.",
"A commercial journey from discovery to expansion.",
"The recurring logic behind every Systems Valley system.",
"One living intelligence model for every target account."
]

def visual_intro(i):
    blocks = [
      '<div class="visual-kpis"><div><b>20.2%</b><span>OECD firms using AI</span></div><div><b>52%</b><span>Large OECD firms</span></div><div><b>48%</b><span>AI without workflow redesign</span></div><div><b>34%</b><span>Truly reimagining business</span></div></div><div class="viz-bars"><h3>Adoption is moving faster than redesign</h3><div><span>OECD AI adoption</span><i style="width:20.2%"></i><b>20.2%</b></div><div><span>Large firms</span><i style="width:52%"></i><b>52%</b></div><div><span>Workflow redesign gap</span><i style="width:48%"></i><b>48%</b></div></div>',
      '<div class="visual-cards five"><div><b>01</b><strong>Complex operator</strong><span>Many sites, systems, exceptions</span></div><div><b>02</b><strong>Growth constrained</strong><span>Demand leaks before cash</span></div><div><b>03</b><strong>Scale constrained</strong><span>Growth multiplies people</span></div><div><b>04</b><strong>Transformation ready</strong><span>AI pilots in islands</span></div><div><b>05</b><strong>New business</strong><span>Start differently</span></div></div><div class="weight-strip">25 value · 15 complexity · 15 fragmentation · 10 data · 10 AI readiness · 10 urgency · 10 pilotability · 5 expansion</div>',
      '<div class="visual-cards three"><div><b>US</b><strong>Growth + productivity</strong><span>Fast pilots, security, measurable ROI</span></div><div><b>EMEA</b><strong>Governance + trust</strong><span>Regulation, data architecture, oversight</span></div><div><b>APAC</b><strong>Operational leverage</strong><span>Manufacturing, supply chain, regional scale</span></div></div><div class="md-flow"><span>fragmented boundaries</span><span>regional data paths</span><span>policy-aware agents</span><span>human escalation</span><span>observable decisions</span></div>',
      '<div class="visual-cards seven"><div><b>GROW</b><span>Revenue leakage</span><em>pipeline · win rate</em></div><div><b>CONVERT</b><span>Slow response</span><em>cycle time</em></div><div><b>SCALE</b><span>Headcount follows growth</span><em>revenue / FTE</em></div><div><b>OPERATE</b><span>Experts in exceptions</span><em>touchless rate</em></div><div><b>DECIDE</b><span>Data waits</span><em>decision latency</em></div><div><b>RESHAPE</b><span>Pilots stay isolated</span><em>time to production</em></div><div><b>START</b><span>Legacy complexity</span><em>time to market</em></div></div><div class="latent-line"><span>Technology request</span><b>→</b><span>Latent need</span><b>→</b><span>Business KPI</span></div>',
      '<div class="system-flow"><span>Signal</span><span>Context</span><span>Reason</span><span>Act</span><span>Human checkpoint</span><span>Update</span><span>KPI</span><span>Learn</span></div><div class="visual-cards four"><div><b>01</b><strong>Collections</strong><span>ERP + AR + CRM + email</span></div><div><b>02</b><strong>Demand → supply</strong><span>Signals → scenarios → planner</span></div><div><b>03</b><strong>Quote → conversion</strong><span>Intent → context → seller</span></div><div><b>04</b><strong>Service exception</strong><span>Entitlement → route → decide</span></div></div>',
      '<div class="market-map"><span>Accenture</span><span>BCG / BCG X</span><span>Thoughtworks</span><span>EPAM</span><span>Globant</span><span>Cognizant</span><span>Searce</span><span>Genpact</span><strong>Systems Valley</strong></div><div class="whitespace"><span>AI consulting</span><span>Agent development</span><span>Digital transformation</span><span>IT services</span><b>Intelligent business systems</b></div>',
      '<div class="insight-list"><div><b>01</b>AI adoption is not the problem. <strong>Business redesign is.</strong></div><div><b>02</b>The workflow is the <strong>unit of transformation.</strong></div><div><b>03</b>System boundaries are where <strong>value gets stuck.</strong></div><div><b>04</b>Human-in-the-loop is a <strong>design variable.</strong></div><div><b>05</b>Existing systems should be <strong>orchestrated, not replaced.</strong></div><div><b>06</b>Proof must show <strong>business movement.</strong></div></div>',
      '<div class="category-hero"><span>PROPOSED CATEGORY</span><h2>Intelligent Business Transformations</h2><p>Engineer intelligent business systems for companies whose growth or scale has outgrown their current way of working.</p></div><div class="stack-line"><span>Systems</span><span>Data</span><span>People</span><span>AI agents</span><span>Governance</span><b>→ intelligent workflow</b></div><blockquote>Automate what machines should do. Augment what humans should own. Orchestrate everything in between.</blockquote>',
      '<div class="story-ladder"><div>01 · Business pain</div><div>02 · Hidden system friction</div><div>03 · Value opportunity</div><div>04 · Intelligent workflow</div><div>05 · Human checkpoint</div><div>06 · Pilot</div><div>07 · Outcome</div><div>08 · Expansion</div></div><div class="story-callout">Your business already has the systems. The problem is that the work still moves between them manually.</div>',
      '<div class="timeline"><div><b>MONTH 1</b><strong>Make the category visible</strong><span>Website · POV · targeted outreach</span></div><div><b>MONTH 2</b><strong>Show the machinery</strong><span>Demos · before/after · system maps</span></div><div><b>MONTH 3</b><strong>Convert</strong><span>Account pages · assessment · pilot</span></div></div><div class="content-loop">Insight → post → system diagram → video → email → proof story</div>',
      '<div class="ia-visual"><strong>START WITH A PROBLEM</strong><div><span>Explore<br><small>Grow · Convert · Scale · Operate · Decide · Start</small></span><span>Industries<br><small>Manufacturing · Healthcare · Logistics · Services</small></span><span>Systems<br><small>Customer · Revenue · Operations · Supply · Finance</small></span><span>Proof<br><small>Transformations · Experiments · Before / After</small></span></div></div><div class="md-flow"><span>What is changing?</span><span>What is in the way?</span><span>Leverage map</span><span>First experiment</span></div>',
      '<div class="experience-grid"><div><b>01</b><strong>Find your leverage</strong><span>Intent · friction · systems · volume · judgement</span></div><div><b>02</b><strong>System story</strong><span>Fragmented → orchestrated</span></div><div><b>03</b><strong>Executive proof</strong><span>Baseline · intervention · human · outcome</span></div><div><b>04</b><strong>Pilot builder</strong><span>Systems · data · agents · HITL · KPI</span></div></div><div class="before-after"><span>CRM → email → spreadsheet → ERP → human chase</span><b>→</b><span>signal → context → reasoning → approved action → update → exception</span></div>',
      '<div class="visual-cards three"><div><b>01</b><strong>Multi-country manufacturer</strong><span>CRM + SCM + ERP</span><em>OTIF · cycle time · exceptions</em></div><div><b>02</b><strong>Growth-constrained B2B</strong><span>Demand → conversion → expansion</span><em>response · win rate · sales cycle</em></div><div><b>03</b><strong>Scale-constrained operations</strong><span>Expert workflow → supervised agents</span><em>revenue / FTE · cost / transaction</em></div></div><div class="md-flow"><span>Signal</span><span>Friction</span><span>Hidden cost</span><span>New system</span><span>Human role</span><span>Outcome</span><span>Expansion</span></div>',
      '<div class="funnel-visual"><div>01 <b>Discover</b></div><div>02 <b>Qualify</b></div><div>03 <b>Diagnose</b></div><div>04 <b>Prove</b></div><div>05 <b>Transform</b></div><div>06 <b>Amplify</b></div><div>07 <b>Learn</b></div></div><div class="crm-strip">Profile · Problem · Workflow · Value · Sponsor · Urgency · AI maturity · Pilotability · Next action</div>',
      '<div class="loop-visual"><div><b>SEE</b><span>Signals</span></div><i>→</i><div><b>THINK</b><span>Context</span></div><i>→</i><div><b>ACT</b><span>Execution</span></div><i>→</i><div><b>AMPLIFY</b><span>Scale</span></div><i>→</i><div><b>LEARN</b><span>Improve</span></div></div><div class="rule-card">A complete business system explains <strong>what it sees, how it reasons, what it can do, where a human decides and how it learns.</strong></div>',
      '<div class="account-visual"><div class="account-core">ACCOUNT<br>INTELLIGENCE</div><p>Identity · Pressure · Business system · Intelligence · Opportunity · Buying system · Competitive system · Engagement</p></div><div class="state-strip">Unknown → Researched → Hypothesis → Engaged → Diagnosed → Pilot → Proven → Expanded</div>'
    ]
    return blocks[i] if 0 <= i < len(blocks) else ""

def build():
    SITE.mkdir(parents=True, exist_ok=True)
    for md in sorted(RESEARCH.glob("*.md")):
        if md.name == "README.md": continue
        target = SITE / (md.stem + ".html")
        source = md.read_text(encoding="utf-8")
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
            f'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(md.stem)} | Systems Valley Strategy</title><meta name="description" content="{html.escape(SUMMARIES[idx])}"><link rel="stylesheet" href="assets/style.css"></head><body><header class="top"><a class="brand" href="index.html">Systems Valley<span>Strategy</span></a><nav>{nav}</nav></header><div class="strategy-layout">{sidebar}<main class="strategy-content"><div class="part-meta">PART {idx+1:02d} / 16 <span>STRATEGY SYSTEM</span></div><div class="hero compact"><h1>{html.escape(md.stem.replace("-", " ").title())}</h1><p>Systems Valley Strategy</p></div><section class="visual-section">{visual_intro(idx)}</section><details class="research-notes"><summary>Research notes</summary><div class="prose">{body}</div></details>{prevnext}</main></div><footer class="footer">Research cut-off: 26 Sep 2026 · <a href="sources.html">Source register</a></footer></body></html>',
            encoding="utf-8"
        )

if __name__ == "__main__":
    build()
