import re
from app.core.skill_normalizer import normalize_skills


class SkillExtractorAgent:
    """
    Extracts raw skills from free-text input and normalizes them
    using a canonical skill alias mapping.
    """

    def extract(self, skills_text: str):
        if not skills_text:
            return {"identified_skills": []}

        # ----------------------------
        # Step 1: Basic text cleaning
        # ----------------------------
        text = skills_text.lower()

        # Replace common separators with spaces
        text = re.sub(r"[,\n;/]", " ", text)

        # Keep + for c++ before splitting
        tokens = re.findall(r"[a-zA-Z\+\.]+", text)

        # ----------------------------
        # Step 2: Raw skill candidates
        # ----------------------------
        raw_skills = []
        for token in tokens:
            token = token.strip()

            # Ignore very small noise tokens
            if len(token) < 2:
                continue

            raw_skills.append(token)

        # ----------------------------
        # Step 3: Normalize skills
        # ----------------------------
        normalized_skills = normalize_skills(raw_skills)

        return {
            "identified_skills": normalized_skills
        }
