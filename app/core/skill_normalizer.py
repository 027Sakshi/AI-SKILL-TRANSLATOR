from app.core.skill_aliases import SKILL_ALIASES


def normalize_skills(raw_skills: list[str]) -> list[str]:
    """
    Normalizes raw extracted skills using alias mapping.
    Known aliases → canonical names.
    Unknown skills → preserved (capitalized).
    """

    normalized = set()

    # Flatten all aliases into a single set for fast lookup
    all_aliases = {
        alias.lower()
        for aliases in SKILL_ALIASES.values()
        for alias in aliases
    }

    # First: match known aliases
    for canonical, aliases in SKILL_ALIASES.items():
        for alias in aliases:
            if alias.lower() in raw_skills:
                normalized.add(canonical)

    # Second: preserve unknown skills
    for skill in raw_skills:
        if skill.lower() not in all_aliases:
            normalized.add(skill.capitalize())

    return sorted(normalized)
