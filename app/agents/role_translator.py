class RoleTranslatorAgent:
    """
    Maps normalized skills to suitable career roles
    using explicit, explainable role skill requirements.
    """

    ROLE_SKILL_MAP = {
        "Data Analyst": {
            "skills": {"Python", "SQL", "Excel", "Data Analysis"},
            "industries": ["IT Services", "Finance", "Healthcare", "E-commerce"]
        },
        "Business Analyst": {
            "skills": {"Excel", "Data Analysis", "Communication"},
            "industries": ["Consulting", "Finance", "Operations"]
        },
        "Backend Developer": {
            "skills": {"Python", "SQL"},
            "industries": ["SaaS", "FinTech", "EdTech"]
        },
        "Automation Engineer": {
            "skills": {"Python"},
            "industries": ["Manufacturing", "IT Services"]
        },
        "Machine Learning Engineer": {
            "skills": {"Python", "Machine Learning"},
            "industries": ["AI", "FinTech", "Healthcare", "Research"]
        },
        "AI Engineer": {
            "skills": {"Python", "Machine Learning"},
            "industries": ["AI", "Robotics", "Startups"]
        },
        "Software Engineer (C/C++)": {
            "skills": {"C/C++"},
            "industries": ["Systems", "Embedded", "Gaming", "Defense"]
        },
        "Systems Programmer": {
            "skills": {"C/C++"},
            "industries": ["OS Development", "Embedded", "Infrastructure"]
        },
    }

    def translate(self, identified_skills: list[str]):
        roles_ranked = {}

        skill_set = set(identified_skills)

        for role, data in self.ROLE_SKILL_MAP.items():
            required_skills = data["skills"]
            matched = skill_set.intersection(required_skills)

            if not matched:
                continue

            confidence = len(matched) / len(required_skills)

            roles_ranked[role] = {
                "confidence_score": round(confidence, 2),
                "industries": data["industries"],
                "matched_skills": sorted(matched),
                "missing_skills": sorted(required_skills - matched),
                "explanation": (
                    f"This role matches {int(confidence * 100)}% "
                    f"of the expected skills based on your profile."
                )
            }

        return {
            "roles_ranked": roles_ranked
        }
