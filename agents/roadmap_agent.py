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

def create_roadmap(resume_text,role):

    prompt = f"""
Candidate Resume:
{resume_text}

Target Role:
{role}

Create a realistic roadmap.

Consider:

- Current skills
- Existing experience
- Skill gaps

Provide:

1. Current Position
2. Skill Gap Analysis
3. Recommended Career Path
4. 12 Week Learning Plan
5. Certifications
6. Projects to Build

Do not assume prior experience.
"""

    response = model.generate_content(
        prompt
    )

    return response.text