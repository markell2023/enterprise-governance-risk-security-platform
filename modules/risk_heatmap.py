import streamlit as st
import plotly.graph_objects as go


def show_risk_heatmap(df):
    likelihood_map = {
        "Low": 1,
        "Medium": 2,
        "High": 3,
    }

    impact_map = {
        "Medium": 2,
        "High": 3,
        "Critical": 4,
    }

    heatmap_df = df.copy()
    heatmap_df["Likelihood Score"] = heatmap_df["Likelihood"].map(likelihood_map)
    heatmap_df["Impact Score"] = heatmap_df["Impact"].map(impact_map)

    risk_matrix = [
        [6, 9, 12],
        [9, 12, 16],
        [12, 16, 20],
    ]

    fig = go.Figure()

    fig.add_trace(
        go.Heatmap(
            z=risk_matrix,
            x=["Medium", "High", "Critical"],
            y=["Low", "Medium", "High"],
            colorscale=[
                [0.00, "#22C55E"],
                [0.40, "#F59E0B"],
                [0.70, "#EF4444"],
                [1.00, "#991B1B"],
            ],
            showscale=True,
            colorbar=dict(title="Risk Level"),
        )
    )

    fig.add_trace(
        go.Scatter(
            x=heatmap_df["Impact"],
            y=heatmap_df["Likelihood"],
            mode="markers+text",
            text=heatmap_df["Risk ID"],
            textposition="middle center",
            marker=dict(
                size=42,
                color="#111827",
                line=dict(color="#F8FAFC", width=2),
            ),
            hovertext=heatmap_df["Risk Name"],
            hoverinfo="text",
        )
    )

    fig.update_layout(
        title="Enterprise Risk Heat Map",
        xaxis_title="Impact",
        yaxis_title="Likelihood",
        height=600,
        paper_bgcolor="#121212",
        plot_bgcolor="#181818",
        font=dict(color="#F8FAFC"),
    )

    st.plotly_chart(fig, use_container_width=True)