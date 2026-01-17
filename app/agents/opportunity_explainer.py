from typing import Dict


class OpportunityExplainerAgent:
    """
    Explains industries and role-fit reasoning.
    """

    ROLE_INDUSTRY_MAP = {
        "Data Analyst": ["IT Services", "Finance", "Healthcare", "E-commerce"],
        "Business Analyst": ["Consulting", "Finance", "Operations"],
        "Backend Developer": ["SaaS", "FinTech", "EdTech"],
        "Automation Engineer": ["Manufacturing", "IT Services"],
        "Business Intelligence Analyst": ["Retail", "Logistics"],
        "Operations Analyst": ["Supply Chain", "Manufacturing"],
        "Product Analyst": ["Tech", "E-commerce"],
        "Project Coordinator": ["IT Services", "Construction"]
    }

    def explain(self, ranked_roles: Dict) -> Dict:
        explanation = {}

        for role, data in ranked_roles.items():
            explanation[role] = {
                "confidence_score": data["confidence_score"],
                "industries": self.ROLE_INDUSTRY_MAP.get(role, ["Multiple sectors"]),
                "matched_skills": data["matched_skills"],
                "missing_skills": data["missing_skills"],
                "explanation": (
                    f"This role matches {int(data['confidence_score'] * 100)}% "
                    f"of the expected skills based on your profile."
                )
            }

        return explanation
