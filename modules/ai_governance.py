import streamlit as st
import pandas as pd

from modules.ui_components import kpi_card


def show_ai_governance():
    st.title("AI Governance")

    st.caption(
        "Monitor enterprise AI models, validation status, ownership, and governance risk."
    )

    st.markdown("---")

    models = pd.DataFrame(
        [
            ["Credit Risk Model", "Finance", "Data Science", "High", "Validated", "2026-06-12"],
            ["Customer Support Chatbot", "Customer Service", "AI Engineering", "Medium", "Review Required", "2026-05-30"],
            ["Vendor Risk Classifier", "Procurement", "Cybersecurity", "Low", "Validated", "2026-06-20"],
            ["Fraud Detection Model", "Finance", "Machine Learning", "Critical", "Pending Approval", "2026-04-18"],
        ],
        columns=[
            "Model",
            "Business Unit",
            "Owner",
            "Risk",
            "Status",
            "Last Review",
        ],
    )

    total_models = len(models)
    validated_models = len(models[models["Status"] == "Validated"])
    pending_models = len(models[models["Status"].isin(["Review Required", "Pending Approval"])])
    critical_models = len(models[models["Risk"] == "Critical"])

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        kpi_card("AI Models", total_models, "Enterprise AI inventory")

    with col2:
        kpi_card("Validated", validated_models, "Models approved for use")

    with col3:
        kpi_card("Pending Review", pending_models, "Awaiting governance review")

    with col4:
        kpi_card("Critical Models", critical_models, "High-impact AI systems")

    st.markdown("---")

    st.subheader("Enterprise AI Model Inventory")

    st.dataframe(
        models,
        use_container_width=True,
        hide_index=True,
    )

    st.markdown("---")

    st.subheader("Executive Insight")

    st.info(
        """
One critical AI model is currently awaiting executive approval.

The Customer Support Chatbot requires governance review before the next production release.

Recommendation:

• Complete Fraud Detection Model approval

• Schedule chatbot governance review

• Perform bias and validation assessment
"""
    )