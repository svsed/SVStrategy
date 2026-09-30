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

GROUPS = [
    ("01 · Understand the market", [
        (0,"Changing industry landscape"),
        (2,"Regional realities"),
        (5,"Competitive landscape"),
    ]),
    ("02 · Understand the customer", [
        (1,"Customer profiles"),
        (3,"Real customer needs"),
        (4,"Solution patterns"),
        (15,"Customer intelligence map"),
    ]),
    ("03 · Define Systems Valley", [
        (6,"Strategic insights"),
        (7,"Category & whitespace"),
        (8,"Winning narrative"),
        (14,"Underlying rule"),
    ]),
    ("04 · Design the experience", [
        (9,"Digital touchpoints"),
        (10,"Website architecture"),
        (11,"Interactions & stories"),
        (12,"Case studies"),
    ]),
    ("05 · Commercialise", [
        (13,"Commercial funnel"),
    ]),
]

SUMMARIES = [
    "How IT/ITeS moved from labor-arbitrage and projects toward AI, intelligent workflows and outcome economics.",
    "Five customer shapes, qualification logic, CXO stories and the complex-operator account pattern.",
    "How regional regulation, data, industrial context and buying expectations change the transformation.",
    "The business constraints underneath requests for AI, automation, agents and modernization.",
    "Concrete intelligent workflow patterns across collections, supply, sales, service and AI production.",
    "Where major services firms converge, and the intelligent-business-system whitespace for Systems Valley.",
    "The strategic conclusions that survive the evidence and shape the operating choices.",
    "The proposed category, proposition, boundaries and commercial shape for Systems Valley.",
    "The narrative from business pain to workflow redesign, human judgement, proof and expansion.",
    "A 90-day digital system that turns research into visibility, machinery demos and commercial conversion.",
    "A website architecture that behaves like the product Systems Valley claims to build.",
    "The interactive experiences that turn curiosity into a leverage map and a pilot conversation.",
    "Three anchor case-study stories and the evidence each needs before publication.",
    "The commercial system from discovery through pilot, transformation, expansion and learning.",
    "The recurring See → Think → Act → Amplify → Learn logic behind every Systems Valley system.",
    "The living account model connecting identity, pressure, systems, intelligence, opportunity, buying and engagement.",
]

