import streamlit as st
import time
import os
import tempfile
import re

from pypdf import PdfReader
from docx import Document
from utils.pdf_export import generate_pdf, build_summary

# =================================================
# PAGE CONFIGURATION
# =================================================

st.set_page_config(
    page_title="AI Legal Assistant",
    page_icon="⚔️",
    layout="wide"
)

# =================================================
# BLUE × GREEN UI THEME
# =================================================

st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden;}

.stApp {
    background: linear-gradient(135deg, #0b1f33, #041624);
    color: #e6f6ff;
    font-family: 'Inter', sans-serif;
}

.page-title {
    font-size: 2.8rem;
    font-weight: 800;
    background: linear-gradient(90deg, #38bdf8, #22c55e);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.page-subtitle {
    color: #9ddcff;
    margin-bottom: 1.8rem;
}

.section-title {
    font-size: 1.4rem;
    font-weight: 700;
    color: #e0f7ff;
    margin-bottom: 0.8rem;
}

.risk-low { color: #22c55e; font-weight: 700; }
.risk-medium { color: #facc15; font-weight: 700; }
.risk-high { color: #ef4444; font-weight: 700; }

.stButton > button {
    background: linear-gradient(135deg, #38bdf8, #22c55e);
    color: #022c22;
    font-weight: 700;
    border-radius: 14px;
    padding: 0.65rem 1.4rem;
}

.small-text {
    color: #9ddcff;
    font-size: 0.85rem;
}

.streamlit-expanderHeader {
    font-weight: 600;
    color: #e0f7ff;
}
</style>
""", unsafe_allow_html=True)

# =================================================
# UTILITY FUNCTIONS (UNCHANGED)
# =================================================

def extract_text(uploaded_file):
    suffix = os.path.splitext(uploaded_file.name)[1].lower()

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded_file.getvalue())
        tmp_path = tmp.name

    text = ""
    if suffix == ".pdf":
        reader = PdfReader(tmp_path)
        for page in reader.pages[:5]:
            text += page.extract_text() or ""
    elif suffix == ".docx":
        doc = Document(tmp_path)
        text = " ".join(p.text for p in doc.paragraphs)
    elif suffix == ".txt":
        text = uploaded_file.getvalue().decode("utf-8")

    os.remove(tmp_path)
    return text.lower()


def analyze_contract(text):
    high_risk, medium_risk = [], []

    if "terminate" in text and "without notice" in text:
        high_risk.append("Termination allowed without notice")
    if "indemnify" in text or "indemnity" in text:
        high_risk.append("Unlimited indemnity obligation")
    if "auto-renew" in text or "automatically renew" in text:
        medium_risk.append("Auto-renewal clause present")

    if not high_risk and not medium_risk:
        return "LOW", [], []
    if high_risk:
        return "HIGH", high_risk, medium_risk
    return "MEDIUM", high_risk, medium_risk


def detect_contract_type(text):
    if "employment" in text or "employee" in text:
        return "Employment Agreement"
    if "vendor" in text or "supplier" in text:
        return "Vendor Agreement"
    if "lease" in text or "rent" in text:
        return "Lease Agreement"
    if "service" in text or "scope of work" in text:
        return "Service Contract"
    if "partnership" in text:
        return "Partnership Deed"
    return "General / Unknown Contract"


def extract_clauses(text):
    raw = re.split(r'\n\s*\d+[\.\)]|\n[A-Z][A-Za-z ]{3,}:', text)
    return [c.strip() for c in raw if len(c.strip()) > 80][:15]


def explain_clause_plainly(clause):
    clause = clause.lower()
    if "terminate" in clause:
        return "Explains how and when the contract can be ended."
    if "indemnify" in clause:
        return "Transfers legal and financial liability to one party."
    if "payment" in clause:
        return "Describes payment obligations and timelines."
    if "confidential" in clause:
        return "Restricts sharing of sensitive information."
    if "jurisdiction" in clause:
        return "Specifies which country’s laws apply."
    return "Defines general rights and responsibilities."

# =================================================
# MAIN INTERFACE
# =================================================

st.markdown("<div class='page-title'>Contract Analysis Dashboard</div>", unsafe_allow_html=True)
st.markdown("<div class='page-subtitle'>AI Legal Risk Intelligence Platform</div>", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "📤 Upload Contract (PDF / DOCX / TXT)",
    type=["pdf", "docx", "txt"]
)

st.markdown(
    "<div class='small-text'>Files are processed locally. No data is stored.</div>",
    unsafe_allow_html=True
)

if not uploaded_file:
    st.info("Upload a contract to begin analysis.")
    st.stop()

# =================================================
# ANALYSIS FLOW (UNCHANGED)
# =================================================

with st.spinner("Reading contract..."):
    text = extract_text(uploaded_file)
    time.sleep(0.3)

contract_type = detect_contract_type(text)
clauses = extract_clauses(text)

with st.spinner("Analyzing risks..."):
    risk, high_risk, medium_risk = analyze_contract(text)
    time.sleep(0.3)

st.session_state["analysis_result"] = {
    "overall_risk": risk,
    "high_risk_clauses": high_risk,
    "medium_risk_clauses": medium_risk,
    "entities": {"FILE": [uploaded_file.name]}
}

# =================================================
# OVERVIEW
# =================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='section-title'>Contract Type</div>", unsafe_allow_html=True)
    st.write(contract_type)

with col2:
    st.markdown("<div class='section-title'>Overall Risk</div>", unsafe_allow_html=True)
    if risk == "LOW":
        st.markdown("<span class='risk-low'>LOW RISK</span>", unsafe_allow_html=True)
    elif risk == "MEDIUM":
        st.markdown("<span class='risk-medium'>MEDIUM RISK</span>", unsafe_allow_html=True)
    else:
        st.markdown("<span class='risk-high'>HIGH RISK</span>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='section-title'>File Name</div>", unsafe_allow_html=True)
    st.write(uploaded_file.name)

# =================================================
# RISK FINDINGS (UNCHANGED)
# =================================================

st.markdown("<div class='section-title'>⚠️ Risk Findings</div>", unsafe_allow_html=True)

if high_risk:
    st.error("High Risk Clauses")
    for r in high_risk:
        st.write("•", r)

if medium_risk:
    st.warning("Medium Risk Clauses")
    for r in medium_risk:
        st.write("•", r)

if not high_risk and not medium_risk:
    st.success("No significant legal risks detected")

# =================================================
# CLAUSE EXPLANATIONS (UNCHANGED)
# =================================================

st.markdown("<div class='section-title'>📄 Clause Explanations</div>", unsafe_allow_html=True)

for i, clause in enumerate(clauses, 1):
    with st.expander(f"Clause {i}"):
        st.write(clause)
        st.info(explain_clause_plainly(clause))

# =================================================
# PDF EXPORT (FIXED, NO FEATURE LOSS)
# =================================================

st.markdown("<div class='section-title'>📄 Export Legal Summary</div>", unsafe_allow_html=True)

if st.button("Generate PDF"):
    with st.spinner("Generating PDF..."):
        summary_text = build_summary(st.session_state["analysis_result"])
        pdf_path = generate_pdf(summary_text)

    # Handle both return styles safely
    if isinstance(pdf_path, str) and os.path.exists(pdf_path):
        with open(pdf_path, "rb") as f:
            st.download_button(
                label="⬇️ Download Legal Summary (PDF)",
                data=f.read(),
                file_name="legal_summary.pdf",
                mime="application/pdf"
            )
    else:
        st.error("PDF generation failed. Please verify generate_pdf().")
