import streamlit as st


def show_executive_intelligence():

    st.subheader("Executive Intelligence Brief")

    st.info(
        """
Enterprise risk remains **Moderate** this reporting period.

Two enterprise risks currently exceed organizational tolerance and require executive attention.

Cybersecurity posture has improved following privileged access remediation, while Vendor Risk continues to trend upward because of overdue third-party assurance documentation.
"""
    )

    st.markdown("---")

    left, right = st.columns([2, 1])

    with left:

        st.markdown("### Executive Actions")

        st.error("Approve Vendor Remediation Plan")

        st.warning("Review Disaster Recovery Exercise")

        st.success("Complete AI Governance Review")

        st.error("Review Privileged Access Controls")

    with right:

        st.markdown("### Upcoming Deadlines")

        st.write("📅 July 10")
        st.caption("Vendor Review")

        st.write("📅 July 14")
        st.caption("Internal Audit")

        st.write("📅 July 21")
        st.caption("Board Risk Committee")