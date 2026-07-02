import streamlit as st
import pandas as pd


def show_enterprise_risk():
    st.markdown(
        "<h1 class='main-title'>Enterprise Risk Register</h1>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<p class='subtitle'>Track enterprise risks, ownership, impact, likelihood, scoring, and mitigation status for Apex Horizon Energy.</p>",
        unsafe_allow_html=True,
    )

    risks = pd.DataFrame(
        [
            ["R-001", "Cybersecurity", "Privileged access misuse", "Corporate IT", "High", "Critical", 20, "Open", "Implement privileged access management"],
            ["R-002", "AI Governance", "Credit model validation expired", "Data Science", "Medium", "High", 12, "In Progress", "Schedule model revalidation"],
            ["R-003", "Vendor Risk", "Third-party SOC report overdue", "Supply Chain", "High", "High", 16, "Monitoring", "Request updated SOC 2 report"],
            ["R-004", "Compliance", "NIST incident response gap", "Compliance", "Medium", "High", 12, "Open", "Update IR plan and run tabletop exercise"],
            ["R-005", "Operational", "Pipeline monitoring outage", "Operations Technology", "Low", "Critical", 10, "Mitigating", "Improve monitoring redundancy"],
            ["R-006", "Privacy", "Employee data access review overdue", "Human Resources", "Medium", "Medium", 9, "In Progress", "Complete quarterly access review"],
            ["R-007", "Business Continuity", "Disaster recovery test delayed", "Corporate IT", "Medium", "High", 12, "Open", "Schedule DR test with infrastructure team"],
        ],
        columns=[
            "Risk ID",
            "Category",
            "Risk Name",
            "Owner",
            "Likelihood",
            "Impact",
            "Risk Score",
            "Status",
            "Mitigation Plan",
        ],
    )

    total_risks = len(risks)
    high_risks = len(risks[risks["Risk Score"] >= 15])
    open_risks = len(risks[risks["Status"] == "Open"])
    avg_score = round(risks["Risk Score"].mean(), 1)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Risks", total_risks)
    col2.metric("High/Critical Risks", high_risks)
    col3.metric("Open Risks", open_risks)
    col4.metric("Avg. Risk Score", avg_score)

    st.markdown("---")

    st.subheader("Risk Filters")

    search_text = st.text_input("Search risk name or owner")

    col_filter1, col_filter2 = st.columns(2)

    with col_filter1:
        selected_category = st.selectbox(
            "Category",
            ["All"] + sorted(risks["Category"].unique().tolist()),
        )

    with col_filter2:
        selected_status = st.selectbox(
            "Status",
            ["All"] + sorted(risks["Status"].unique().tolist()),
        )

    filtered_risks = risks.copy()

    if search_text:
        filtered_risks = filtered_risks[
            filtered_risks["Risk Name"].str.contains(search_text, case=False, na=False)
            | filtered_risks["Owner"].str.contains(search_text, case=False, na=False)
        ]

    if selected_category != "All":
        filtered_risks = filtered_risks[filtered_risks["Category"] == selected_category]

    if selected_status != "All":
        filtered_risks = filtered_risks[filtered_risks["Status"] == selected_status]

    st.markdown("---")

    st.subheader("Risk Register")

    st.dataframe(
        filtered_risks,
        use_container_width=True,
        hide_index=True,
    )