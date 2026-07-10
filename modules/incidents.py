import pandas as pd
import plotly.express as px
import streamlit as st

from modules.ui_components import kpi_card


def show_incidents():
    st.title("Incident Management")

    st.caption(
        "Track security incidents, severity, response ownership, containment, "
        "and resolution performance."
    )

    st.markdown("---")

    incidents = pd.DataFrame(
        [
            [
                "INC-001",
                "Phishing campaign targeting finance employees",
                "Critical",
                "Active",
                "Security Operations",
                "Email Security",
                "Contained",
                "2026-07-10",
                "2026-07-10",
            ],
            [
                "INC-002",
                "Unauthorized administrative login attempts",
                "High",
                "Investigating",
                "Identity & Access Management",
                "Credential Access",
                "In Progress",
                "2026-07-09",
                "2026-07-11",
            ],
            [
                "INC-003",
                "Malware detected on corporate endpoint",
                "High",
                "Contained",
                "Endpoint Security",
                "Execution",
                "Complete",
                "2026-07-08",
                "2026-07-09",
            ],
            [
                "INC-004",
                "Suspicious PowerShell execution",
                "Medium",
                "Monitoring",
                "Security Operations",
                "Execution",
                "In Progress",
                "2026-07-08",
                "2026-07-12",
            ],
            [
                "INC-005",
                "Impossible travel alert",
                "Medium",
                "Resolved",
                "Identity Team",
                "Initial Access",
                "Complete",
                "2026-07-07",
                "2026-07-07",
            ],
            [
                "INC-006",
                "USB device connected to restricted workstation",
                "Low",
                "Resolved",
                "Endpoint Team",
                "Collection",
                "Complete",
                "2026-07-06",
                "2026-07-06",
            ],
            [
                "INC-007",
                "Cloud storage bucket exposed publicly",
                "Critical",
                "Investigating",
                "Cloud Security",
                "Exfiltration",
                "In Progress",
                "2026-07-10",
                "2026-07-10",
            ],
        ],
        columns=[
            "Incident ID",
            "Incident",
            "Severity",
            "Status",
            "Owner",
            "MITRE Tactic",
            "Containment",
            "Detected Date",
            "Target Resolution",
        ],
    )

    total_incidents = len(incidents)

    active_incidents = len(
        incidents[
            incidents["Status"].isin(
                ["Active", "Investigating", "Monitoring"]
            )
        ]
    )

    critical_incidents = len(
        incidents[
            incidents["Severity"] == "Critical"
        ]
    )

    contained_incidents = len(
        incidents[
            incidents["Containment"].isin(
                ["Contained", "Complete"]
            )
        ]
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        kpi_card(
            "Total Incidents",
            total_incidents,
            "Current incident inventory",
        )

    with col2:
        kpi_card(
            "Active Incidents",
            active_incidents,
            "Require ongoing response",
        )

    with col3:
        kpi_card(
            "Critical Incidents",
            critical_incidents,
            "Immediate leadership attention",
        )

    with col4:
        kpi_card(
            "Contained",
            contained_incidents,
            "Contained or fully resolved",
        )

    st.markdown("---")

    st.subheader("Incident Severity Distribution")

    severity_order = [
        "Critical",
        "High",
        "Medium",
        "Low",
    ]

    severity_summary = (
        incidents.groupby("Severity")
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
            "Incidents: %{x}"
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
        xaxis_title="Incident count",
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

    st.subheader("Incident Register")

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
                    incidents["Status"]
                    .unique()
                    .tolist()
                ),
            ],
        )

    filtered_incidents = incidents.copy()

    if selected_severity != "All":
        filtered_incidents = filtered_incidents[
            filtered_incidents["Severity"]
            == selected_severity
        ]

    if selected_status != "All":
        filtered_incidents = filtered_incidents[
            filtered_incidents["Status"]
            == selected_status
        ]

    st.dataframe(
        filtered_incidents,
        use_container_width=True,
        hide_index=True,
    )

    st.markdown("---")

    st.subheader("Executive Insight")

    st.info(
        """
Two critical incidents currently require executive visibility: an active phishing campaign and a publicly exposed cloud storage bucket.

Containment activity is progressing, but identity-related investigations and cloud remediation remain open.

Recommended Actions:

• Escalate INC-001 and INC-007 for immediate response oversight

• Validate credential resets and access reviews for affected users

• Confirm public cloud exposure has been removed and independently verified

• Review incident response performance during the next security leadership meeting
"""
    )