def inline(s):
    s = html.escape(str(s), quote=False)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\`(.+?)\`", r"<code>\1</code>", s)
    return s

def markdown_to_html(text):
    out, table, in_list = [], [], False

    def flush_table():
        nonlocal table
        if not table:
            return
        headers, rows = table[0], table[1:]
        out.append('<div class="table-scroll"><table><thead><tr>' +
                   ''.join(f"<th>{inline(x)}</th>" for x in headers) +
                   '</tr></thead><tbody>')
        for row in rows:
            out.append("<tr>" + ''.join(f"<td>{inline(x)}</td>" for x in row) + "</tr>")
        out.append("</tbody></table></div>")
        table = []

    for raw in text.splitlines():
        line = raw.strip()

        if line.startswith("|"):
            if "---" in line:
                continue
            table.append([x.strip() for x in line.strip("|").split("|")])
            continue
        if table:
            flush_table()

        if not line:
            if in_list:
                out.append("</ul>")
                in_list = False
            continue

        if line.startswith("# "):
            out.append(f"<h2>{inline(line[2:])}</h2>")
        elif line.startswith("## "):
            out.append(f"<h3>{inline(line[3:])}</h3>")
        elif line.startswith("### "):
            out.append(f"<h4>{inline(line[4:])}</h4>")
        elif line.startswith("- "):
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{inline(line[2:])}</li>")
        elif line.startswith("> "):
            out.append(f"<blockquote>{inline(line[2:])}</blockquote>")
        elif "→" in line and len(line) < 180:
            pieces = [x.strip() for x in line.split("→") if x.strip()]
            out.append('<div class="md-flow">' + ''.join(f"<span>{inline(x)}</span>" for x in pieces) + "</div>")
        else:
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append(f"<p>{inline(line)}</p>")

    if table:
        flush_table()
    if in_list:
        out.append("</ul>")
    return "\n".join(out)

def rail(current):
    chunks = [
        '<aside class="strategy-rail">',
        '<div class="rail-brand"><a href="index.html">Systems Valley</a><span>Strategy</span></div>',
        f'<a class="rail-overview {"active" if current == "index.html" else ""}" href="index.html"><span>00</span>Overview</a>'
    ]
    for title, items in GROUPS:
        chunks.append(f'<div class="rail-group"><div class="rail-group-title">{html.escape(title)}</div>')
        for idx, label in items:
            href = PARTS[idx][0]
            active = "active" if href == current else ""
            chunks.append(f'<a class="rail-item {active}" href="{href}"><span>{idx+1:02d}</span>{html.escape(label)}</a>')
        chunks.append("</div>")
    chunks.append('<div class="rail-group resources"><div class="rail-group-title">Resources</div>')
    resources = [
        ("sources.html","Sources"),
        ("accounts.html","Target accounts"),
        ("competitors.html","Competitor explorer"),
    ]
    for href, label in resources:
        active = "active" if href == current else ""
        chunks.append(f'<a class="rail-item {active}" href="{href}"><span>↗</span>{label}</a>')
    chunks.append("</div></aside>")
    return "".join(chunks)

def visual_intro(i):
    blocks = [
        """
        <div class="visual-kpis">
          <div><b>$6.37T</b><span>Global IT spend forecast, 2026</span></div>
          <div><b>20.2%</b><span>OECD firms using AI, 2025</span></div>
          <div><b>48%</b><span>Introduced AI without workflow redesign</span></div>
          <div><b>30%</b><span>Forecast modular/platform-enabled services by 2029</span></div>
        </div>
        <div class="timeline-wide">
          <div><b>2015-2018</b><strong>Labor & project scale</strong><span>Application development, infrastructure, maintenance, outsourcing and cost arbitrage</span></div>
          <div><b>2019-2021</b><strong>Cloud & modernization</strong><span>Cloud migration, SaaS, digital products, data platforms and managed services</span></div>
          <div><b>2022-2024</b><strong>GenAI experimentation</strong><span>Copilots, RAG, content generation and functional pilots</span></div>
          <div class="current"><b>2025-2026</b><strong>Agentic pivot</strong><span>Value moves from tasks/projects toward intelligent workflows</span></div>
          <div><b>2027-2031</b><strong>Adaptive business systems</strong><span>Productized services, reusable orchestration, outcome economics and supervised agents</span></div>
        </div>
        """,
        """
        <div class="persona-story">
          <div class="persona-card"><span>PERSONA · COMPLEX OPERATOR</span><h3>“I know where the data lives. I don’t know why the work still needs so many people.”</h3><p>Multi-site packaging group · UK / China / India</p><div class="persona-tags"><b>ERP</b><b>CRM</b><b>SCM</b><b>Email</b><b>People</b></div></div>
          <div class="storyboard"><div><b>01 · Signal</b><span>Demand changes</span></div><div><b>02 · Friction</b><span>Teams reconcile spreadsheets</span></div><div><b>03 · Cost</b><span>Planner time + delayed decisions</span></div><div><b>04 · Opportunity</b><span>Connect systems + exceptions</span></div><div><b>05 · Human role</b><span>Own trade-offs</span></div><div><b>06 · Outcome</b><span>Faster decisions + resilient flow</span></div></div>
        </div>
        <div class="visual-cards five">
          <div><b>01</b><strong>Complex operator</strong><span>Many sites, systems and exceptions</span></div>
          <div><b>02</b><strong>Growth constrained</strong><span>Demand leaks before cash</span></div>
          <div><b>03</b><strong>Scale constrained</strong><span>Growth multiplies people</span></div>
          <div><b>04</b><strong>Transformation ready</strong><span>AI pilots remain fragmented</span></div>
          <div><b>05</b><strong>New business</strong><span>Start differently</span></div>
        </div>
        """,
        """
        <div class="visual-cards three">
          <div><b>US</b><strong>Growth + productivity</strong><span>Fast pilots, security, measurable ROI</span></div>
          <div><b>EMEA</b><strong>Governance + trust</strong><span>Regulation, data architecture, oversight</span></div>
          <div><b>APAC</b><strong>Operational leverage</strong><span>Manufacturing, supply chain, regional scale</span></div>
        </div>
        <div class="regional-flow"><span>Fragmented boundaries</span><b>→</b><span>Regional data paths</span><b>→</b><span>Policy-aware agents</span><b>→</b><span>Human escalation</span><b>→</b><span>Observable decisions</span></div>
        """,
        """
        <div class="needs-grid">
          <div><b>GROW</b><strong>Revenue leakage</strong><span>Pipeline · win rate · revenue</span></div>
          <div><b>CONVERT</b><strong>Slow response</strong><span>Sales cycle · win rate</span></div>
          <div><b>SCALE</b><strong>Headcount follows growth</strong><span>Revenue/FTE · cost/transaction</span></div>
          <div><b>OPERATE</b><strong>Experts trapped in exceptions</strong><span>Cycle time · touchless rate</span></div>
          <div><b>DECIDE</b><strong>Data exists, decisions wait</strong><span>Decision latency · forecast accuracy</span></div>
          <div><b>RESHAPE</b><strong>Pilots stay isolated</strong><span>Time-to-production · reuse</span></div>
          <div><b>START</b><strong>Legacy complexity</strong><span>Time-to-market · cost-to-serve</span></div>
        </div>
        <div class="latent-line"><span>Technology request</span><b>→</b><span>Latent business need</span><b>→</b><span>Measurable KPI</span></div>
        """,
        """
        <div class="system-flow"><span>Signal</span><span>Context</span><span>Reasoning</span><span>Action</span><span>Human checkpoint</span><span>System update</span><span>KPI</span><span>Learning</span></div>
        <div class="visual-cards four">
          <div><b>01</b><strong>Collections</strong><span>ERP + AR + CRM + email</span></div>
          <div><b>02</b><strong>Demand → supply</strong><span>Signals → scenarios → planner</span></div>
          <div><b>03</b><strong>Quote → conversion</strong><span>Intent → context → seller</span></div>
          <div><b>04</b><strong>Service exception</strong><span>Entitlement → route → decide</span></div>
        </div>
        """,
        """
        <div class="competitor-map"><div class="competitor-cloud"><span>Accenture</span><span>BCG / BCG X</span><span>Thoughtworks</span><span>EPAM</span><span>Globant</span><span>Cognizant</span><span>Searce</span><span>Genpact</span></div><div class="whitespace-focus"><small>WHITESPACE</small><strong>Intelligent business systems</strong><span>Across existing systems, data, people and AI</span></div></div>
        <div class="boundary-pills"><span>Not AI consulting</span><span>Not agent development</span><span>Not digital transformation</span><span>Not IT services</span><b>Intelligent business systems</b></div>
        """,
        """
        <div class="insight-list">
          <div><b>01</b><strong>AI adoption is not the problem.</strong><span>Business redesign is.</span></div>
          <div><b>02</b><strong>The workflow is the unit.</strong><span>Transformation happens where work moves.</span></div>
          <div><b>03</b><strong>System boundaries trap value.</strong><span>Orchestration crosses them.</span></div>
          <div><b>04</b><strong>Human-in-the-loop is a variable.</strong><span>Design where judgement belongs.</span></div>
          <div><b>05</b><strong>Orchestrate existing systems.</strong><span>Replace only when justified.</span></div>
          <div><b>06</b><strong>Proof means business movement.</strong><span>Measure the KPI, not AI activity.</span></div>
          <div><b>07</b><strong>Start small, prove value.</strong><span>Then expand through adjacent workflows.</span></div>
          <div><b>08</b><strong>Build reusable IP.</strong><span>Avoid bespoke services every time.</span></div>
          <div><b>09</b><strong>Design for regional reality.</strong><span>Governance and resilience are system properties.</span></div>
          <div><b>10</b><strong>Make the website diagnostic.</strong><span>Help the CEO see the problem differently.</span></div>
        </div>
        """,
        """
        <div class="category-hero"><small>PROPOSED CATEGORY</small><h2>Intelligent Business Transformations</h2><p>SV engineers intelligent business systems for companies whose growth or scale has outgrown their current way of working.</p></div>
        <div class="stack-line"><span>Existing systems</span><span>Data & context</span><span>People & decisions</span><span>Automation</span><span>AI agents</span><span>Governance</span><b>→ intelligent workflow</b></div>
        <blockquote>Automate what machines should do. Augment what humans should own. Orchestrate everything in between.</blockquote>
        """,
        """
        <div class="story-ladder"><div>01 · Business pain</div><div>02 · Hidden system friction</div><div>03 · Value opportunity</div><div>04 · Intelligent workflow</div><div>05 · Human checkpoint</div><div>06 · Pilot</div><div>07 · Outcome</div><div>08 · Expansion</div></div>
        <div class="story-callout">Your business already has the systems. The problem is that the work still moves between them manually.</div>
        """,
        """
        <div class="timeline"><div><b>MONTH 1</b><strong>Make the category visible</strong><span>Website · POV · targeted outreach</span></div><div><b>MONTH 2</b><strong>Show the machinery</strong><span>Demos · before/after · system maps</span></div><div><b>MONTH 3</b><strong>Convert</strong><span>Account pages · assessment · pilot</span></div></div>
        <div class="content-loop"><span>Research insight</span><b>→</b><span>Executive post</span><b>→</b><span>System diagram</span><b>→</b><span>Video</span><b>→</b><span>Email</span><b>→</b><span>Proof story</span></div>
        """,
        """
        <div class="ia-visual"><strong>START WITH A PROBLEM</strong><div><span>Explore<small>Grow · Convert · Scale · Operate · Decide · Start</small></span><span>Industries<small>Manufacturing · Healthcare · Logistics · Services</small></span><span>Systems<small>Customer · Revenue · Operations · Supply · Finance</small></span><span>Proof<small>Transformations · Experiments · Before / After</small></span></div></div>
        <div class="md-flow"><span>What is changing?</span><span>What is in the way?</span><span>Leverage map</span><span>First experiment</span></div>
        """,
        """
        <div class="experience-grid"><div><b>01</b><strong>Find Your Leverage</strong><span>Intent · friction · systems · volume · judgement</span></div><div><b>02</b><strong>System Story</strong><span>Fragmented → orchestrated</span></div><div><b>03</b><strong>Executive Proof</strong><span>Baseline · intervention · human · outcome</span></div><div><b>04</b><strong>Pilot Builder</strong><span>Systems · data · agents · HITL · KPI</span></div></div>
        <div class="before-after"><span>CRM → email → spreadsheet → ERP → human chase</span><b>→</b><span>signal → context → reasoning → approved action → update → exception</span></div>
        """,
        """
        <div class="case-grid"><div><b>01</b><strong>Multi-country manufacturer</strong><span>CRM + SCM + ERP</span><em>OTIF · cycle time · exceptions</em></div><div><b>02</b><strong>Growth-constrained B2B</strong><span>Demand → conversion → expansion</span><em>Response · win rate · sales cycle</em></div><div><b>03</b><strong>Scale-constrained operations</strong><span>Expert workflow → supervised agents</span><em>Revenue/FTE · cost/transaction · cycle time</em></div></div>
        <div class="story-sequence"><span>Signal</span><span>Friction</span><span>Hidden cost</span><span>New system</span><span>Human role</span><span>Outcome</span><span>Expansion</span></div>
        """,
        """
        <div class="funnel-visual"><div><small>01</small><b>Discover</b></div><div><small>02</small><b>Qualify</b></div><div><small>03</small><b>Diagnose</b></div><div><small>04</small><b>Prove</b></div><div><small>05</small><b>Transform</b></div><div><small>06</small><b>Amplify</b></div><div><small>07</small><b>Learn</b></div></div>
        <div class="crm-strip">Profile · Value · Workflow · Sponsor · Urgency · AI maturity · Pilotability · Competitor · Next action</div>
        """,
        """
        <div class="loop-visual"><div><b>SEE</b><span>Signals</span></div><i>→</i><div><b>THINK</b><span>Context + constraints</span></div><i>→</i><div><b>ACT</b><span>Execute or recommend</span></div><i>→</i><div><b>AMPLIFY</b><span>Scale patterns</span></div><i>→</i><div><b>LEARN</b><span>Measure + improve</span></div></div>
        <div class="rule-card">A complete business system explains <strong>what it sees, how it reasons, what it can do, where a human decides and how it learns.</strong></div>
        """,
        """
        <div class="account-visual"><div class="account-core">ACCOUNT<br>INTELLIGENCE</div><div class="orbit orbit-1">Identity</div><div class="orbit orbit-2">Pressure</div><div class="orbit orbit-3">Business system</div><div class="orbit orbit-4">Intelligence</div><div class="orbit orbit-5">Opportunity</div><div class="orbit orbit-6">Buying system</div></div>
        <div class="state-strip">Unknown → Researched → Hypothesis → Engaged → Diagnosed → Pilot → Proven → Expanded</div>
        """
    ]
    return blocks[i]

def page_shell(current, title, summary, body, visual):
    idx = next((i for i,(href,_) in enumerate(PARTS) if href == current), -1)
    part = f"PART {idx+1:02d} / 16" if idx >= 0 else "SYSTEMS VALLEY STRATEGY"
    sequence = ""
    if idx >= 0:
        prev_href = "index.html" if idx == 0 else PARTS[idx-1][0]
        prev_label = "Overview" if idx == 0 else PARTS[idx-1][1]
        next_href = PARTS[idx+1][0] if idx < 15 else "index.html"
        next_label = PARTS[idx+1][1] if idx < 15 else "Overview"
        sequence = f'<div class="sequence-nav"><a href="{prev_href}">← {html.escape(prev_label)}</a><a href="{next_href}">{html.escape(next_label)} →</a></div>'
    return f'''<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} | Systems Valley Strategy</title><meta name="description" content="{html.escape(summary)}"><link rel="stylesheet" href="assets/style.css"></head><body><button class="mobile-nav-toggle" type="button" aria-label="Open navigation" aria-expanded="false"><span></span></button><div class="mobile-nav-backdrop"></div><div class="strategy-layout">{rail(current)}<main class="strategy-content"><div class="part-meta"><span>{part}</span><span>STRATEGY SYSTEM</span></div><section class="hero compact"><h1>{html.escape(title)}</h1><p>{html.escape(summary)}</p></section><section class="visual-section">{visual}</section><section class="evidence-section"><div class="evidence-label">FULL RESEARCH · RENDERED ON PAGE</div><div class="prose">{body}</div></section>{sequence}</main></div><footer class="footer">Research cut-off: 26 Sep 2026 · <a href="sources.html">Source register</a></footer><script>(function(){const b=document.querySelector(".mobile-nav-toggle"),n=document.querySelector(".strategy-rail"),o=document.querySelector(".mobile-nav-backdrop");if(!b||!n||!o)return;function t(x){n.classList.toggle("open",x);o.classList.toggle("open",x);b.setAttribute("aria-expanded",x);b.setAttribute("aria-label",x?"Close navigation":"Open navigation");document.body.classList.toggle("nav-open",x)}b.addEventListener("click",()=>t(!n.classList.contains("open")));o.addEventListener("click",()=>t(false));n.querySelectorAll("a").forEach(a=>a.addEventListener("click",()=>t(false)));window.addEventListener("keydown",e=>{if(e.key==="Escape")t(false)});})();</script><script>(function(){const b=document.querySelector(".mobile-nav-toggle"),n=document.querySelector(".strategy-rail"),o=document.querySelector(".mobile-nav-backdrop");if(!b||!n||!o)return;function t(x){n.classList.toggle("open",x);o.classList.toggle("open",x);b.setAttribute("aria-expanded",x);b.setAttribute("aria-label",x?"Close navigation":"Open navigation");document.body.classList.toggle("nav-open",x)}b.addEventListener("click",()=>t(!n.classList.contains("open")));o.addEventListener("click",()=>t(false));n.querySelectorAll("a").forEach(a=>a.addEventListener("click",()=>t(false)));window.addEventListener("keydown",e=>{if(e.key==="Escape")t(false)});})();</script></body></html>'''

def build_research_pages():
    for md in sorted(RESEARCH.glob("*.md")):
        if md.name in {"README.md","sources.md"}:
            continue
        current = md.stem + ".html"
        match = next((x for x in PARTS if x[0] == current), None)
        if not match:
            continue
        source = md.read_text(encoding="utf-8")
        body = markdown_to_html(source)
        idx = PARTS.index(match)
        SITE.joinpath(current).write_text(
            page_shell(current, match[1], SUMMARIES[idx], body, visual_intro(idx)),
            encoding="utf-8"
        )

def utility_page(filename, title, summary, body):
    SITE.joinpath(filename).write_text(
        page_shell(filename, title, summary, markdown_to_html(body), '<div class="utility-hero"><span>RESOURCE</span><h2>Use the strategy system, not a hidden file.</h2><p>This page is part of the same persistent navigation and evidence surface.</p></div>'),
        encoding="utf-8"
    )

def build_utilities():
    utility_page(
        "sources.html",
        "Source Register",
        "Evidence-backed market, AI adoption, services and competitor sources used by the strategy system.",
        """# Evidence register
Gartner, OECD, Deloitte, PwC, McKinsey, IDC, NITI Aayog, Eurostat, EU, MeitY, SEC and public Crunchbase reporting are registered in the research layer.

The detailed source register remains maintained in the research repository, while the strategic pages now render their substantive evidence directly on-page."""
    )
    utility_page(
        "accounts.html",
        "Target Account Explorer",
        "A public-hypothesis target-account set for qualification across US, EMEA and APAC.",
        """# Account model
The account model prioritizes complex operators, growth-constrained businesses and transformation-ready enterprises.

This is a public strategy hypothesis set, not a claimed private ZoomInfo database.

**Account state:** Unknown → Researched → Hypothesis → Engaged → Diagnosed → Pilot → Proven → Expanded."""
    )
    utility_page(
        "competitors.html",
        "Competitor Explorer",
        "A comparative view of the narratives shaping the AI-native services market.",
        """# Competitive frame
Thoughtworks, EPAM, Globant, Cognizant, Searce, Publicis Sapient, Quantiphi, BCG/BCG X, Accenture and Genpact are benchmarked against Systems Valley's intelligent business systems whitespace.

The detailed competitive evidence is rendered directly in Part 06."""
    )

def build():
    SITE.mkdir(parents=True, exist_ok=True)
    build_research_pages()
    build_utilities()

if __name__ == "__main__":
    build()
