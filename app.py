import streamlit as st

from modules.executive_dashboard import show_executive_dashboard
from modules.enterprise_risk import show_enterprise_risk
from modules.ai_governance import show_ai_governance
from modules.cyber_operations import show_cyber_operations
from modules.incidents import show_incidents
from modules.vendor_risk import show_vendor_risk
from modules.compliance import show_compliance
from modules.audit_center import show_audit_center
from modules.assets import show_assets
from modules.vulnerabilities import show_vulnerabilities
from modules.reports import show_reports
from theme.styles import load_theme


# Replace this after your Streamlit deployment is created.
LIVE_DEMO_URL = "YOUR_STREAMLIT_URL_HERE"

GITHUB_REPOSITORY_URL = (
    "https://github.com/markell2023/"
    "enterprise-governance-risk-security-platform"
)


st.set_page_config(
    page_title="Enterprise Governance, Risk & Security Platform",
    page_icon="🛡️",
    layout="wide",
)

# ----------------------------------
# Global Theme
# ----------------------------------

st.markdown(load_theme(), unsafe_allow_html=True)

# ----------------------------------
# Sidebar Branding
# ----------------------------------

st.sidebar.title("🛡️ EGRSP")

st.sidebar.caption(
    "Enterprise Governance, Risk & Security Platform"
)

st.sidebar.caption("Apex Horizon Energy")
st.sidebar.caption("Fictional Portfolio Demo")

st.sidebar.divider()

# ----------------------------------
# Navigation
# ----------------------------------

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Enterprise Risk",
        "AI Governance",
        "Cyber Operations",
        "Incidents",
        "Vendor Risk",
        "Compliance",
        "Audit Center",
        "Assets",
        "Vulnerabilities",
        "Reports",
    ],
)

st.sidebar.divider()

# ----------------------------------
# Project Links
# ----------------------------------

st.sidebar.markdown("**Project Links**")

st.sidebar.link_button(
    "View GitHub Repository",
    GITHUB_REPOSITORY_URL,
    use_container_width=True,
)

if LIVE_DEMO_URL != "YOUR_STREAMLIT_URL_HERE":
    st.sidebar.link_button(
        "Open Live Application",
        LIVE_DEMO_URL,
        use_container_width=True,
    )
else:
    st.sidebar.caption(
        "Live application link will appear after deployment."
    )

st.sidebar.divider()

# ----------------------------------
# User and Application Information
# ----------------------------------

st.sidebar.markdown("**User**")
st.sidebar.caption("Markell Mitchell")

st.sidebar.markdown("**Role**")
st.sidebar.caption("Governance & Risk Analyst")

st.sidebar.markdown("**Application**")
st.sidebar.caption("Version 1.0.0")
st.sidebar.caption("Demo Environment")

# ----------------------------------
# Main Pages
# ----------------------------------

if page == "Dashboard":
    show_executive_dashboard()

elif page == "Enterprise Risk":
    show_enterprise_risk()

elif page == "AI Governance":
    show_ai_governance()

elif page == "Cyber Operations":
    show_cyber_operations()

elif page == "Incidents":
    show_incidents()

elif page == "Vendor Risk":
    show_vendor_risk()

elif page == "Compliance":
    show_compliance()

elif page == "Audit Center":
    show_audit_center()

elif page == "Assets":
    show_assets()

elif page == "Vulnerabilities":
    show_vulnerabilities()

elif page == "Reports":
    show_reports()

# ----------------------------------
# Footer
# ----------------------------------

st.divider()

st.markdown(
    "**Enterprise Governance, Risk & Security Platform (EGRSP)**"
)

st.caption(
    "Apex Horizon Energy • Fictional Demo Environment"
)

st.caption(
    "Version 1.0.0 • Developed by Markell Mitchell"
)

st.caption(
    "Built with Python • Streamlit • Pandas • Plotly"
)

st.caption(
    "All organizations, assessments, risks, incidents, vendors, findings, "
    "and performance metrics displayed in this application are fictional "
    "and were created for educational and portfolio demonstration purposes."
)