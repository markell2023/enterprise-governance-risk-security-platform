"""
Enterprise Governance, Risk & Security Platform
Global Theme
"""

from theme.colors import *


def load_theme():
    return f"""
<style>

/* Import Professional Font */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* ---------- GLOBAL ---------- */

html, body, [class*="css"] {{
    font-family: 'Inter', sans-serif;
}}

p,
span,
label,
div {{
    color: #CBD5E1;
}}

/* ---------- APP ---------- */

.stApp {{
    background-color: {BACKGROUND};
    color: {TEXT_PRIMARY};
}}

/* ---------- SIDEBAR ---------- */

section[data-testid="stSidebar"] {{
    background-color: {SIDEBAR};
}}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] strong {{
    color: #F8FAFC !important;
}}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] div {{
    color: #CBD5E1 !important;
}}

section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] {{
    color: #94A3B8 !important;
}}

section[data-testid="stSidebar"] [role="radiogroup"] label {{
    color: #CBD5E1 !important;
}}

section[data-testid="stSidebar"] [role="radiogroup"] label:hover {{
    color: #F8FAFC !important;
}}

/* ---------- HEADINGS ---------- */

.main-title {{
    font-size: 2.4rem;
    font-weight: 700;
    color: {TEXT_PRIMARY};
    margin-bottom: 0.2rem;
}}

.subtitle {{
    color: #CBD5E1;
    font-size: 1rem;
    margin-bottom: 2rem;
}}

/* ---------- SECTION TITLES ---------- */

.section-title {{
    color: {TEXT_PRIMARY};
    font-size: 1.4rem;
    font-weight: 600;
    margin-top: 2rem;
    margin-bottom: 1rem;
}}

/* ---------- STREAMLIT TEXT ---------- */

[data-testid="stMarkdownContainer"] p {{
    color: #CBD5E1;
}}

[data-testid="stCaptionContainer"] {{
    color: #94A3B8 !important;
}}

/* ---------- INPUT LABELS ---------- */

label[data-testid="stWidgetLabel"] p {{
    color: #CBD5E1 !important;
}}

/* ---------- DATAFRAME TEXT ---------- */

[data-testid="stDataFrame"] {{
    color: #111827;
}}

/* ---------- FOOTER TEXT ---------- */

footer {{
    color: #94A3B8;
}}

</style>
"""