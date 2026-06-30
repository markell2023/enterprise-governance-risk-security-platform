import streamlit as st

def metric_card(label, value, note):
    st.markdown(
        f"""
        <div style="
            background-color:#1E1E1E;
            padding:20px;
            border-radius:16px;
            border:1px solid #2D2D2D;
            box-shadow:0 0 18px rgba(59,130,246,0.08);
        ">
            <div style="color:#94A3B8;font-size:0.85rem;">{label}</div>
            <div style="color:#F8FAFC;font-size:1.8rem;font-weight:800;">{value}</div>
            <div style="color:#64748B;font-size:0.8rem;">{note}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

def show_executive_dashboard():
    st.markdown(
        "<h1 class='main-title'>Enterprise Governance, Risk & Security Platform</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p class='subtitle'>Executive risk overview for Apex Horizon Energy</p>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        metric_card("Enterprise Risk Score", "72 / 100", "Moderate risk posture")
    with col2:
        metric_card("Compliance Score", "91%", "NIST, ISO 27001, SOC 2")
    with col3:
        metric_card("Critical Risks", "4", "Require executive review")

    st.markdown("")

    col4, col5, col6 = st.columns(3)
    with col4:
        metric_card("Cyber Alerts", "18", "2 critical alerts open")
    with col5:
        metric_card("AI Models Monitored", "7", "1 requires validation")
    with col6:
        metric_card("Open Audits", "3", "Next audit due in 14 days")

    st.markdown("---")
    st.subheader("Executive Summary")
    st.write(
        "Apex Horizon Energy currently has a moderate enterprise risk posture. "
        "Priority areas include privileged access management, AI model validation, "
        "vendor security reviews, and cybersecurity incident response readiness."
    )