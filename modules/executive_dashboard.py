import streamlit as st

from modules.executive_intelligence import show_executive_intelligence
from modules.ui_components import kpi_card


def show_executive_dashboard():
    st.markdown(
        "<h1 class='main-title'>Enterprise Governance, Risk & Security Platform</h1>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<p class='subtitle'>Executive risk overview for Apex Horizon Energy</p>",
        unsafe_allow_html=True,
    )

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        kpi_card("Enterprise Risk Score", "72 / 100", "Moderate risk posture")

    with col2:
        kpi_card("Compliance Score", "91%", "NIST, ISO 27001, SOC 2")

    with col3:
        kpi_card("Critical Risks", "4", "Require executive review")

    st.markdown("")

    col4, col5, col6 = st.columns(3)

    with col4:
        kpi_card("Cyber Alerts", "18", "2 critical alerts open")

    with col5:
        kpi_card("AI Models Monitored", "7", "1 requires validation")

    with col6:
        kpi_card("Open Audits", "3", "Next audit due in 14 days")

    st.markdown("---")

    show_executive_intelligence()