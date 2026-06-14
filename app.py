import streamlit as st
import re

from utils.pdf_reader import extract_text
from agents.master_agent import run_career_copilot

# -------------------------

# PAGE CONFIG

# -------------------------

st.set_page_config(
page_title="Agentic AI Career Copilot",
page_icon="🤖",
layout="wide"
)

# -------------------------

# SIDEBAR

# -------------------------

with st.sidebar:

    st.title("🤖 Career Copilot")

    st.markdown("---")

    st.markdown("""
### Navigation

📄 Resume Analysis

📊 ATS Analysis

🎤 Interview Prep

🛣 Career Roadmap
""")

    st.markdown("---")

    st.caption(
        "Built with Gemini AI + Streamlit"
    )


# -------------------------

# HEADER

# -------------------------

st.title("🤖 Agentic AI Career Copilot")

st.markdown(
"""
### AI-Powered Resume Analyzer & Career Coach

Upload your resume and receive:

✅ ATS Score

✅ Resume Feedback

✅ Interview Questions

✅ Personalized Learning Roadmap

"""
)

# -------------------------

# INPUTS

# -------------------------

uploaded_file = st.file_uploader(
"📄 Upload Resume",
type=["pdf"]
)

role = st.text_input(
"🎯 Target Role",
value="AI Engineer"
)

# -------------------------

# RUN AGENT

# -------------------------

if uploaded_file is not None:


    st.success("✅ Resume uploaded successfully!")

if st.button(
    "🚀 Run Agents",
    use_container_width=True
):

    resume_text = extract_text(
        uploaded_file
    )

    with st.spinner(
        "🤖 AI Agent is analyzing your profile..."
    ):

        result = run_career_copilot(
            resume_text,
            role
        )
    if result.startswith("Error:"):
        st.error(result)
        st.stop()    

    st.success("✅ Analysis Complete!")

    # -------------------------
    # ATS SCORE CARD
    # -------------------------

    score = 0

    match = re.search(
    r'ATS Score.*?(\d+)',
    result,
    re.IGNORECASE
)

    if match:
        score = int(match.group(1))

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "ATS Score",
            f"{score}/100"
        )

    with col2:
        st.metric(
            "Target Role",
            role
        )

    st.progress(
        score / 100 if score > 0 else 0
    )

    st.markdown("---")


    # -------------------------
    # TABS
    # -------------------------

    st.info(
    f"🎯 Target Role: {role}"
)

    st.markdown("---")

    with st.expander(
    "📋 Complete AI Analysis",
    expanded=True
):
     st.markdown(result)

    st.markdown("---")

    st.download_button(
    label="📥 Download Report",
    data=result,
    file_name="career_report.txt",
    mime="text/plain"
)


else:
 
 st.info(
    "📄 Upload a resume PDF to begin analysis."
)





