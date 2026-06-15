# 🤖 Agentic AI Career Copilot

An AI-powered career guidance platform that analyzes resumes, provides ATS scoring, generates interview questions, and creates personalized career roadmaps using Google's Gemini AI.

## 🚀 Live Demo

🔗 Live Application: https://agentic-ai-career-copilot-9tuuetrpyetovflrbjumew.streamlit.app/

## 📌 Overview

Agentic AI Career Copilot is designed to help students, freshers, and job seekers evaluate their resumes and prepare for their desired career paths.

The application leverages Large Language Models (LLMs) through Gemini AI to provide intelligent career guidance by analyzing uploaded resumes against target job roles.

## ✨ Features

### 📄 Resume Analysis

* Extracts and analyzes resume content from PDF files.
* Identifies strengths and weaknesses.
* Highlights missing skills and improvement areas.

### 📊 ATS Score Analysis

* Estimates resume compatibility with target job roles.
* Suggests relevant keywords and resume enhancements.
* Helps improve Applicant Tracking System (ATS) performance.

### 🎤 Interview Preparation

* Generates HR interview questions.
* Creates role-specific technical questions.
* Provides situational and behavioral interview questions.

### 🛣 Personalized Career Roadmap

* Performs skill-gap analysis.
* Recommends learning paths.
* Suggests certifications and upskilling opportunities.
* Generates a structured career transition roadmap.

### 🔒 Privacy Focused

* Resumes are processed only for analysis purposes.
* No permanent storage of uploaded resumes.
* User data is not stored in any database.

## 🏗 Architecture

User Resume Upload
↓
PDF Text Extraction
↓
Agentic AI Career Copilot
↓
Gemini AI Analysis
↓
ATS Analysis + Resume Review
↓
Interview Questions + Career Roadmap

## 🛠 Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI & NLP

* Google Gemini API
* Prompt Engineering

### Document Processing

* PyPDF

### Deployment

* Streamlit Community Cloud

## 📂 Project Structure

agentic-ai-career-copilot/

├── app.py

├── agents/

│   └── master_agent.py

├── utils/

│   └── pdf_reader.py

├── requirements.txt

├── .gitignore

└── README.md

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Sk7483/agentic-ai-career-copilot.git
```

Navigate to project folder:

```bash
cd agentic-ai-career-copilot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a .env file:

```env
GEMINI_API_KEY=your_api_key
```

Run the application:

```bash
streamlit run app.py
```

## 🎯 Use Cases

* Students preparing for placements
* Freshers applying for jobs
* Career switchers
* Professionals seeking resume feedback
* Interview preparation assistance

## 📈 Future Enhancements

* Multi-agent architecture using CrewAI
* Resume comparison against job descriptions
* PDF report generation
* Skill-gap visualization dashboard
* Career trend analysis
* Job recommendation engine

## 👨‍💻 Author

Mallikarjun S K

Artificial Intelligence & Data Science Engineer

GitHub: https://github.com/Sk7483

LinkedIn: (https://www.linkedin.com/in/mallikarjun7483/)

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.

