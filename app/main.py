from fastapi import FastAPI

from app.schemas.user_input import UserProfile
from app.graph.career_graph import build_career_graph
from app.agents.llm_explainer import LLMExplainerAgent

app = FastAPI(title="AI Skill-to-Opportunity Translator")

# Initialize LangGraph workflow
career_graph = build_career_graph()

# Initialize Gemini explanation agent
llm_explainer = LLMExplainerAgent()


@app.get("/")
def health_check():
    return {
        "status": "running",
        "message": "AI Skill-to-Opportunity Translator API is live (LangGraph + Gemini)"
    }


@app.post("/translate-skills")
def translate_skills(user: UserProfile):
    # Run LangGraph workflow
    result = career_graph.invoke(
        {
            "skills_text": user.skills_text
        }
    )

    # Structured deterministic output
    final_output = {
        "identified_skills": result.get("identified_skills", []),
        "role_translation": result.get("opportunities", {}),
        "skill_gap_recommendations": result.get("skill_gaps", {})
    }

    # Gemini explanation (safe, explanation-only)
    ai_explanation = llm_explainer.explain(final_output)

    return {
        **final_output,
        "ai_explanation": ai_explanation
    }
