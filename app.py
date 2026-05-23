import streamlit as st

st.set_page_config(
    page_title="Aakash Kumar | Engineering Portfolio",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Basic Data
# -----------------------------
PROFILE = {
    "name": "Aakash Kumar",
    "title": "Senior Platform & DevSecOps Engineer",
    "tagline": "Building scalable automation platforms, cloud infrastructure systems, and enterprise remediation orchestration solutions.",
    "email": "akgaya99@gmail.com",
    "location": "Pune, India | Open to Bangalore & Dubai",
    "target_roles": ["DevSecOps Engineer", "Platform Engineer", "Cloud Engineer"],
    "expected_ctc": "₹45 LPA",
}

SKILLS = [
    "DevSecOps", "Platform Engineering", "CI/CD", "Cloud Automation",
    "Infrastructure Automation", "Vulnerability Management", "AWS Services",
    "Jenkins", "Python", "Terraform", "Ansible", "Linux", "RESTful APIs",
    "API Integration", "Automation Engineering", "Bitbucket", "Artifactory", "Git", "Bash", "Jira"
]

METRICS = [
    ("6+", "Years Experience"),
    ("100K+", "Deployments Supported"),
    ("70%", "Operational Effort Reduced"),
    ("45 LPA", "Target CTC"),
]

PROJECTS = [
    {
        "title": "Enterprise Vulnerability Remediation Platform",
        "category": "DevSecOps / Platform Engineering",
        "description": "A centralized remediation orchestration platform concept for regulated enterprise environments, focused on automation governance, vulnerability workflow tracking, CI/CD integration, and operational visibility.",
        "stack": ["Python", "Jenkins", "AWS", "REST APIs", "DevSecOps", "Automation"]
    },
    {
        "title": "Enterprise CI/CD Automation Framework",
        "category": "Release Engineering",
        "description": "Automation framework supporting large-scale deployment ecosystems with standardized release workflows, governance checkpoints, and reduced senior operational dependency.",
        "stack": ["Jenkins", "Terraform", "AWS", "Linux", "Shell", "Bitbucket"]
    },
    {
        "title": "Trading Automation Systems",
        "category": "FinTech Automation",
        "description": "Built real-time automated trading systems using WebSocket data, broker APIs, and strategy-based execution logic for market automation experiments.",
        "stack": ["Python", "WebSocket", "Dhan API", "MQL5", "REST APIs"]
    },
]

ARCHITECTURE_FLOW = """
flowchart LR
    A[Security / Infra Signal] --> B[Central Remediation Platform]
    B --> C[Policy & Governance Engine]
    B --> D[CI/CD Orchestration]
    B --> E[Automation Workers]
    E --> F[AWS / Linux / Infra Targets]
    D --> G[Jenkins Pipelines]
    C --> H[Audit & Reporting]
    F --> H
    G --> H
"""

# -----------------------------
# Styling
# -----------------------------
st.markdown("""
<style>
    .main {
        background-color: #0f172a;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .hero-card {
        padding: 2rem;
        border-radius: 24px;
        background: linear-gradient(135deg, #111827 0%, #1e293b 60%, #0f172a 100%);
        border: 1px solid rgba(148, 163, 184, 0.25);
        box-shadow: 0 20px 50px rgba(0,0,0,0.25);
    }
    .section-card {
        padding: 1.4rem;
        border-radius: 18px;
        background: #111827;
        border: 1px solid rgba(148, 163, 184, 0.18);
        height: 100%;
    }
    .metric-card {
        padding: 1.2rem;
        border-radius: 18px;
        background: #020617;
        border: 1px solid rgba(59, 130, 246, 0.35);
        text-align: center;
    }
    .metric-number {
        font-size: 2rem;
        font-weight: 800;
        color: #38bdf8;
    }
    .metric-label {
        color: #cbd5e1;
        font-size: 0.9rem;
    }
    .tag {
        display: inline-block;
        padding: 0.35rem 0.7rem;
        margin: 0.25rem;
        border-radius: 999px;
        background: rgba(59,130,246,0.14);
        border: 1px solid rgba(96,165,250,0.35);
        color: #dbeafe;
        font-size: 0.85rem;
    }
    .muted {
        color: #94a3b8;
    }
    h1, h2, h3, p, li, span, div {
        color: #e5e7eb;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Aakash Kumar")
st.sidebar.caption("Senior Platform & DevSecOps Engineer")

page = st.sidebar.radio(
    "Navigate",
    ["Overview", "Capabilities", "Architecture", "Projects", "Resume Snapshot", "Contact"]
)

st.sidebar.divider()
st.sidebar.write("**Target Roles**")
for role in PROFILE["target_roles"]:
    st.sidebar.write(f"• {role}")

st.sidebar.divider()
st.sidebar.write(f"**Expected CTC:** {PROFILE['expected_ctc']}")
st.sidebar.write(f"**Location:** {PROFILE['location']}")

# -----------------------------
# Reusable Components
# -----------------------------
def skill_tags(skills):
    html = "".join([f"<span class='tag'>{skill}</span>" for skill in skills])
    st.markdown(html, unsafe_allow_html=True)


def metric_grid():
    cols = st.columns(4)
    for col, (number, label) in zip(cols, METRICS):
        with col:
            st.markdown(
                f"""
                <div class='metric-card'>
                    <div class='metric-number'>{number}</div>
                    <div class='metric-label'>{label}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

# -----------------------------
# Pages
# -----------------------------
if page == "Overview":
    st.markdown(
        f"""
        <div class='hero-card'>
            <h1>{PROFILE['name']}</h1>
            <h2>{PROFILE['title']}</h2>
            <p class='muted'>{PROFILE['tagline']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    metric_grid()

    st.write("")
    st.subheader("Profile Summary")
    st.write(
        "Senior Platform & DevSecOps Engineer with 6+ years of experience designing and scaling "
        "enterprise automation platforms within large banking and financial services environments. "
        "Specialized in CI/CD automation, cloud infrastructure, vulnerability remediation, platform engineering, "
        "and policy-driven operational automation that transforms manual processes into scalable self-service systems."
    )

    st.subheader("Core Technology Stack")
    skill_tags(SKILLS)

elif page == "Capabilities":
    st.title("Engineering Capabilities")
    capabilities = [
        ("DevSecOps Engineering", "Security remediation workflows, governance automation, and vulnerability lifecycle orchestration."),
        ("Platform Engineering", "Self-service engineering platforms, reusable automation layers, and enterprise operational tooling."),
        ("CI/CD Automation", "Jenkins-driven deployment orchestration, release governance, and standardized delivery workflows."),
        ("Cloud Automation", "AWS-based infrastructure automation, environment provisioning, and operational reliability workflows."),
        ("Infrastructure Automation", "Terraform, Ansible, Linux, scripting, and API-first automation across enterprise systems."),
        ("Engineering Leadership", "Ownership mindset, product-style platform thinking, and cross-functional execution in regulated environments."),
    ]

    cols = st.columns(2)
    for index, (title, desc) in enumerate(capabilities):
        with cols[index % 2]:
            st.markdown(
                f"""
                <div class='section-card'>
                    <h3>{title}</h3>
                    <p class='muted'>{desc}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.write("")

elif page == "Architecture":
    st.title("Architecture Showcase")
    st.write("A reference architecture for an enterprise remediation and automation platform.")

    try:
        st.graphviz_chart("""
            digraph {
                rankdir=LR;
                node [shape=box, style="rounded,filled", fillcolor="#111827", fontcolor="#e5e7eb", color="#38bdf8"];
                edge [color="#94a3b8"];
                Signal [label="Security / Infra Signal"];
                Platform [label="Central Remediation Platform"];
                Governance [label="Policy & Governance Engine"];
                CICD [label="CI/CD Orchestration"];
                Workers [label="Automation Workers"];
                Infra [label="AWS / Linux / Infra Targets"];
                Jenkins [label="Jenkins Pipelines"];
                Reporting [label="Audit & Reporting"];
                Signal -> Platform;
                Platform -> Governance;
                Platform -> CICD;
                Platform -> Workers;
                Workers -> Infra;
                CICD -> Jenkins;
                Governance -> Reporting;
                Infra -> Reporting;
                Jenkins -> Reporting;
            }
        """)
    except Exception:
        st.code(ARCHITECTURE_FLOW, language="mermaid")

    st.subheader("Platform Thinking")
    st.write(
        "The architecture is designed around centralized control, automation workers, governed execution, "
        "CI/CD integration, and audit-ready reporting. This reflects enterprise banking-grade engineering "
        "where automation is treated as a long-lived platform, not a loose set of scripts."
    )

elif page == "Projects":
    st.title("Project Showcase")
    for project in PROJECTS:
        st.markdown(
            f"""
            <div class='section-card'>
                <h3>{project['title']}</h3>
                <p><b>{project['category']}</b></p>
                <p class='muted'>{project['description']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        skill_tags(project["stack"])
        st.write("")

elif page == "Resume Snapshot":
    st.title("Resume Snapshot")

    st.subheader("Preferred Roles")
    for role in PROFILE["target_roles"]:
        st.write(f"• {role}")

    st.subheader("Preferred Companies")
    companies = ["JP Morgan Chase", "Goldman Sachs", "Morgan Stanley", "Deutsche Bank", "Mastercard", "Fidelity Investments"]
    for company in companies:
        st.write(f"• {company}")

    st.subheader("Preferred Industries")
    industries = ["Banking / Financial Services", "Software Product", "IT Services & Consulting", "FinTech"]
    for industry in industries:
        st.write(f"• {industry}")

    st.subheader("Profile Summary")
    st.info(
        "Senior Platform & DevSecOps Engineer with 6+ years of experience designing and scaling enterprise automation platforms within large banking and financial services environments. Specialized in CI/CD automation, cloud infrastructure, platform engineering, vulnerability remediation, and policy-driven operational automation."
    )

elif page == "Contact":
    st.title("Contact")
    st.write(f"**Email:** {PROFILE['email']}")
    st.write(f"**Location:** {PROFILE['location']}")
    st.write("**Open For:** Senior IC roles in DevSecOps, Platform Engineering, Cloud Engineering, and Automation Engineering.")

    st.divider()
    st.subheader("Recruiter Note")
    st.write(
        "I am exploring senior individual contributor roles focused on enterprise DevSecOps, platform engineering, "
        "cloud automation, CI/CD orchestration, and infrastructure automation across banking, fintech, and product engineering organizations."
    )
