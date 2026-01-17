from typing import Dict, List


class SkillGapAgent:
    """
    Suggests skill improvements based on missing skills.
    """

    SKILL_RESOURCES = {
        "project management": "Intro to Project Management (Agile basics)",
        "machine learning": "Supervised ML fundamentals",
        "statistics": "Applied statistics for data analysis"
    }

    def recommend(self, role_data: Dict) -> Dict[str, List[str]]:
        recommendations = {}

        for role, data in role_data.items():
            missing = data["missing_skills"]
            if missing:
                recommendations[role] = [
                    self.SKILL_RESOURCES.get(skill, f"Learn {skill}")
                    for skill in missing
                ]

        return recommendations
