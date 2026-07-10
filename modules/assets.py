import pandas as pd
import plotly.express as px
import streamlit as st

from modules.ui_components import kpi_card


def show_assets():
    st.title("Asset Inventory")

    st.caption(
        "Track enterprise technology assets, ownership, criticality, lifecycle status, "
        "security classification, and review activity."
    )

    st.markdown("---")

    assets = pd.DataFrame(
        [
            [
                "AST-001",
                "Web Server 01",
                "Server",
                "Infrastructure",
                "Production",
                "Critical",
                "Confidential",
                "Linux",
                "Supported",
                "2026-06-20",
            ],
            [
                "AST-002",
                "Application Server 04",
                "Server",
                "Platform Engineering",
                "Production",
                "High",
                "Confidential",
                "Linux",
                "Supported",
                "2026-06-18",
            ],
            [
                "AST-003",
                "Finance Workstation 17",
                "Workstation",
                "Finance",
                "Corporate",
                "High",
                "Restricted",
                "Windows 10",
                "Unsupported",
                "2026-05-30",
            ],
            [
                "AST-004",
                "Network Appliance 03",
                "Network Device",
                "Network Security",
                "Production",
                "Critical",
                "Confidential",
                "Firmware OS",
                "Supported",
                "2026-06-22",
            ],
            [
                "AST-005",
                "Customer Portal",
                "Application",
                "Application Security",
                "Production",
                "Critical",
                "Restricted",
                "Cloud Hosted",
                "Supported",
                "2026-06-15",
            ],
            [
                "AST-006",
                "Operations Laptop 22",
                "Laptop",
                "Operations",
                "Corporate",
                "Medium",
                "Internal",
                "Windows 11",
                "Supported",
                "2026-06-10",
            ],
            [
                "AST-007",
                "Development Server 08",
                "Server",
                "DevOps",
                "Development",
                "Medium",
                "Internal",
                "Linux",
                "Supported",
                "2026-05-28",
            ],
            [
                "AST-008",
                "Vendor Portal",
                "Application",
                "Third-Party Risk",
                "Production",
                "High",
                "Confidential",
                "Cloud Hosted",
                "Supported",
                "2026-06-12",
            ],
            [
                "AST-009",
                "Legacy File Server",
                "Server",
                "Corporate IT",
                "Corporate",
                "High",
                "Confidential",
                "Windows Server 2012",
                "Unsupported",
                "2026-04-25",
            ],
            [
                "AST-010",
                "Employee Identity Platform",
                "Application",
                "Identity & Access Management",
                "Production",
                "Critical",
                "Restricted",
                "Cloud Hosted",
                "Supported",
                "2026-06-24",
            ],
        ],
        columns=[
            "Asset ID",
            "Asset",
            "Asset Type",
            "Owner",
            "Environment",
            "Criticality",
            "Security Classification",
            "Operating System",
            "Lifecycle Status",
            "Last Security Review",
        ],
    )

    total_assets = len(assets)

    critical_assets = len(
        assets[
            assets["Criticality"] == "Critical"
        ]
    )

    unsupported_assets = len(
        assets[
            assets["Lifecycle Status"] == "Unsupported"
        ]
    )

    restricted_assets = len(
        assets[
            assets["Security Classification"] == "Restricted"
        ]
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        kpi_card(
            "Total Assets",
            total_assets,
            "Current enterprise inventory",
        )

    with col2:
        kpi_card(
            "Critical Assets",
            critical_assets,
            "Business-critical systems",
        )

    with col3:
        kpi_card(
            "Unsupported Assets",
            unsupported_assets,
            "Require lifecycle remediation",
        )

    with col4:
        kpi_card(
            "Restricted Assets",
            restricted_assets,
            "Highest data classification",
        )

    st.markdown("---")

    st.subheader("Asset Type Distribution")

    asset_type_summary = (
        assets.groupby("Asset Type")
        .size()
        .reset_index(name="Count")
        .sort_values("Count", ascending=True)
    )

    asset_type_chart = px.bar(
        asset_type_summary,
        x="Count",
        y="Asset Type",
        orientation="h",
        color="Asset Type",
        text="Count",
    )

    asset_type_chart.update_traces(
        textposition="outside",
        cliponaxis=False,
        hovertemplate=(
            "<b>%{y}</b><br>"
            "Assets: %{x}"
            "<extra></extra>"
        ),
    )

    asset_type_chart.update_layout(
        height=390,
        margin=dict(
            l=10,
            r=40,
            t=10,
            b=10,
        ),
        xaxis_title="Asset count",
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
        asset_type_chart,
        use_container_width=True,
        config={
            "displayModeBar": False,
        },
    )

    st.markdown("---")

    st.subheader("Asset Register")

    filter_col1, filter_col2 = st.columns(2)

    with filter_col1:
        selected_asset_type = st.selectbox(
            "Filter by Asset Type",
            [
                "All",
                *sorted(
                    assets["Asset Type"]
                    .unique()
                    .tolist()
                ),
            ],
        )

    with filter_col2:
        selected_lifecycle = st.selectbox(
            "Filter by Lifecycle Status",
            [
                "All",
                *sorted(
                    assets["Lifecycle Status"]
                    .unique()
                    .tolist()
                ),
            ],
        )

    filtered_assets = assets.copy()

    if selected_asset_type != "All":
        filtered_assets = filtered_assets[
            filtered_assets["Asset Type"]
            == selected_asset_type
        ]

    if selected_lifecycle != "All":
        filtered_assets = filtered_assets[
            filtered_assets["Lifecycle Status"]
            == selected_lifecycle
        ]

    st.dataframe(
        filtered_assets,
        use_container_width=True,
        hide_index=True,
    )

    st.markdown("---")

    st.subheader("Executive Insight")

    st.info(
        """
The current technology inventory includes four critical assets and two unsupported systems.

The Finance Workstation and Legacy File Server require lifecycle remediation because they are operating on unsupported platforms.

Recommended Actions:

• Prioritize replacement of unsupported operating systems

• Confirm compensating controls for unsupported assets until retirement

• Validate ownership and security review dates for all critical assets

• Link critical assets to vulnerability, incident, and risk records
"""
    )