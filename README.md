
# AI Skill-to-Opportunity Translator

An explainable, agent-driven career opportunity mapping system designed to help students and early-career professionals understand how their skills translate into real-world job roles.

This project aligns with the United Nations Sustainable Development Goal 8 (SDG 8): Decent Work and Economic Growth.

---

## Overview

The AI Skill-to-Opportunity Translator is an applied AI system that accepts free-text skill input from users and maps those skills to suitable career roles in a transparent and interpretable manner.  
Unlike traditional career recommendation systems that rely on black-box predictions, this system emphasizes explainability, confidence-based role ranking, and clear skill-gap identification.

The system is designed to be robust, modular, and responsible, using deterministic logic for decision-making and generative AI only for explanation.

---

## Key Features

- Free-text skill input (no rigid forms or checklists)
- Skill extraction and normalization (e.g., C, C++, cpp → C/C++)
- Explainable role-to-skill mapping
- Confidence-based role suitability ranking
- Identification of skill gaps for partial matches
- AI-generated, human-readable explanations
- Downloadable analysis reports in PDF and JSON formats
- Clean and intuitive web interface

---

## System Architecture

The system follows a hybrid, agent-based architecture consisting of the following components:

1. Skill Extractor Agent  
   Extracts skills from unstructured user input.

2. Skill Normalization Layer  
   Resolves skill aliases and ensures consistent representation.

3. Role Translator Agent  
   Maps normalized skills to predefined career roles and computes confidence scores.

4. Skill Gap Analysis Agent  
   Identifies missing or complementary skills for each role.

5. AI Explanation Agent  
   Uses generative AI to explain results in neutral, educational language.

6. Frontend Interface  
   Presents results using an interactive Streamlit-based UI.

Agent orchestration is handled using LangGraph to ensure modularity and clear data flow.

---

## Technology Stack

- Python
- FastAPI (backend API)
- Streamlit (frontend user interface)
- LangGraph (agent orchestration)
- Gemini API (explanation generation)

---

## Responsible AI Design

This project follows responsible AI principles:

- Core career mapping logic is deterministic and rule-based
- Generative AI is used only for explanation, not for decision-making
- No predictions, guarantees, or career advice are provided
- Outputs are transparent, explainable, and user-focused
- Unknown or uncommon skills are preserved rather than discarded

---

## How to Run the Project

### Prerequisites
- Python 3.10 or later
- Virtual environment support

### Backend Setup

```bash
uvicorn app.main:app --reload
```

The backend will start at:
http://127.0.0.1:8000

### Frontend Setup

```bash
streamlit run app/frontend/app.py
```

The frontend will start at:
http://localhost:8501

---

## Project Documentation

Detailed project documentation is available in the `docs/` folder:

- Lean Canvas
- Concept Note
- Project Presentation

These documents describe the problem statement, solution approach, business model, and system design in detail.

---

## SDG Alignment

This project supports SDG 8: Decent Work and Economic Growth by:

- Enabling skill-based career awareness
- Supporting informed employability decisions
- Encouraging transparent and fair access to career opportunities
- Promoting lifelong learning and upskilling

---

## Future Scope

- Resume (PDF) parsing and analysis
- Embedding-based exploratory role discovery
- Industry-specific skill ontologies
- Human-in-the-loop validation for role mapping

---

## License

This project is intended for academic and internship evaluation purposes.
