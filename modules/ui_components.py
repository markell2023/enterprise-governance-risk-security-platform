import streamlit as st


def kpi_card(title, value, subtitle):
    st.markdown(
        f"""
<div style="background-color:#1E1E1E; border:1px solid #2D2D2D; border-radius:16px; padding:20px; min-height:115px;">
    <div style="color:#94A3B8; font-size:0.85rem; font-weight:500; margin-bottom:8px;">
        {title}
    </div>
    <div style="color:#F8FAFC; font-size:2rem; font-weight:800; margin-bottom:6px;">
        {value}
    </div>
    <div style="color:#64748B; font-size:0.8rem; font-weight:400;">
        {subtitle}
    </div>
</div>
""",
        unsafe_allow_html=True,
    )