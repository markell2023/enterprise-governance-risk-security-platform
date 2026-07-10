import pandas as pd
import plotly.express as px
import streamlit as st

from modules.ui_components import kpi_card


def show_reports():
    st.title("Executive Reports")

    st.caption(
        "Review enterprise security performance, generate leadership reports, "
        "and track scheduled reporting activity."
    )

    st.markdown("---")

    scorecard = pd.DataFrame(
        [
            ["Enterprise Risk", 72, "Moderate"],
            ["Compliance", 50, "Needs Improvement"],
            ["Cyber Operations", 88, "Strong"],
            ["Vendor Risk", 78, "Moderate"],
            ["AI Governance", 75, "Moderate"],
            ["Vulnerability Management", 63, "Needs Improvement"],
            ["Audit Readiness", 70, "Moderate"],
            ["Asset Security", 80, "Strong"],
        ],
        columns=[
            "Security Domain",
            "Score",
            "Status",
        ],
    )

    available_reports = pd.DataFrame(
        [
            [
                "RPT-001",
                "Executive Risk Summary",
                "Executive",
                "Monthly",
                "Governance & Risk",
                "2026-07-10",
            ],
            [
                "RPT-002",
                "Board Risk Report",
                "Executive",
                "Quarterly",
                "Chief Risk Officer",
                "2026-06-30",
            ],
            [
                "RPT-003",
                "Cyber Operations Dashboard",
                "Operational",
                "Weekly",
                "Security Operations",
                "2026-07-09",
            ],
            [
                "RPT-004",
                "Compliance Status Report",
                "Compliance",
                "Monthly",
                "Compliance",
                "2026-07-01",
            ],
            [
                "RPT-005",
                "Vulnerability Remediation Report",
                "Operational",
                "Weekly",
                "Vulnerability Management",
                "2026-07-08",
            ],
            [
                "RPT-006",
                "Incident Response Summary",
                "Operational",
                "Monthly",
                "Cyber Operations",
                "2026-07-05",
            ],
            [
                "RPT-007",
                "Vendor Risk Review",
                "Third-Party Risk",
                "Quarterly",
                "Vendor Risk",
                "2026-06-25",
            ],
            [
                "RPT-008",
                "Audit Findings Report",
                "Audit",
                "Monthly",
                "Internal Audit",
                "2026-07-03",
            ],
        ],
        columns=[
            "Report ID",
            "Report",
            "Category",
            "Frequency",
            "Owner",
            "Last Generated",
        ],
    )

    scheduled_reports = pd.DataFrame(
        [
            [
                "Weekly Executive Brief",
                "Weekly",
                "Monday 8:00 AM",
                "Executive Leadership",
                "Active",
            ],
            [
                "Monthly Cyber Dashboard",
                "Monthly",
                "First business day",
                "CISO",
                "Active",
            ],
            [
                "Quarterly Board Risk Report",
                "Quarterly",
                "Quarter end",
                "Board Risk Committee",
                "Active",
            ],
            [
                "Monthly Compliance Package",
                "Monthly",
                "15th of each month",
                "Compliance Leadership",
                "Active",
            ],
        ],
        columns=[
            "Scheduled Report",
            "Frequency",
            "Delivery",
            "Audience",
            "Status",
        ],
    )

    overall_score = round(scorecard["Score"].mean())
    strong_domains = len(scorecard[scorecard["Score"] >= 80])
    improvement_domains = len(scorecard[scorecard["Score"] < 70])
    scheduled_count = len(scheduled_reports)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        kpi_card(
            "Enterprise Security Score",
            f"{overall_score}%",
            "Average across security domains",
        )

    with col2:
        kpi_card(
            "Strong Domains",
            strong_domains,
            "Scores at or above 80%",
        )

    with col3:
        kpi_card(
            "Needs Improvement",
            improvement_domains,
            "Scores below 70%",
        )

    with col4:
        kpi_card(
            "Scheduled Reports",
            scheduled_count,
            "Automated leadership reporting",
        )

    st.markdown("---")

    st.subheader("Enterprise Security Scorecard")

    scorecard_chart = px.bar(
        scorecard.sort_values("Score"),
        x="Score",
        y="Security Domain",
        orientation="h",
        color="Status",
        text="Score",
        range_x=[0, 100],
        color_discrete_map={
            "Strong": "#22C55E",
            "Moderate": "#F59E0B",
            "Needs Improvement": "#EF4444",
        },
    )

    scorecard_chart.update_traces(
        texttemplate="%{text:.0f}%",
        textposition="outside",
        cliponaxis=False,
        hovertemplate=(
            "<b>%{y}</b><br>"
            "Score: %{x:.0f}%"
            "<extra></extra>"
        ),
    )

    scorecard_chart.update_layout(
        height=500,
        margin=dict(
            l=10,
            r=45,
            t=10,
            b=10,
        ),
        xaxis_title="Security score",
        yaxis_title="",
        xaxis=dict(
            range=[0, 105],
            ticksuffix="%",
            showgrid=True,
            gridcolor="#2D2D2D",
            zeroline=False,
        ),
        paper_bgcolor="#121212",
        plot_bgcolor="#121212",
        font=dict(
            color="#F8FAFC",
        ),
        showlegend=False,
    )

    st.plotly_chart(
        scorecard_chart,
        use_container_width=True,
        config={
            "displayModeBar": False,
        },
    )

    st.markdown("---")

    st.subheader("Report Library")

    filter_col1, filter_col2 = st.columns(2)

    with filter_col1:
        selected_category = st.selectbox(
            "Filter by Category",
            [
                "All",
                *sorted(
                    available_reports["Category"]
                    .unique()
                    .tolist()
                ),
            ],
        )

    with filter_col2:
        selected_frequency = st.selectbox(
            "Filter by Frequency",
            [
                "All",
                *sorted(
                    available_reports["Frequency"]
                    .unique()
                    .tolist()
                ),
            ],
        )

    filtered_reports = available_reports.copy()

    if selected_category != "All":
        filtered_reports = filtered_reports[
            filtered_reports["Category"] == selected_category
        ]

    if selected_frequency != "All":
        filtered_reports = filtered_reports[
            filtered_reports["Frequency"] == selected_frequency
        ]

    st.dataframe(
        filtered_reports,
        use_container_width=True,
        hide_index=True,
    )

    st.markdown("---")

    st.subheader("Scheduled Reports")

    st.dataframe(
        scheduled_reports,
        use_container_width=True,
        hide_index=True,
    )

    st.markdown("---")

    st.subheader("Export Center")

    export_col1, export_col2, export_col3 = st.columns(3)

    report_csv = available_reports.to_csv(index=False).encode("utf-8")
    scorecard_csv = scorecard.to_csv(index=False).encode("utf-8")
    schedule_csv = scheduled_reports.to_csv(index=False).encode("utf-8")

    with export_col1:
        st.download_button(
            label="Download Report Library",
            data=report_csv,
            file_name="report_library.csv",
            mime="text/csv",
            use_container_width=True,
        )

    with export_col2:
        st.download_button(
            label="Download Security Scorecard",
            data=scorecard_csv,
            file_name="security_scorecard.csv",
            mime="text/csv",
            use_container_width=True,
        )

    with export_col3:
        st.download_button(
            label="Download Report Schedule",
            data=schedule_csv,
            file_name="scheduled_reports.csv",
            mime="text/csv",
            use_container_width=True,
        )

    st.markdown("---")

    st.subheader("Executive Insight")

    st.info(
        """
Overall enterprise security performance is moderate.

Cyber Operations and Asset Security are the strongest-performing domains. Compliance and Vulnerability Management require the most immediate improvement.

Recommended Actions:

• Prioritize remediation of compliance gaps and overdue vulnerabilities

• Present the updated security scorecard during the next executive risk meeting

• Continue weekly executive briefings until critical findings are reduced

• Track domain scores monthly to demonstrate measurable risk reduction
"""
    )