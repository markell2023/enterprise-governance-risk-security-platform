import streamlit as st
import pandas as pd

from modules.ui_components import kpi_card


def show_cyber_operations():

    st.title("Cyber Operations")

    st.caption(
        "Monitor security operations, incidents, vulnerabilities, and operational health."
    )

    st.markdown("---")

    incidents = pd.DataFrame(
        [
            {
                "Incident": "Unauthorized Login Attempts",
                "Severity": "Medium",
                "Status": "Monitoring",
                "Owner": "SOC Team"
            },
            {
                "Incident": "Critical Server Patch",
                "Severity": "High",
                "Status": "In Progress",
                "Owner": "Infrastructure"
            },
            {
                "Incident": "Phishing Campaign",
                "Severity": "Critical",
                "Status": "Active",
                "Owner": "Security Operations"
            },
            {
                "Incident": "Endpoint Malware Detection",
                "Severity": "Low",
                "Status": "Resolved",
                "Owner": "Endpoint Team"
            }
        ]
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        kpi_card("Open Incidents", "4", "Active security queue")

    with col2:
        kpi_card("Critical", "1", "Immediate response required")

    with col3:
        kpi_card("Resolved Today", "2", "Closed by security teams")

    with col4:
        kpi_card("Systems Healthy", "98%", "Operational security health")

    st.markdown("---")

    st.subheader("Security Operations Queue")

    st.dataframe(
        incidents,
        use_container_width=True,
        hide_index=True,
    )

    st.markdown("---")

    st.subheader("Executive Insight")

    st.info(
        """
A phishing campaign is currently the highest operational security priority.

Critical infrastructure patching remains on schedule with no production outages reported.

Recommendation:

• Continue phishing monitoring

• Complete server patch deployment

• Validate endpoint protection across all corporate devices
"""
    )