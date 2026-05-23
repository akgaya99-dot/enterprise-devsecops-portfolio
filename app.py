import streamlit as st

st.set_page_config(
    page_title="Aakash Kumar | Enterprise Engineering Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ======================================================
# DATA CONFIG
# ======================================================
PROFILE = {
    "name": "Aakash Kumar",
    "role": "Senior Platform & DevSecOps Engineer",
    "positioning": "Enterprise Automation • DevSecOps • Cloud Platform Engineering",
    "location": "Pune, India | Open to Bangalore & Dubai",
    "email": "akgaya99@gmail.com",
    "summary": (
        "Senior Platform & DevSecOps Engineer with 6+ years of experience designing and scaling "
        "enterprise automation platforms within banking and financial services environments. Specialized in "
        "CI/CD automation, vulnerability remediation, cloud infrastructure, platform engineering, and "
        "policy-driven operational automation."
    ),
    "cta": "Open for senior IC roles in DevSecOps, Platform Engineering, Cloud Engineering, and Automation Engineering.",
}

METRICS = [
    {"value": "6+", "label": "Years Experience", "detail": "Enterprise banking environments"},
    {"value": "100K+", "label": "Deployments Supported", "detail": "Large-scale application ecosystems"},
    {"value": "70%", "label": "Effort Reduction", "detail": "Automation-led operational efficiency"},
    {"value": "45 LPA", "label": "Target CTC", "detail": "Senior IC / specialist roles"},
]

CAPABILITIES = [
    {
        "title": "DevSecOps Engineering",
        "icon": "🛡️",
        "desc": "Vulnerability remediation workflows, governance controls, audit-ready automation, and security lifecycle orchestration.",
    },
    {
        "title": "Platform Engineering",
        "icon": "⚙️",
        "desc": "Internal developer platforms, self-service workflows, reusable automation layers, and operational product ownership.",
    },
    {
        "title": "CI/CD Automation",
        "icon": "🚀",
        "desc": "Jenkins-led delivery automation, release governance, environment orchestration, and deployment lifecycle optimization.",
    },
    {
        "title": "Cloud Automation",
        "icon": "☁️",
        "desc": "AWS-based infrastructure automation, provisioning workflows, API integration, and cloud operational reliability.",
    },
    {
        "title": "Infrastructure Automation",
        "icon": "🏗️",
        "desc": "Terraform, Ansible, Linux, Bash, REST APIs, and automation-first infrastructure engineering practices.",
    },
    {
        "title": "Enterprise Governance",
        "icon": "📊",
        "desc": "Controls, reporting, audit visibility, release discipline, and regulated-environment execution models.",
    },
]

SKILLS = [
    "DevSecOps", "Platform Engineering", "CI/CD", "Cloud Automation", "Infrastructure Automation",
    "Vulnerability Management", "AWS Services", "Jenkins", "Python", "Terraform", "Ansible", "Linux",
    "RESTful APIs", "API Integration", "Automation Engineering", "Bitbucket", "Artifactory", "Git", "Bash", "Jira"
]

PROJECTS = [
    {
        "title": "Enterprise Vulnerability Remediation Platform",
        "label": "DevSecOps Platform",
        "impact": "Centralized remediation orchestration for regulated enterprise environments.",
        "desc": "Designed platform concepts for vulnerability workflow tracking, policy-based remediation, CI/CD integration, automation workers, and audit visibility without exposing proprietary implementation details.",
        "stack": ["Python", "Jenkins", "AWS", "REST APIs", "DevSecOps", "Automation"],
    },
    {
        "title": "Enterprise CI/CD Automation Framework",
        "label": "Release Engineering",
        "impact": "Standardized and scaled deployment operations across large application ecosystems.",
        "desc": "Built automation-first delivery workflows with governance checkpoints, deployment orchestration, environment handling, and reduced senior operational dependency.",
        "stack": ["Jenkins", "Terraform", "AWS", "Linux", "Shell", "Bitbucket"],
    },
    {
        "title": "Trading Automation Systems",
        "label": "FinTech Automation",
        "impact": "Real-time strategy execution using broker APIs and market data streams.",
        "desc": "Created automated trading systems using WebSocket feeds, REST APIs, strategy logic, risk controls, and execution workflows for market automation experiments.",
        "stack": ["Python", "WebSocket", "Dhan API", "MQL5", "REST APIs"],
    },
]

TIMELINE = [
    ("Platform Ownership", "Moved automation from script-based execution to long-lived platform ownership models."),
    ("Enterprise Scale", "Supported large-scale deployment operations and multi-team engineering workflows."),
    ("DevSecOps Expansion", "Focused on remediation orchestration, governance, and security automation."),
    ("Cloud Automation", "Built AWS, CI/CD, infrastructure, and API-driven automation capabilities."),
]

# ======================================================
# DESIGN SYSTEM
# ======================================================
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        .stApp {
            background:
                radial-gradient(circle at 15% 10%, rgba(37, 99, 235, 0.28), transparent 28%),
                radial-gradient(circle at 85% 15%, rgba(14, 165, 233, 0.18), transparent 26%),
                radial-gradient(circle at 50% 90%, rgba(99, 102, 241, 0.16), transparent 26%),
                #020617;
            color: #e5e7eb;
        }

        section[data-testid="stSidebar"] {
            background: rgba(2, 6, 23, 0.92);
            border-right: 1px solid rgba(148, 163, 184, 0.18);
        }

        .block-container {
            padding-top: 1.6rem;
            padding-bottom: 3rem;
            max-width: 1320px;
        }

        h1, h2, h3, h4, h5, h6, p, li, span, div {
            color: #e5e7eb;
        }

        .hero {
            position: relative;
            overflow: hidden;
            padding: 3rem;
            border-radius: 34px;
            background:
                linear-gradient(135deg, rgba(15, 23, 42, 0.96), rgba(15, 23, 42, 0.72)),
                linear-gradient(90deg, rgba(37, 99, 235, 0.28), rgba(14, 165, 233, 0.12));
            border: 1px solid rgba(148, 163, 184, 0.22);
            box-shadow: 0 32px 90px rgba(0, 0, 0, 0.42);
        }

        .hero:before {
            content: "";
            position: absolute;
            inset: -2px;
            background: radial-gradient(circle at 70% 20%, rgba(56, 189, 248, 0.22), transparent 25%);
            pointer-events: none;
        }

        .kicker {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 8px 14px;
            border-radius: 999px;
            color: #bae6fd;
            background: rgba(14, 165, 233, 0.12);
            border: 1px solid rgba(125, 211, 252, 0.28);
            font-size: 0.88rem;
            font-weight: 700;
            letter-spacing: 0.02em;
        }

        .hero-title {
            margin-top: 1.1rem;
            font-size: clamp(2.4rem, 5vw, 5rem);
            line-height: 0.95;
            font-weight: 900;
            letter-spacing: -0.06em;
            color: #f8fafc;
        }

        .hero-role {
            font-size: clamp(1.15rem, 2vw, 1.8rem);
            color: #38bdf8;
            font-weight: 800;
            margin-top: 0.8rem;
        }

        .hero-text {
            max-width: 880px;
            color: #cbd5e1;
            font-size: 1.06rem;
            line-height: 1.75;
            margin-top: 1rem;
        }

        .pill-row {
            margin-top: 1.4rem;
        }

        .pill {
            display: inline-block;
            padding: 0.5rem 0.82rem;
            margin: 0.24rem;
            border-radius: 999px;
            background: rgba(15, 23, 42, 0.9);
            border: 1px solid rgba(148, 163, 184, 0.25);
            color: #e0f2fe;
            font-size: 0.88rem;
            font-weight: 600;
        }

        .metric-card {
            padding: 1.35rem;
            border-radius: 24px;
            background: linear-gradient(180deg, rgba(15,23,42,0.98), rgba(2,6,23,0.95));
            border: 1px solid rgba(148, 163, 184, 0.18);
            box-shadow: 0 20px 50px rgba(0,0,0,0.22);
            min-height: 160px;
        }

        .metric-value {
            font-size: 2.25rem;
            font-weight: 900;
            color: #38bdf8;
            letter-spacing: -0.04em;
        }

        .metric-label {
            font-size: 1rem;
            font-weight: 800;
            color: #f8fafc;
            margin-top: 0.35rem;
        }

        .metric-detail {
            font-size: 0.86rem;
            color: #94a3b8;
            margin-top: 0.4rem;
            line-height: 1.5;
        }

        .section-title {
            margin-top: 2.4rem;
            margin-bottom: 0.9rem;
            font-size: 1.8rem;
            font-weight: 900;
            letter-spacing: -0.04em;
            color: #f8fafc;
        }

        .section-subtitle {
            color: #94a3b8;
            font-size: 1rem;
            margin-bottom: 1.2rem;
            max-width: 860px;
        }

        .glass-card {
            padding: 1.45rem;
            border-radius: 24px;
            background: rgba(15, 23, 42, 0.78);
            border: 1px solid rgba(148, 163, 184, 0.18);
            box-shadow: 0 20px 60px rgba(0,0,0,0.25);
            backdrop-filter: blur(16px);
            height: 100%;
        }

        .cap-icon {
            font-size: 1.8rem;
            margin-bottom: 0.7rem;
        }

        .card-title {
            font-size: 1.1rem;
            font-weight: 850;
            color: #f8fafc;
            margin-bottom: 0.45rem;
        }

        .card-text {
            color: #aebdd0;
            line-height: 1.62;
            font-size: 0.94rem;
        }

        .project-card {
            padding: 1.6rem;
            border-radius: 28px;
            background:
                linear-gradient(135deg, rgba(15, 23, 42, 0.96), rgba(30, 41, 59, 0.72));
            border: 1px solid rgba(148, 163, 184, 0.2);
            box-shadow: 0 24px 70px rgba(0,0,0,0.24);
            margin-bottom: 1rem;
        }

        .project-label {
            display: inline-block;
            padding: 0.35rem 0.7rem;
            border-radius: 999px;
            background: rgba(37, 99, 235, 0.18);
            border: 1px solid rgba(96, 165, 250, 0.28);
            color: #bfdbfe;
            font-size: 0.78rem;
            font-weight: 800;
        }

        .project-title {
            margin-top: 0.8rem;
            font-size: 1.35rem;
            font-weight: 900;
            color: #f8fafc;
        }

        .project-impact {
            margin-top: 0.35rem;
            color: #7dd3fc;
            font-weight: 700;
        }

        .timeline-item {
            border-left: 2px solid rgba(56, 189, 248, 0.55);
            padding-left: 1rem;
            padding-bottom: 1.2rem;
            margin-left: 0.4rem;
        }

        .timeline-title {
            font-weight: 850;
            color: #f8fafc;
        }

        .timeline-desc {
            color: #94a3b8;
            line-height: 1.55;
        }

        .notice {
            padding: 1.25rem 1.4rem;
            border-radius: 22px;
            background: rgba(8, 47, 73, 0.5);
            border: 1px solid rgba(14, 165, 233, 0.3);
            color: #dbeafe;
            line-height: 1.65;
        }

        .footer-card {
            padding: 1.5rem;
            border-radius: 24px;
            background: rgba(2, 6, 23, 0.8);
            border: 1px solid rgba(148, 163, 184, 0.18);
            margin-top: 2rem;
        }

        div[data-testid="stRadio"] label p {
            font-weight: 700;
            color: #cbd5e1;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ======================================================
# HELPERS
# ======================================================
def render_pills(items):
    html = "<div class='pill-row'>" + "".join([f"<span class='pill'>{item}</span>" for item in items]) + "</div>"
    st.markdown(html, unsafe_allow_html=True)


def render_metrics():
    cols = st.columns(4)
    for col, item in zip(cols, METRICS):
        with col:
            st.markdown(
                f"""
                <div class='metric-card'>
                    <div class='metric-value'>{item['value']}</div>
                    <div class='metric-label'>{item['label']}</div>
                    <div class='metric-detail'>{item['detail']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_section_header(title, subtitle):
    st.markdown(f"<div class='section-title'>{title}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='section-subtitle'>{subtitle}</div>", unsafe_allow_html=True)

# ======================================================
# SIDEBAR
# ======================================================
st.sidebar.markdown("### ⚡ Aakash Kumar")
st.sidebar.caption("Enterprise Engineering Portfolio")

page = st.sidebar.radio(
    "Navigation",
    ["Command Center", "Capabilities", "Architecture", "Projects", "Resume Snapshot", "Contact"],
)

st.sidebar.divider()
st.sidebar.markdown("**Target Roles**")
st.sidebar.write("• DevSecOps Engineer")
st.sidebar.write("• Platform Engineer")
st.sidebar.write("• Cloud Engineer")

st.sidebar.divider()
st.sidebar.markdown("**Core Stack**")
st.sidebar.write("AWS • Jenkins • Python • Terraform")
st.sidebar.write("CI/CD • Linux • APIs • Automation")

st.sidebar.divider()
st.sidebar.markdown("**Location**")
st.sidebar.write(PROFILE["location"])

# ======================================================
# PAGES
# ======================================================
if page == "Command Center":
    st.markdown(
        f"""
        <div class='hero'>
            <div class='kicker'>⚡ {PROFILE['positioning']}</div>
            <div class='hero-title'>{PROFILE['name']}</div>
            <div class='hero-role'>{PROFILE['role']}</div>
            <div class='hero-text'>{PROFILE['summary']}</div>
            <div class='pill-row'>
                <span class='pill'>DevSecOps</span>
                <span class='pill'>Platform Engineering</span>
                <span class='pill'>Cloud Automation</span>
                <span class='pill'>CI/CD Orchestration</span>
                <span class='pill'>Vulnerability Remediation</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    render_metrics()

    render_section_header(
        "Executive Positioning",
        "Designed for recruiters and engineering leaders to understand senior IC capability in under 60 seconds.",
    )

    col1, col2 = st.columns([1.25, 0.75])
    with col1:
        st.markdown(
            """
            <div class='glass-card'>
                <div class='card-title'>Engineering Identity</div>
                <div class='card-text'>
                    I operate at the intersection of DevSecOps, platform engineering, cloud automation, and enterprise governance.
                    My core strength is converting manual operational processes into self-service, policy-driven automation platforms
                    that scale across teams, tools, and regulated environments.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class='glass-card'>
                <div class='card-title'>Best Fit</div>
                <div class='card-text'>
                    Senior IC roles in banking, fintech, GCCs, cloud infrastructure, DevSecOps, CI/CD platforms,
                    internal developer platforms, and automation engineering.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    render_section_header("Technology Stack", "Recruiter-searchable and aligned with senior platform engineering roles.")
    render_pills(SKILLS)

elif page == "Capabilities":
    render_section_header(
        "Engineering Capabilities",
        "A capability map showing how enterprise automation, security, cloud, and platform ownership connect.",
    )

    cols = st.columns(3)
    for idx, item in enumerate(CAPABILITIES):
        with cols[idx % 3]:
            st.markdown(
                f"""
                <div class='glass-card'>
                    <div class='cap-icon'>{item['icon']}</div>
                    <div class='card-title'>{item['title']}</div>
                    <div class='card-text'>{item['desc']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.write("")

    render_section_header("Career Evolution", "How the profile has matured from execution to platform ownership.")
    for title, desc in TIMELINE:
        st.markdown(
            f"""
            <div class='timeline-item'>
                <div class='timeline-title'>{title}</div>
                <div class='timeline-desc'>{desc}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

elif page == "Architecture":
    render_section_header(
        "Architecture Showcase",
        "Reference architecture for an enterprise remediation and automation platform. This intentionally avoids proprietary implementation details.",
    )

    st.graphviz_chart(
        """
        digraph {
            graph [bgcolor="transparent", rankdir=LR, splines=ortho];
            node [shape=box, style="rounded,filled", fillcolor="#0f172a", fontcolor="#e5e7eb", color="#38bdf8", penwidth=1.5, fontname="Inter"];
            edge [color="#7dd3fc", penwidth=1.4, fontname="Inter", fontcolor="#cbd5e1"];

            Signal [label="Security / Infra Signal"];
            Platform [label="Central Remediation Platform"];
            Governance [label="Policy & Governance Engine"];
            CICD [label="CI/CD Orchestration"];
            Workers [label="Automation Workers"];
            Infra [label="AWS / Linux / Infra Targets"];
            Jenkins [label="Jenkins Pipelines"];
            Reporting [label="Audit & Reporting"];
            Users [label="Engineering / Security Teams"];

            Signal -> Platform;
            Users -> Platform;
            Platform -> Governance;
            Platform -> CICD;
            Platform -> Workers;
            Workers -> Infra;
            CICD -> Jenkins;
            Governance -> Reporting;
            Infra -> Reporting;
            Jenkins -> Reporting;
        }
        """
    )

    col1, col2, col3 = st.columns(3)
    architecture_points = [
        ("Control Plane", "Centralized orchestration for remediation requests, governance, and workflow visibility."),
        ("Execution Layer", "Automation workers and CI/CD systems execute approved operational actions."),
        ("Audit Layer", "Reporting, evidence capture, operational traceability, and governance-ready outputs."),
    ]
    for col, (title, desc) in zip([col1, col2, col3], architecture_points):
        with col:
            st.markdown(
                f"""
                <div class='glass-card'>
                    <div class='card-title'>{title}</div>
                    <div class='card-text'>{desc}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

elif page == "Projects":
    render_section_header(
        "Project Showcase",
        "Portfolio-safe project storytelling focused on capability, architecture, and impact — not proprietary source code.",
    )

    for project in PROJECTS:
        st.markdown(
            f"""
            <div class='project-card'>
                <span class='project-label'>{project['label']}</span>
                <div class='project-title'>{project['title']}</div>
                <div class='project-impact'>{project['impact']}</div>
                <div class='card-text' style='margin-top: 0.7rem;'>{project['desc']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        render_pills(project["stack"])
        st.write("")

elif page == "Resume Snapshot":
    render_section_header(
        "Resume Snapshot",
        "A recruiter-friendly summary of target roles, companies, industries, and positioning.",
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            <div class='glass-card'>
                <div class='card-title'>Preferred Roles</div>
                <div class='card-text'>
                    • DevSecOps Engineer<br>
                    • Platform Engineer<br>
                    • Cloud Engineer
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("")
        st.markdown(
            """
            <div class='glass-card'>
                <div class='card-title'>Preferred Industries</div>
                <div class='card-text'>
                    • Banking / Financial Services<br>
                    • Software Product<br>
                    • IT Services & Consulting<br>
                    • FinTech
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class='glass-card'>
                <div class='card-title'>Preferred Companies</div>
                <div class='card-text'>
                    • JP Morgan Chase<br>
                    • Goldman Sachs<br>
                    • Morgan Stanley<br>
                    • Deutsche Bank<br>
                    • Mastercard<br>
                    • Fidelity Investments
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("")
        st.markdown(
            """
            <div class='glass-card'>
                <div class='card-title'>Compensation Positioning</div>
                <div class='card-text'>
                    Current senior enterprise engineering profile positioned for ₹45 LPA target roles in senior IC, platform,
                    DevSecOps, and cloud automation tracks.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    render_section_header("Profile Summary", "Compact summary suitable for Naukri, LinkedIn, and recruiter screening.")
    st.markdown(f"<div class='notice'>{PROFILE['summary']}</div>", unsafe_allow_html=True)

elif page == "Contact":
    render_section_header("Contact", "For senior engineering, platform, DevSecOps, and cloud automation opportunities.")

    col1, col2 = st.columns([0.8, 1.2])
    with col1:
        st.markdown(
            f"""
            <div class='glass-card'>
                <div class='card-title'>Aakash Kumar</div>
                <div class='card-text'>
                    {PROFILE['role']}<br><br>
                    📍 {PROFILE['location']}<br>
                    ✉️ {PROFILE['email']}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            f"""
            <div class='glass-card'>
                <div class='card-title'>Recruiter Note</div>
                <div class='card-text'>
                    {PROFILE['cta']} Strong fit for organizations building secure automation platforms,
                    internal developer platforms, CI/CD systems, cloud infrastructure automation, and enterprise remediation workflows.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown(
    """
    <div class='footer-card'>
        <div class='card-text'>
            Built as a portfolio-safe engineering showcase. The content demonstrates architecture thinking, capability depth,
            and platform ownership without disclosing proprietary company code or confidential implementation details.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
