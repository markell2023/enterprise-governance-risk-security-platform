import streamlit as st

from modules.executive_dashboard import show_executive_dashboard
from modules.enterprise_risk import show_enterprise_risk
from theme.styles import load_theme


st.set_page_config(
    page_title="Enterprise Governance, Risk & Security Platform",
    page_icon="🛡️",
    layout="wide",
)

# Load global theme
st.markdown(load_theme(), unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.markdown("## EGRSP")
st.sidebar.caption("Apex Horizon Energy")

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

st.sidebar.markdown("---")

st.sidebar.caption("User: Markell Mitchell")
st.sidebar.caption("Role: Governance & Risk Analyst")

# -----------------------------
# Main Pages
# -----------------------------

if page == "Dashboard":
    show_executive_dashboard()

elif page == "Enterprise Risk":
    show_enterprise_risk()

else:
    st.markdown(
        f"<h1 class='main-title'>{page}</h1>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<p class='subtitle'>Module under development.</p>",
        unsafe_allow_html=True,
    )

    st.info("This page will be implemented in a future sprint.")