import pandas as pd
import plotly.express as px
import streamlit as st

from modules.ui_components import kpi_card


def show_vulnerabilities():
    st.title("Vulnerability Management")

    st.caption(
        "Track vulnerability severity, affected assets, remediation ownership, "
        "and service-level agreement performance."
    )

    st.markdown("---")

    vulnerabilities = pd.DataFrame(
        [
            [
                "VULN-001",
                "Remote code execution in internet-facing server",
                "Critical",
                9.8,
                "Web Server 01",
                "Infrastructure",
                "Open",
                "Overdue",
                "2026-06-28",
            ],
            [
                "VULN-002",
                "Outdated OpenSSL package",
                "High",
                8.1,
                "Application Server 04",
                "Platform Engineering",
                "In Progress",
                "On Track",
                "2026-07-12",
            ],
            [
                "VULN-003",
                "Unsupported operating system version",
                "High",
                7.8,
                "Finance Workstation 17",
                "Endpoint Team",
                "Open",
                "Overdue",
                "2026-07-03",
            ],
            [
                "VULN-004",
                "Weak TLS configuration",
                "Medium",
                6.4,
                "Customer Portal",
                "Application Security",
                "In Progress",
                "On Track",
                "2026-07-18",
            ],
            [
                "VULN-005",
                "Missing endpoint security agent",
                "Medium",
                5.9,
                "Operations Laptop 22",
                "Endpoint Team",
                "Open",
                "On Track",
                "2026-07-20",
            ],
            [
                "VULN-006",
                "Default administrative credential detected",
                "Critical",
                9.1,
                "Network Appliance 03",
                "Network Security",
                "In Progress",
                "Overdue",
                "2026-07-01",
            ],
            [
                "VULN-007",
                "Unnecessary service enabled",
                "Low",
                3.2,
                "Development Server 08",
                "DevOps",
                "Accepted",
                "Within SLA",
                "2026-08-02",
            ],
            [
                "VULN-008",
                "Missing security headers",
                "Medium",
                5.4,
                "Vendor Portal",
                "Application Security",
                "Resolved",
                "Within SLA",
                "2026-07-08",
            ],
        ],
        columns=[
            "Vulnerability ID",
            "Finding",
            "Severity",
            "CVSS Score",
            "Affected Asset",
            "Owner",
            "Status",
            "SLA Status",
            "Target Date",
        ],
    )

    total_vulnerabilities = len(vulnerabilities)

    critical_vulnerabilities = len(
        vulnerabilities[
            vulnerabilities["Severity"] == "Critical"
        ]
    )

    overdue_vulnerabilities = len(
        vulnerabilities[
            vulnerabilities["SLA Status"] == "Overdue"
        ]
    )

    resolved_vulnerabilities = len(
        vulnerabilities[
            vulnerabilities["Status"] == "Resolved"
        ]
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        kpi_card(
            "Total Vulnerabilities",
            total_vulnerabilities,
            "Current vulnerability inventory",
        )

    with col2:
        kpi_card(
            "Critical Findings",
            critical_vulnerabilities,
            "Require immediate remediation",
        )

    with col3:
        kpi_card(
            "Overdue SLA",
            overdue_vulnerabilities,
            "Past remediation deadline",
        )

    with col4:
        kpi_card(
            "Resolved",
            resolved_vulnerabilities,
            "Closed vulnerability findings",
        )

    st.markdown("---")

    # -----------------------------
    # Horizontal Severity Chart
    # -----------------------------

    st.subheader("Severity Distribution")

    severity_order = [
        "Critical",
        "High",
        "Medium",
        "Low",
    ]

    severity_summary = (
        vulnerabilities.groupby("Severity")
        .size()
        .reindex(
            severity_order,
            fill_value=0,
        )
        .reset_index(name="Count")
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
        x="Count",
        y="Severity",
        orientation="h",
        color="Severity",
        text="Count",
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
            "Vulnerabilities: %{x}"
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
        xaxis_title="Vulnerability count",
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
    # Vulnerability Register
    # -----------------------------

    st.subheader("Vulnerability Register")

    filter_col1, filter_col2 = st.columns(2)

    with filter_col1:
        selected_severity = st.selectbox(
            "Filter by Severity",
            [
                "All",
                *severity_order,
            ],
        )

    with filter_col2:
        selected_status = st.selectbox(
            "Filter by Status",
            [
                "All",
                *sorted(
                    vulnerabilities["Status"]
                    .unique()
                    .tolist()
                ),
            ],
        )

    filtered_vulnerabilities = vulnerabilities.copy()

    if selected_severity != "All":
        filtered_vulnerabilities = filtered_vulnerabilities[
            filtered_vulnerabilities["Severity"]
            == selected_severity
        ]

    if selected_status != "All":
        filtered_vulnerabilities = filtered_vulnerabilities[
            filtered_vulnerabilities["Status"]
            == selected_status
        ]

    st.dataframe(
        filtered_vulnerabilities,
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
The current vulnerability backlog includes two critical findings and three items that have exceeded remediation service-level agreements.

The highest-priority exposures involve an internet-facing server and a network appliance with a default administrative credential.

Recommended Actions:

• Escalate VULN-001 and VULN-006 for immediate remediation

• Require accountable owners to provide recovery dates for overdue findings

• Validate compensating controls for any accepted vulnerabilities

• Review vulnerability SLA performance during the next risk committee meeting
"""
    )