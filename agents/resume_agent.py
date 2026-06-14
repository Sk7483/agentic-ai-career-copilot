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

def analyze_resume(resume_text, target_role):

    prompt = f"""
You are an expert career coach.

Candidate Resume:
{resume_text}

Target Role:
{target_role}

Analyze the resume specifically for the target role.

Provide:

1. Resume Match Score (0-100)

2. Relevant Skills for the Target Role

3. Transferable Skills

4. Missing Skills Required for the Target Role

5. Strengths for this Target Role

6. Weaknesses for this Target Role

7. Suggestions to improve chances of getting hired for this Target Role

Be strict and realistic.
"""

    response = model.generate_content(
        prompt
    )

    return response.text