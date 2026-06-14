import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def ats_analysis(resume_text, target_role):

    prompt = f"""
    Resume:
    {resume_text}

    Target Role:
    {target_role}

    Analyze ATS compatibility.

    Provide:

    1. ATS Score (0-100)

    2. Missing Keywords

    3. Resume Improvements

    4. Suggested Skills

    5. Recruiter Impression
    """

    response = model.generate_content(
        prompt
    )

    return response.text