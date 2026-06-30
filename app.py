import streamlit as st
from modules.executive_dashboard import show_executive_dashboard

st.set_page_config(
    page_title="Enterprise Governance, Risk & Security Platform",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #121212;
    color: #F8FAFC;
}
section[data-testid="stSidebar"] {
    background-color: #181818;
}
.main-title {
    font-size: 2.3rem;
    font-weight: 800;
    color: #F8FAFC;
}
.subtitle {
    color: #94A3B8;
    font-size: 1rem;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("## 🛡️ EGRSP")
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
        "Reports"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("User: Markell Mitchell")
st.sidebar.caption("Role: Governance & Risk Analyst")

if "Dashboard" in page:
    show_executive_dashboard()
else:
    st.markdown(f"<h1 class='main-title'>{page}</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p class='subtitle'>Module shell created. Full functionality coming in a future sprint.</p>",
        unsafe_allow_html=True
    )
    st.info("This page is part of the project roadmap.")