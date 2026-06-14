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

def generate_questions(resume_text,target_role):

    prompt = f"""
Candidate Resume:
{resume_text}

Target Role:
{target_role}

Generate interview questions specifically for this target role.

Rules:

1. If target role matches resume domain,
   ask technical questions.

2. If target role is different,
   ask role-transition questions.

Provide:

- 5 HR Questions
- 5 Role-Specific Questions
- 5 Situational Questions

Be realistic.
"""

    response = model.generate_content(
        prompt
    )

    return response.text