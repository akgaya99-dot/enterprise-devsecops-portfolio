import streamlit as st

st.set_page_config(
    page_title="Aakash Kumar | Platform Engineering Command Center",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

PROFILE = {
    "name": "Aakash Kumar",
    "initials": "AK",
    "role": "Senior Platform & DevSecOps Engineer",
    "subheadline": "Cloud Automation • CI/CD • Infrastructure • Governance • Remediation",
    "email": "akgaya99@gmail.com",
    "location": "Pune, India | Open to Bangalore & Dubai",
    "url": "aakash-platform-engineering.streamlit.app",
}

CAPABILITY_RAIL = [
    ("🛡️", "DevSecOps", "Secure, automated and compliant delivery pipelines"),
    ("🧊", "Platform Engineering", "Scalable platforms and self-service automation"),
    ("⚙️", "CI/CD Automation", "End-to-end build, test and deploy automation"),
    ("☁️", "Cloud Infrastructure", "AWS cloud automation and infrastructure design"),
    ("💻", "Infrastructure as Code", "Terraform, Ansible, and automated infrastructure provisioning"),
    ("🔐", "Enterprise Governance", "Policy-as-code, compliance and governance at scale"),
    ("🎯", "Remediation Automation", "Vulnerability remediation and operational automation"),
    ("📈", "Monitoring & Observability", "Observability, logging and alerting at enterprise scale"),
]

NAV_ITEMS = ["Overview", "About Me", "Capabilities", "Experience", "Architecture", "Projects", "Technologies", "Achievements", "Contact"]

METRICS = [
    ("🚀", "100K+", "Deployment Operations", "Supported"),
    ("📈", "70%", "Reduction in", "Operational Effort"),
    ("🏢", "Enterprise", "Scale", "Automation Platform Ownership"),
    ("👥", "Multi-Team", "Enablement", "Cross-functional Collaboration"),
    ("🛡️", "High", "Reliability", "Secure & Compliant Delivery"),
]

PIPELINE = [("💻", "Code"), ("⚙️", "Build"), ("🧪", "Test"), ("🛡️", "Security Scan"), ("🚀", "Deploy"), ("📡", "Monitor")]
REMEDIATION = [("🔎", "Detect"), ("📊", "Prioritize"), ("🛠️", "Remediate"), ("✅", "Validate"), ("📄", "Report")]

BOTTOM_CARDS = [
    ("☁️", "CLOUD & INFRASTRUCTURE", "AWS, Terraform, Ansible, Linux and scalable infrastructure automation."),
    ("🔒", "SECURE BY DESIGN", "DevSecOps practices, policy controls, security scanning and compliance embedded in pipelines."),
    ("⚙️", "AUTOMATION FIRST", "Eliminating manual work through reusable automation and engineering frameworks."),
    ("🎯", "BUSINESS IMPACT", "Driving operational excellence, improving reliability and delivering measurable outcomes."),
]

TECH_STACK = [
    "DevSecOps", "Platform Engineering", "AWS", "Jenkins", "Python", "Terraform", "Ansible", "Linux",
    "REST APIs", "CI/CD", "Cloud Automation", "Infrastructure Automation", "Bitbucket", "Artifactory", "Git", "Jira"
]

PROJECTS = [
    ("DevSecOps Platform", "Enterprise Vulnerability Remediation Platform", "Centralized remediation orchestration for regulated enterprise environments with workflow tracking, governance checkpoints, CI/CD integration, automation workers and audit visibility."),
    ("Release Engineering", "Enterprise CI/CD Automation Framework", "Standardized deployment operations across large application ecosystems using Jenkins-led orchestration, policy controls, infrastructure automation and operational reliability practices."),
    ("FinTech Automation", "Trading Automation Systems", "Real-time automation systems using WebSocket market data, broker APIs, strategy logic and execution workflow design for market automation experiments."),
]

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
*{font-family:Inter,sans-serif;box-sizing:border-box} .stApp{background:radial-gradient(circle at 50% -8%,rgba(59,130,246,.30),transparent 30%),radial-gradient(circle at 12% 28%,rgba(14,165,233,.13),transparent 26%),radial-gradient(circle at 85% 40%,rgba(37,99,235,.18),transparent 30%),linear-gradient(180deg,#020617 0%,#03111f 55%,#020617 100%);color:#f8fafc}.block-container{max-width:1540px;padding:1.25rem 2.3rem 2rem}header[data-testid='stHeader']{background:transparent}#MainMenu,footer{visibility:hidden}h1,h2,h3,p,span,div{color:#f8fafc}.top-title{text-align:center;margin-bottom:1.1rem}.top-title h1{font-size:clamp(2.4rem,5.3vw,5.1rem);line-height:.92;letter-spacing:-.055em;font-weight:950;text-transform:uppercase;margin:0;text-shadow:0 0 32px rgba(125,211,252,.25)}.top-title .blue{display:block;color:#3b82f6;text-shadow:0 0 36px rgba(59,130,246,.52)}.subtitle{margin-top:.9rem;color:#cbd5e1;font-weight:700;letter-spacing:.36em;font-size:clamp(.78rem,1.2vw,1.08rem);text-transform:uppercase}.shell{display:grid;grid-template-columns:310px 1fr;gap:22px}.left-label{font-weight:900;margin:0 0 .7rem 1.05rem}.cap-card{display:grid;grid-template-columns:50px 1fr;gap:14px;align-items:center;min-height:74px;padding:.74rem .95rem;margin-bottom:7px;border-radius:10px;background:linear-gradient(135deg,rgba(8,28,50,.88),rgba(4,19,35,.86));border:1px solid rgba(56,189,248,.16)}.cap-icon{height:42px;width:42px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:1.28rem;background:rgba(14,165,233,.12);border:1px solid rgba(56,189,248,.18);box-shadow:0 0 22px rgba(56,189,248,.12)}.cap-title{font-size:.98rem;font-weight:850;line-height:1.05;margin-bottom:.25rem}.cap-desc{color:#c8d4e2;line-height:1.35;font-size:.80rem}.main-panel{border-radius:22px;border:1px solid rgba(56,189,248,.33);background:radial-gradient(circle at 78% 24%,rgba(56,189,248,.20),transparent 22%),linear-gradient(180deg,rgba(5,18,34,.95),rgba(4,13,26,.92));box-shadow:0 0 42px rgba(14,165,233,.13),0 30px 90px rgba(0,0,0,.36);overflow:hidden;min-height:610px}.panel-header{min-height:88px;display:flex;align-items:center;justify-content:space-between;gap:18px;padding:0 1.45rem;border-bottom:1px solid rgba(148,163,184,.18);background:rgba(3,12,26,.72)}.brand{display:flex;align-items:center;gap:18px}.ak-box{height:48px;width:48px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-weight:950;font-size:1.35rem;color:#38bdf8;background:rgba(14,165,233,.11);border:1px solid rgba(56,189,248,.38)}.brand-name{font-size:1.15rem;font-weight:900}.brand-role{margin-top:.35rem;font-size:.84rem;color:#dbeafe}.buttons{display:flex;gap:14px;flex-wrap:wrap}.top-button{padding:.72rem 1.05rem;border-radius:8px;background:linear-gradient(180deg,rgba(15,38,72,.86),rgba(8,24,46,.86));border:1px solid rgba(148,163,184,.22);font-weight:700;font-size:.88rem;text-decoration:none}.panel-body{display:grid;grid-template-columns:180px 1fr;min-height:520px}.inner-nav{padding:1.6rem .9rem;border-right:1px solid rgba(148,163,184,.16);background:linear-gradient(180deg,rgba(3,20,39,.88),rgba(2,9,21,.85))}.nav-row{padding:.68rem .7rem;border-radius:6px;margin-bottom:.55rem;font-size:.82rem;display:flex;gap:9px}.nav-row.active{background:linear-gradient(90deg,rgba(37,99,235,.78),rgba(14,165,233,.35))}.command-content{padding:2.35rem 1.55rem 1rem 2.35rem}.hero-grid{display:grid;grid-template-columns:1fr 420px;gap:28px;align-items:center}.small-blue{color:#7dd3fc;letter-spacing:.22em;font-size:.78rem;font-weight:800}.command-title{margin-top:.9rem;font-size:clamp(1.8rem,2.3vw,2.25rem);line-height:1.05;font-weight:950;letter-spacing:-.04em}.command-text{max-width:650px;margin-top:1rem;color:#d4dfed;line-height:1.62;font-size:.96rem}.cloud-scene{height:190px;position:relative;overflow:hidden}.cloud{position:absolute;top:8px;left:145px;font-size:5.4rem;color:#38bdf8;filter:drop-shadow(0 0 28px rgba(56,189,248,.72))}.node-base,.node-small{position:absolute;border:1px solid rgba(56,189,248,.55);background:rgba(14,165,233,.08);transform:rotate(45deg);box-shadow:0 0 18px rgba(56,189,248,.25)}.node-base{width:80px;height:80px;top:98px;left:188px}.node-small{width:44px;height:44px}.n1{top:112px;left:88px}.n2{top:135px;left:150px}.n3{top:135px;left:285px}.n4{top:112px;left:350px}.metrics-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:14px;margin-top:2.1rem}.metric-card{min-height:118px;border-radius:10px;padding:1.1rem .9rem;background:linear-gradient(180deg,rgba(12,36,65,.86),rgba(5,17,33,.92));border:1px solid rgba(148,163,184,.18);text-align:center}.metric-icon{height:34px;width:34px;margin:0 auto .55rem;border-radius:10px;display:flex;align-items:center;justify-content:center;background:rgba(37,99,235,.28)}.metric-main{font-size:1.34rem;font-weight:950;line-height:1.02}.metric-sub{margin-top:.38rem;color:#d5e2f0;font-size:.76rem;line-height:1.34}.workflow-grid{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:1rem}.workflow-card{border-radius:10px;padding:1rem;background:linear-gradient(180deg,rgba(10,31,57,.72),rgba(5,17,33,.90));border:1px solid rgba(148,163,184,.16)}.workflow-title{font-size:.78rem;color:#cfe7ff;letter-spacing:.04em;margin-bottom:1rem}.steps{display:flex;align-items:flex-start;justify-content:space-between;gap:8px}.step{text-align:center;flex:1;position:relative}.step:not(:last-child)::after{content:'→';position:absolute;right:-10px;top:13px;color:#7dd3fc}.step-icon{height:40px;width:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto .55rem;background:rgba(37,99,235,.35);border:1px solid rgba(56,189,248,.22)}.step-label{font-size:.74rem;line-height:1.2}.checks{border-top:1px solid rgba(148,163,184,.14);display:flex;justify-content:space-between;gap:10px;margin-top:1rem;padding-top:.8rem;font-size:.72rem}.check::before{content:'✓';color:#22c55e;font-weight:900;margin-right:5px}.bottom-strip{display:grid;grid-template-columns:repeat(4,1fr);border-radius:10px;border:1px solid rgba(56,189,248,.22);background:rgba(4,14,27,.78);overflow:hidden;margin-top:1rem}.bottom-item{display:grid;grid-template-columns:58px 1fr;gap:14px;padding:1.15rem 1.1rem;border-right:1px solid rgba(148,163,184,.16);min-height:100px}.bottom-item:last-child{border-right:0}.bottom-icon{font-size:2rem;color:#38bdf8;filter:drop-shadow(0 0 18px rgba(56,189,248,.34));display:flex;align-items:center;justify-content:center}.bottom-title{font-size:.95rem;font-weight:950;color:#67e8f9}.bottom-text{margin-top:.35rem;color:#cad8e7;line-height:1.36;font-size:.80rem}.footer-line{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:22px;margin-top:1rem;color:#38bdf8;letter-spacing:.52em;font-size:1rem;font-weight:800}.footer-line:before,.footer-line:after{content:'';height:1px;background:linear-gradient(90deg,transparent,rgba(56,189,248,.42))}.footer-line:after{background:linear-gradient(90deg,rgba(56,189,248,.42),transparent)}.explore{position:fixed;right:2.2rem;bottom:1.4rem;padding:.75rem 1.15rem;width:330px;border-radius:10px;background:rgba(5,20,38,.95);border:1px solid rgba(56,189,248,.35);box-shadow:0 0 30px rgba(14,165,233,.12);z-index:99}.explore .one{font-size:1rem;font-weight:800}.explore .two{margin-top:.25rem;font-size:.86rem;color:#38bdf8}.content-section{border-radius:18px;border:1px solid rgba(56,189,248,.23);background:rgba(5,18,34,.82);padding:1.3rem;margin-top:1rem}.section-title{font-size:1.45rem;font-weight:950;letter-spacing:-.03em;margin-bottom:.5rem}.section-muted{color:#a9bdd3;line-height:1.6}.tag{display:inline-block;padding:.44rem .75rem;border-radius:999px;margin:.26rem;background:rgba(14,165,233,.10);border:1px solid rgba(56,189,248,.24);color:#dbeafe;font-size:.82rem;font-weight:700}.project-card{border-radius:14px;padding:1.2rem;background:linear-gradient(135deg,rgba(9,32,58,.86),rgba(4,16,31,.86));border:1px solid rgba(148,163,184,.18);margin-bottom:.9rem}.project-tag{display:inline-block;color:#bae6fd;background:rgba(37,99,235,.22);border:1px solid rgba(56,189,248,.25);padding:.25rem .55rem;border-radius:999px;font-size:.72rem;font-weight:800}.project-title{margin-top:.7rem;font-size:1.08rem;font-weight:900}@media(max-width:1150px){.shell{grid-template-columns:1fr}.capability-rail{display:grid;grid-template-columns:repeat(2,1fr);gap:8px}.panel-body{grid-template-columns:1fr}.inner-nav{display:none}.hero-grid{grid-template-columns:1fr}.metrics-grid{grid-template-columns:repeat(2,1fr)}.workflow-grid{grid-template-columns:1fr}.bottom-strip{grid-template-columns:1fr}.bottom-item{border-right:0;border-bottom:1px solid rgba(148,163,184,.16)}.explore{position:static;width:auto;margin-top:1rem}}
</style>
""",
    unsafe_allow_html=True,
)


def capability_html():
    cards = "".join(
        f"""
        <div class="cap-card">
            <div class="cap-icon">{icon}</div>
            <div>
                <div class="cap-title">{title}</div>
                <div class="cap-desc">{desc}</div>
            </div>
        </div>
        """
        for icon, title, desc in CAPABILITY_RAIL
    )
    return f"<div class='left-label'>ENGINEERING CAPABILITIES</div><div class='capability-rail'>{cards}</div>"


def nav_html():
    rows = "".join(
        f"<div class='nav-row {'active' if i == 0 else ''}'><span>{'⌂' if i == 0 else '•'}</span><span>{label}</span></div>"
        for i, label in enumerate(NAV_ITEMS)
    )
    return f"<div class='inner-nav'>{rows}</div>"


def metrics_html():
    return "<div class='metrics-grid'>" + "".join(
        f"""
        <div class='metric-card'>
            <div class='metric-icon'>{icon}</div>
            <div class='metric-main'>{main}</div>
            <div class='metric-sub'>{line1}<br>{line2}</div>
        </div>
        """
        for icon, main, line1, line2 in METRICS
    ) + "</div>"


def workflow_html(title, steps, checks):
    step_html = "".join(
        f"<div class='step'><div class='step-icon'>{icon}</div><div class='step-label'>{label}</div></div>"
        for icon, label in steps
    )
    check_html = "".join(f"<span class='check'>{check}</span>" for check in checks)
    return f"<div class='workflow-card'><div class='workflow-title'>{title}</div><div class='steps'>{step_html}</div><div class='checks'>{check_html}</div></div>"


def bottom_html():
    return "<div class='bottom-strip'>" + "".join(
        f"""
        <div class='bottom-item'>
            <div class='bottom-icon'>{icon}</div>
            <div><div class='bottom-title'>{title}</div><div class='bottom-text'>{text}</div></div>
        </div>
        """
        for icon, title, text in BOTTOM_CARDS
    ) + "</div>"


st.markdown(
    f"""
<div class='top-title'>
    <h1>ENTERPRISE DEVSECOPS &<span class='blue'>PLATFORM ENGINEERING PORTFOLIO</span></h1>
    <div class='subtitle'>{PROFILE['subheadline']}</div>
</div>

<div class='shell'>
    <div>{capability_html()}</div>
    <div>
        <div class='main-panel'>
            <div class='panel-header'>
                <div class='brand'>
                    <div class='ak-box'>{PROFILE['initials']}</div>
                    <div><div class='brand-name'>{PROFILE['name']}</div><div class='brand-role'>{PROFILE['role']}</div></div>
                </div>
                <div class='buttons'>
                    <a class='top-button' href='#resume'>▣ Resume</a>
                    <a class='top-button' href='https://www.linkedin.com/' target='_blank'>in LinkedIn</a>
                    <a class='top-button' href='https://github.com/' target='_blank'>● GitHub</a>
                    <a class='top-button' href='mailto:{PROFILE['email']}'>✉ Contact</a>
                </div>
            </div>
            <div class='panel-body'>
                {nav_html()}
                <div class='command-content'>
                    <div class='hero-grid'>
                        <div>
                            <div class='small-blue'>WELCOME TO</div>
                            <div class='command-title'>Platform Engineering Command Center</div>
                            <div class='command-text'>Building enterprise-grade automation platforms and delivering scalable, secure and resilient engineering solutions.</div>
                        </div>
                        <div class='cloud-scene'>
                            <div class='cloud'>☁</div>
                            <div class='node-base'></div><div class='node-small n1'></div><div class='node-small n2'></div><div class='node-small n3'></div><div class='node-small n4'></div>
                        </div>
                    </div>
                    {metrics_html()}
                    <div class='workflow-grid'>
                        {workflow_html('CI/CD PIPELINE OVERVIEW', PIPELINE, ['Automated', 'Secure', 'Scalable', 'Observable'])}
                        {workflow_html('REMEDIATION WORKFLOW', REMEDIATION, ['Detect Faster', 'Automate Remediation', 'Reduce Risk'])}
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

{bottom_html()}
<div class='footer-line'><span>AUTOMATE • ORCHESTRATE • SECURE • SCALE</span></div>
<div class='explore'><div class='one'>Explore the Portfolio →</div><div class='two'>{PROFILE['url']}</div></div>
""",
    unsafe_allow_html=True,
)

st.markdown("<div id='resume'></div>", unsafe_allow_html=True)

st.markdown(
    """
<div class='content-section'>
    <div class='section-title'>Professional Summary</div>
    <div class='section-muted'>Senior Platform & DevSecOps Engineer with 6+ years of experience designing and scaling enterprise automation platforms within large banking and financial services environments. Specialized in CI/CD automation, cloud infrastructure, platform engineering, vulnerability remediation, and policy-driven operational automation that transforms manual processes into scalable self-service systems.</div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class='content-section'>
    <div class='section-title'>Core Technology Stack</div>
    <div class='section-muted'>Recruiter-searchable skills aligned with senior DevSecOps, platform engineering and cloud automation roles.</div>
</div>
""",
    unsafe_allow_html=True,
)
st.markdown("".join(f"<span class='tag'>{skill}</span>" for skill in TECH_STACK), unsafe_allow_html=True)

st.markdown(
    """
<div class='content-section'>
    <div class='section-title'>Project Showcase</div>
    <div class='section-muted'>Portfolio-safe project storytelling focused on architecture, execution capability and enterprise impact.</div>
</div>
""",
    unsafe_allow_html=True,
)

for tag, title, text in PROJECTS:
    st.markdown(
        f"""
<div class='project-card'>
    <span class='project-tag'>{tag}</span>
    <div class='project-title'>{title}</div>
    <div class='section-muted' style='margin-top:.5rem'>{text}</div>
</div>
""",
        unsafe_allow_html=True,
    )

st.markdown(
    """
<div class='content-section'>
    <div class='section-title'>Recruiter Note</div>
    <div class='section-muted'>Open for senior individual contributor roles across DevSecOps, Platform Engineering, Cloud Engineering and Automation Engineering. Strong fit for teams building internal developer platforms, secure delivery systems, remediation workflows, cloud automation and enterprise governance platforms.</div>
</div>
""",
    unsafe_allow_html=True,
)
