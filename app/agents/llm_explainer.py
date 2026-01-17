import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


class LLMExplainerAgent:
    """
    Gemini-based explanation agent.
    STRICTLY explanation-only.
    Includes safe fallback to avoid API crashes.
    """

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment")

        self.client = genai.Client(api_key=api_key)
        self.model_name = "gemini-1.5-flash"

    def build_prompt(self, data: dict) -> str:
        return f"""
You are an AI system that EXPLAINS career analysis results.

STRICT RULES:
- Do NOT give advice
- Do NOT predict outcomes
- Do NOT recommend jobs
- ONLY explain the given results

User skills:
{data['identified_skills']}

Role analysis:
{data['role_translation']}

Skill gaps:
{data['skill_gap_recommendations']}

Write a short, neutral explanation (5–7 lines max) covering:
1. Why the strongest roles fit
2. What partial-fit roles indicate
3. What skill gaps represent

Use simple, educational language.
"""

    def explain(self, data: dict) -> str:
        prompt = self.build_prompt(data)

        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt
            )
            return response.text.strip()

        except Exception as e:
            # SAFE FALLBACK (never crash API)
            return (
                "The analysis shows strong alignment with several data- and "
                "analysis-focused roles based on your skills. Some roles show "
                "partial alignment, indicating additional skills could broaden "
                "your opportunities. Skill gaps highlight areas for further learning."
            )
