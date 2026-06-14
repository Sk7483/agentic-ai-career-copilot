import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    api_key = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def run_career_copilot(
    resume_text,
    target_role
):

    prompt = f"""
You are an expert AI Career Coach.

Candidate Resume:

{resume_text}

Target Role:

{target_role}

Perform the following analysis.

=========================
ATS ANALYSIS
=========================

Provide:

- ATS Score (0-100)
- Missing Keywords
- Resume Improvements

=========================
RESUME ANALYSIS
=========================

Provide:

- Match Score (0-100)
- Strengths
- Weaknesses
- Missing Skills

=========================
INTERVIEW QUESTIONS
=========================

Provide:

- 5 HR Questions
- 5 Role Specific Questions
- 5 Situational Questions

=========================
CAREER ROADMAP
=========================

Provide:

- Current Position
- Skill Gap Analysis
- Career Transition Path
- 12 Week Learning Plan
- Recommended Certifications

Return the response EXACTLY in this format.

# ATS ANALYSIS

ATS Score: X/100

Missing Keywords:
- item
- item

Resume Improvements:
- item
- item

# RESUME ANALYSIS

Match Score: X/100

Strengths:
- item
- item

Weaknesses:
- item
- item

Missing Skills:
- item
- item

# INTERVIEW QUESTIONS

HR Questions:
1.
2.
3.
4.
5.

Role Specific Questions:
1.
2.
3.
4.
5.

Situational Questions:
1.
2.
3.
4.
5.

# CAREER ROADMAP

Current Position:

Skill Gap Analysis:

Career Transition Path:

12 Week Learning Plan:

Recommended Certifications:
- item
- item

Keep the response concise and recruiter-friendly.
"""

    try:

        response = model.generate_content(
            prompt
        )

        return response.text

    except Exception as e:

        return f"Error: {str(e)}"