import pandas as pd
import plotly.express as px
import streamlit as st

from modules.ui_components import kpi_card


def show_audit_center():
    st.title("Audit Center")

    st.caption(
        "Track internal and external audits, findings, remediation owners, "
        "due dates, and audit readiness."
    )

    st.markdown("---")

    audits = pd.DataFrame(
        [
            [
                "AUD-001",
                "Internal Access Control Audit",
                "Internal",
                "Identity & Access Management",
                "In Progress",
                "High",
                3,
                "Jordan Lee",
                "2026-07-18",
            ],
            [
                "AUD-002",
                "SOC 2 Readiness Review",
                "External",
                "Compliance",
                "Planned",
                "Medium",
                2,
                "Morgan Reed",
                "2026-08-05",
            ],
            [
                "AUD-003",
                "Cloud Security Configuration Audit",
                "Internal",
                "Infrastructure",
                "Open",
                "Critical",
                4,
                "Taylor Brooks",
                "2026-07-12",
            ],
            [
                "AUD-004",
                "Vendor Assurance Audit",
                "Internal",
                "Third-Party Risk",
                "In Progress",
                "High",
                2,
                "Casey Morgan",
                "2026-07-22",
            ],
            [
                "AUD-005",
                "Incident Response Program Review",
                "External",
                "Cyber Operations",
                "Complete",
                "Low",
                1,
                "Avery Collins",
                "2026-06-28",
            ],
            [
                "AUD-006",
                "AI Model Governance Review",
                "Internal",
                "AI Governance",
                "Open",
                "High",
                3,
                "Riley Parker",
                "2026-07-16",
            ],
        ],
        columns=[
            "Audit ID",
            "Audit",
            "Audit Type",
            "Business Area",
            "Status",
            "Highest Finding",
            "Open Findings",
            "Audit Owner",
            "Target Date",
        ],
    )

    findings = pd.DataFrame(
        [
            [
                "FND-001",
                "AUD-001",
                "Privileged access reviews are not consistently documented",
                "High",
                "Identity & Access Management",
                "Open",
                "2026-07-15",
            ],
            [
                "FND-002",
                "AUD-001",
                "Terminated user access removal evidence is incomplete",
                "Medium",
                "Human Resources",
                "In Progress",
                "2026-07-18",
            ],
            [
                "FND-003",
                "AUD-003",
                "Public cloud storage configuration allows excessive access",
                "Critical",
                "Cloud Security",
                "Open",
                "2026-07-11",
            ],
            [
                "FND-004",
                "AUD-003",
                "Cloud logging coverage is incomplete",
                "High",
                "Security Engineering",
                "In Progress",
                "2026-07-20",
            ],
            [
                "FND-005",
                "AUD-004",
                "Annual vendor assessments are overdue",
                "High",
                "Third-Party Risk",
                "Open",
                "2026-07-19",
            ],
            [
                "FND-006",
                "AUD-006",
                "Model approval evidence is missing",
                "High",
                "AI Governance",
                "Open",
                "2026-07-14",
            ],
            [
                "FND-007",
                "AUD-005",
                "Incident escalation matrix requires minor updates",
                "Low",
                "Cyber Operations",
                "Resolved",
                "2026-06-25",
            ],
        ],
        columns=[
            "Finding ID",
            "Audit ID",
            "Finding",
            "Severity",
            "Owner",
            "Status",
            "Due Date",
        ],
    )

    total_audits = len(audits)

    active_audits = len(
        audits[
            audits["Status"].isin(
                [
                    "Open",
                    "In Progress",
                ]
            )
        ]
    )

    open_findings = len(
        findings[
            findings["Status"].isin(
                [
                    "Open",
                    "In Progress",
                ]
            )
        ]
    )

    critical_findings = len(
        findings[
            findings["Severity"] == "Critical"
        ]
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        kpi_card(
            "Total Audits",
            total_audits,
            "Current audit inventory",
        )

    with col2:
        kpi_card(
            "Active Audits",
            active_audits,
            "Open or in progress",
        )

    with col3:
        kpi_card(
            "Open Findings",
            open_findings,
            "Require remediation",
        )

    with col4:
        kpi_card(
            "Critical Findings",
            critical_findings,
            "Immediate leadership attention",
        )

    st.markdown("---")

    # -----------------------------
    # Horizontal Severity Chart
    # -----------------------------

    st.subheader("Audit Finding Severity")

    severity_order = [
        "Critical",
        "High",
        "Medium",
        "Low",
    ]

    severity_summary = (
        findings.groupby("Severity")
        .size()
        .reindex(
            severity_order,
            fill_value=0,
        )
        .reset_index(name="Findings")
    )

    severity_summary["Severity"] = pd.Categorical(
        severity_summary["Severity"],
        categories=severity_order,
        ordered=True,
    )

    severity_summary = severity_summary.sort_values(
        "Severity",
        ascending=False,
    )

    severity_chart = px.bar(
        severity_summary,
        x="Findings",
        y="Severity",
        orientation="h",
        color="Severity",
        text="Findings",
        color_discrete_map={
            "Critical": "#991B1B",
            "High": "#EF4444",
            "Medium": "#F59E0B",
            "Low": "#22C55E",
        },
    )

    severity_chart.update_traces(
        textposition="outside",
        cliponaxis=False,
        hovertemplate=(
            "<b>%{y}</b><br>"
            "Findings: %{x}"
            "<extra></extra>"
        ),
    )

    severity_chart.update_layout(
        height=360,
        margin=dict(
            l=10,
            r=40,
            t=10,
            b=10,
        ),
        xaxis_title="Finding count",
        yaxis_title="",
        xaxis=dict(
            dtick=1,
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
        severity_chart,
        use_container_width=True,
        config={
            "displayModeBar": False,
        },
    )

    st.markdown("---")

    # -----------------------------
    # Audit Portfolio
    # -----------------------------

    st.subheader("Audit Portfolio")

    audit_filter_col1, audit_filter_col2 = st.columns(2)

    with audit_filter_col1:
        selected_audit_type = st.selectbox(
            "Filter by Audit Type",
            [
                "All",
                *sorted(
                    audits["Audit Type"]
                    .unique()
                    .tolist()
                ),
            ],
        )

    with audit_filter_col2:
        selected_audit_status = st.selectbox(
            "Filter by Audit Status",
            [
                "All",
                *sorted(
                    audits["Status"]
                    .unique()
                    .tolist()
                ),
            ],
        )

    filtered_audits = audits.copy()

    if selected_audit_type != "All":
        filtered_audits = filtered_audits[
            filtered_audits["Audit Type"]
            == selected_audit_type
        ]

    if selected_audit_status != "All":
        filtered_audits = filtered_audits[
            filtered_audits["Status"]
            == selected_audit_status
        ]

    st.dataframe(
        filtered_audits,
        use_container_width=True,
        hide_index=True,
    )

    st.markdown("---")

    # -----------------------------
    # Audit Findings
    # -----------------------------

    st.subheader("Audit Findings")

    finding_filter_col1, finding_filter_col2 = st.columns(2)

    with finding_filter_col1:
        selected_finding_severity = st.selectbox(
            "Filter by Finding Severity",
            [
                "All",
                *severity_order,
            ],
        )

    with finding_filter_col2:
        selected_finding_status = st.selectbox(
            "Filter by Finding Status",
            [
                "All",
                *sorted(
                    findings["Status"]
                    .unique()
                    .tolist()
                ),
            ],
        )

    filtered_findings = findings.copy()

    if selected_finding_severity != "All":
        filtered_findings = filtered_findings[
            filtered_findings["Severity"]
            == selected_finding_severity
        ]

    if selected_finding_status != "All":
        filtered_findings = filtered_findings[
            filtered_findings["Status"]
            == selected_finding_status
        ]

    st.dataframe(
        filtered_findings,
        use_container_width=True,
        hide_index=True,
    )

    st.markdown("---")

    # -----------------------------
    # Executive Insight
    # -----------------------------

    st.subheader("Executive Insight")

    st.info(
        """
Audit activity remains elevated, with four audits currently open or in progress.

One critical cloud security finding requires immediate remediation, and several high-severity findings remain open across access management, vendor assurance, cloud logging, and AI governance.

Recommended Actions:

• Escalate FND-003 for immediate cloud access remediation

• Require owners to provide recovery dates for open high-severity findings

• Verify evidence closure before findings are marked resolved

• Review overdue audit actions during the next governance committee meeting
"""
    )