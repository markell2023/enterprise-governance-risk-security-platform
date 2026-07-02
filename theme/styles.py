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

/* ---------- APP ---------- */

.stApp {{
    background-color: {BACKGROUND};
    color: {TEXT_PRIMARY};
}}

/* ---------- SIDEBAR ---------- */

section[data-testid="stSidebar"] {{
    background-color: {SIDEBAR};
}}

/* ---------- HEADINGS ---------- */

.main-title {{
    font-size: 2.4rem;
    font-weight: 700;
    color: {TEXT_PRIMARY};
    margin-bottom: 0.2rem;
}}

.subtitle {{
    color: {TEXT_SECONDARY};
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

</style>
"""