from typing import TypedDict, List, Dict
from langgraph.graph import StateGraph, END

from app.agents.skill_extractor import SkillExtractorAgent
from app.agents.role_translator import RoleTranslatorAgent
from app.agents.opportunity_explainer import OpportunityExplainerAgent
from app.agents.skill_gap_agent import SkillGapAgent


# -------- Graph State --------
class CareerGraphState(TypedDict, total=False):
    skills_text: str
    identified_skills: List[str]
    roles_ranked: Dict
    opportunities: Dict
    skill_gaps: Dict


# -------- Initialize Agents --------
skill_extractor = SkillExtractorAgent()
role_translator = RoleTranslatorAgent()
opportunity_explainer = OpportunityExplainerAgent()
skill_gap_agent = SkillGapAgent()


# -------- Graph Nodes --------
def skill_extractor_node(state: CareerGraphState):
    skills_text = state.get("skills_text", "")
    result = skill_extractor.extract(skills_text)
    state["identified_skills"] = result["identified_skills"]
    return state


def role_translator_node(state: CareerGraphState):
    result = role_translator.translate(state["identified_skills"])
    state["roles_ranked"] = result["roles_ranked"]
    return state


def opportunity_explainer_node(state: CareerGraphState):
    state["opportunities"] = opportunity_explainer.explain(
        state["roles_ranked"]
    )
    return state


def skill_gap_node(state: CareerGraphState):
    state["skill_gaps"] = skill_gap_agent.recommend(
        state["roles_ranked"]
    )
    return state


# -------- Build Graph --------
def build_career_graph():
    graph = StateGraph(CareerGraphState)

    graph.add_node("skill_extractor", skill_extractor_node)
    graph.add_node("role_translator", role_translator_node)
    graph.add_node("opportunity_explainer", opportunity_explainer_node)
    graph.add_node("skill_gap", skill_gap_node)

    graph.set_entry_point("skill_extractor")

    graph.add_edge("skill_extractor", "role_translator")
    graph.add_edge("role_translator", "opportunity_explainer")
    graph.add_edge("opportunity_explainer", "skill_gap")
    graph.add_edge("skill_gap", END)

    return graph.compile()
