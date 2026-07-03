import streamlit as st
import pandas as pd

from modules.ui_components import kpi_card


def show_vendor_risk():
    st.title("Vendor Risk")

    st.caption(
        "Monitor third-party vendor security posture, compliance status, and remediation activities."
    )

    st.markdown("---")

    vendors = pd.DataFrame(
        [
            ["Microsoft Azure", "Critical", "Low", "Current", "Complete", "Infrastructure"],
            ["Okta", "Critical", "Medium", "Current", "Complete", "Identity Team"],
            ["Snowflake", "High", "Medium", "Expired", "Pending", "Data Engineering"],
            ["Stripe", "High", "Low", "Current", "Complete", "Finance"],
            ["CrowdStrike", "Critical", "Low", "Current", "Complete", "Cybersecurity"],
        ],
        columns=[
            "Vendor",
            "Criticality",
            "Risk",
            "SOC 2",
            "Security Review",
            "Owner",
        ],
    )

    total_vendors = len(vendors)
    critical_vendors = len(vendors[vendors["Criticality"] == "Critical"])
    pending_reviews = len(vendors[vendors["Security Review"] == "Pending"])
    expired_soc = len(vendors[vendors["SOC 2"] == "Expired"])

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        kpi_card("Vendors", total_vendors, "Third-party inventory")

    with col2:
        kpi_card("Critical Vendors", critical_vendors, "Business-critical suppliers")

    with col3:
        kpi_card("Pending Reviews", pending_reviews, "Awaiting security review")

    with col4:
        kpi_card("Expired SOC Reports", expired_soc, "Requires documentation update")

    st.markdown("---")

    st.subheader("Third-Party Vendor Inventory")

    st.dataframe(
        vendors,
        use_container_width=True,
        hide_index=True,
    )

    st.markdown("---")

    st.subheader("Executive Insight")

    st.info(
        """
Snowflake currently has an expired SOC 2 report and a pending security review.

All critical vendors remain operational, but third-party assurance documentation should be updated before the next quarterly governance meeting.

Recommendation:

• Request updated SOC 2 report from Snowflake

• Complete third-party security assessment

• Review vendor risk with executive leadership
"""
    )