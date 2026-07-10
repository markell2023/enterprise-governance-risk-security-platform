import pandas as pd
import plotly.express as px
import streamlit as st

from modules.ui_components import kpi_card


def show_compliance():
    st.title("Compliance Center")

    st.caption(
        "Track control implementation, evidence status, framework coverage, "
        "and audit readiness."
    )

    st.markdown("---")

    controls = pd.DataFrame(
        [
            [
                "NIST CSF",
                "PR.AA-01",
                "Identity and access permissions are managed",
                "Implemented",
                "Current",
                "Identity & Access Management",
                "2026-06-18",
            ],
            [
                "NIST CSF",
                "DE.CM-01",
                "Networks and network services are monitored",
                "Implemented",
                "Current",
                "Security Operations",
                "2026-06-21",
            ],
            [
                "ISO 27001",
                "A.5.15",
                "Access control",
                "Partially Implemented",
                "Needs Update",
                "Corporate IT",
                "2026-05-30",
            ],
            [
                "ISO 27001",
                "A.5.24",
                "Information security incident management planning",
                "Implemented",
                "Current",
                "Information Security",
                "2026-06-11",
            ],
            [
                "CIS Controls",
                "CIS 4",
                "Secure configuration of enterprise assets",
                "Implemented",
                "Current",
                "Infrastructure",
                "2026-06-07",
            ],
            [
                "CIS Controls",
                "CIS 5",
                "Account management",
                "Partially Implemented",
                "Current",
                "Identity & Access Management",
                "2026-06-09",
            ],
            [
                "CIS Controls",
                "CIS 7",
                "Continuous vulnerability management",
                "Partially Implemented",
                "Needs Update",
                "Vulnerability Management",
                "2026-05-15",
            ],
            [
                "CIS Controls",
                "CIS 8",
                "Audit log management",
                "Not Implemented",
                "Missing",
                "Security Engineering",
                "2026-04-28",
            ],
            [
                "SOC 2",
                "CC6.1",
                "Logical and physical access controls",
                "Implemented",
                "Current",
                "Compliance",
                "2026-06-19",
            ],
            [
                "SOC 2",
                "CC7.2",
                "Security event monitoring",
                "Partially Implemented",
                "Needs Update",
                "Security Operations",
                "2026-05-22",
            ],
        ],
        columns=[
            "Framework",
            "Control ID",
            "Control",
            "Implementation Status",
            "Evidence Status",
            "Owner",
            "Last Review",
        ],
    )

    total_controls = len(controls)

    implemented_controls = len(
        controls[
            controls["Implementation Status"] == "Implemented"
        ]
    )

    open_gaps = len(
        controls[
            controls["Implementation Status"].isin(
                [
                    "Partially Implemented",
                    "Not Implemented",
                ]
            )
        ]
    )

    evidence_ready = len(
        controls[
            controls["Evidence Status"] == "Current"
        ]
    )

    compliance_score = round(
        (implemented_controls / total_controls) * 100
    )

    framework_summary = (
        controls.groupby("Framework")
        .agg(
            Controls=("Control ID", "count"),
            Implemented=(
                "Implementation Status",
                lambda values: (
                    values == "Implemented"
                ).sum(),
            ),
            Open_Gaps=(
                "Implementation Status",
                lambda values: values.isin(
                    [
                        "Partially Implemented",
                        "Not Implemented",
                    ]
                ).sum(),
            ),
        )
        .reset_index()
    )

    framework_summary["Coverage"] = (
        framework_summary["Implemented"]
        / framework_summary["Controls"]
        * 100
    ).round(0)

    framework_summary = framework_summary.sort_values(
        "Coverage",
        ascending=True,
    )

    # -----------------------------
    # Framework Coverage Chart
    # -----------------------------

    st.subheader("Framework Coverage")

    coverage_chart = px.bar(
        framework_summary,
        x="Coverage",
        y="Framework",
        orientation="h",
        color="Framework",
        text="Coverage",
        custom_data=[
            "Controls",
            "Implemented",
            "Open_Gaps",
        ],
        range_x=[0, 105],
        color_discrete_map={
            "NIST CSF": "#2563EB",
            "ISO 27001": "#10B981",
            "SOC 2": "#8B5CF6",
            "CIS Controls": "#F59E0B",
        },
    )

    coverage_chart.update_traces(
        texttemplate="%{text:.0f}%",
        textposition="outside",
        cliponaxis=False,
        hovertemplate=(
            "<b>%{y}</b><br>"
            "Coverage: %{x:.0f}%<br>"
            "Controls assessed: %{customdata[0]}<br>"
            "Implemented: %{customdata[1]}<br>"
            "Open gaps: %{customdata[2]}"
            "<extra></extra>"
        ),
    )

    coverage_chart.update_layout(
        height=420,
        margin=dict(
            l=10,
            r=55,
            t=10,
            b=10,
        ),
        xaxis_title="Control coverage",
        yaxis_title="",
        xaxis=dict(
            range=[0, 105],
            ticksuffix="%",
            showgrid=True,
            gridcolor="#2D2D2D",
            zeroline=False,
        ),
        yaxis=dict(
            categoryorder="array",
            categoryarray=framework_summary[
                "Framework"
            ].tolist(),
        ),
        paper_bgcolor="#121212",
        plot_bgcolor="#121212",
        font=dict(
            color="#F8FAFC",
        ),
        showlegend=False,
    )

    st.plotly_chart(
        coverage_chart,
        use_container_width=True,
        config={
            "displayModeBar": False,
        },
    )

    with st.expander("View framework coverage table"):
        st.dataframe(
            framework_summary,
            use_container_width=True,
            hide_index=True,
        )

    st.markdown("---")

    # -----------------------------
    # KPI Cards
    # -----------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        kpi_card(
            "Compliance Score",
            f"{compliance_score}%",
            "Implemented controls across frameworks",
        )

    with col2:
        kpi_card(
            "Controls Assessed",
            total_controls,
            "Current control inventory",
        )

    with col3:
        kpi_card(
            "Open Gaps",
            open_gaps,
            "Require remediation or review",
        )

    with col4:
        kpi_card(
            "Evidence Ready",
            evidence_ready,
            "Controls with current evidence",
        )

    st.markdown("---")

    # -----------------------------
    # Control Register
    # -----------------------------

    st.subheader("Control Register")

    selected_framework = st.selectbox(
        "Filter by Framework",
        [
            "All",
            *sorted(
                controls["Framework"]
                .unique()
                .tolist()
            ),
        ],
    )

    filtered_controls = controls.copy()

    if selected_framework != "All":
        filtered_controls = filtered_controls[
            filtered_controls["Framework"]
            == selected_framework
        ]

    st.dataframe(
        filtered_controls,
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
Compliance readiness is currently moderate.

Five controls remain partially implemented or not implemented. The largest concentration of gaps is within CIS Controls, including account management, vulnerability management, and audit logging.

NIST CSF currently has the strongest implementation coverage, while ISO 27001 and SOC 2 each remain at 50%.

Recommended Actions:

• Remediate the CIS Control 8 audit logging gap

• Complete implementation of continuous vulnerability management

• Refresh evidence for access control and security monitoring

• Assign target completion dates for partially implemented controls
"""
    )