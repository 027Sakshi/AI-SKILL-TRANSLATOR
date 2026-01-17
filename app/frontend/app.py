import streamlit as st
import requests
import json
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

API_URL = "http://127.0.0.1:8000/translate-skills"

st.set_page_config(
    page_title="AI Skill-to-Opportunity Translator",
    layout="wide"
)

st.title("💼 AI Skill-to-Opportunity Translator")
st.caption("Explainable, agent-driven career opportunity mapping")

# ---------------- User Input ----------------
st.subheader("📝 Your Skill Profile")

skills_text = st.text_area(
    "Describe your skills:",
    placeholder="Python, SQL, Excel, data analysis, communication"
)

analyze_btn = st.button("🚀 Analyze My Skills")

# ---------------- API Call ----------------
if analyze_btn:
    if not skills_text.strip():
        st.warning("Please enter your skills.")
    else:
        payload = {
            "education": "",
            "experience": "",
            "skills_text": skills_text
        }

        with st.spinner("Running multi-agent analysis..."):
            response = requests.post(API_URL, json=payload)

        if response.status_code != 200:
            st.error("Backend error. Ensure FastAPI is running.")
        else:
            data = response.json()

            # ---------------- Identified Skills ----------------
            st.divider()
            st.subheader("🧠 Identified Skills")
            st.write(", ".join(data["identified_skills"]))

            # ---------------- Role Ranking ----------------
            st.divider()
            st.subheader("🎯 Role Suitability Ranking")

            roles = data["role_translation"]

            ranked_roles = sorted(
                roles.items(),
                key=lambda x: x[1]["confidence_score"],
                reverse=True
            )

            for role, details in ranked_roles:
                confidence = int(details["confidence_score"] * 100)

                if confidence >= 75:
                    fit_label = "🟢 Strong Fit"
                elif confidence >= 40:
                    fit_label = "🟡 Partial Fit"
                else:
                    fit_label = "🔵 Exploratory Fit"

                with st.container(border=True):
                    st.markdown(f"### {role} — {fit_label}")
                    st.progress(confidence / 100)
                    st.caption(f"Confidence Score: {confidence}%")

                    cols = st.columns(2)
                    with cols[0]:
                        st.markdown("**Industries**")
                        st.write(", ".join(details["industries"]))
                        st.markdown("**Matched Skills**")
                        st.write(", ".join(details["matched_skills"]))
                    with cols[1]:
                        st.markdown("**Missing Skills**")
                        st.write(", ".join(details["missing_skills"]) if details["missing_skills"] else "None")

            # ---------------- Skill Gaps ----------------
            st.divider()
            st.subheader("📘 Skill Gap Recommendations")

            if data["skill_gap_recommendations"]:
                for role, recs in data["skill_gap_recommendations"].items():
                    st.markdown(f"**{role}**")
                    for r in recs:
                        st.write(f"- {r}")
            else:
                st.success("No critical skill gaps identified.")

            # ---------------- AI Explanation ----------------
            st.divider()
            st.subheader("🤖 AI Explanation")
            st.write(data["ai_explanation"])

            # ---------------- DOWNLOAD SECTION ----------------
            st.divider()
            st.subheader("📥 Download Report")

            # ---- JSON Download ----
            json_bytes = json.dumps(data, indent=2).encode("utf-8")
            st.download_button(
                label="⬇️ Download JSON Report",
                data=json_bytes,
                file_name="skill_to_opportunity_report.json",
                mime="application/json"
            )

            # ---- PDF Download ----
            buffer = BytesIO()
            doc = SimpleDocTemplate(buffer)
            styles = getSampleStyleSheet()
            story = []

            story.append(Paragraph("<b>AI Skill-to-Opportunity Report</b>", styles["Title"]))
            story.append(Spacer(1, 12))

            story.append(Paragraph("<b>Identified Skills:</b>", styles["Heading2"]))
            story.append(Paragraph(", ".join(data["identified_skills"]), styles["Normal"]))
            story.append(Spacer(1, 12))

            story.append(Paragraph("<b>Role Analysis:</b>", styles["Heading2"]))
            for role, d in ranked_roles:
                story.append(Paragraph(
                    f"<b>{role}</b> (Confidence: {int(d['confidence_score'] * 100)}%)",
                    styles["Normal"]
                ))
                story.append(Paragraph(
                    f"Matched Skills: {', '.join(d['matched_skills'])}",
                    styles["Normal"]
                ))
                if d["missing_skills"]:
                    story.append(Paragraph(
                        f"Missing Skills: {', '.join(d['missing_skills'])}",
                        styles["Normal"]
                    ))
                story.append(Spacer(1, 8))

            story.append(Spacer(1, 12))
            story.append(Paragraph("<b>AI Explanation:</b>", styles["Heading2"]))
            story.append(Paragraph(data["ai_explanation"], styles["Normal"]))

            doc.build(story)
            buffer.seek(0)

            st.download_button(
                label="⬇️ Download PDF Report",
                data=buffer,
                file_name="skill_to_opportunity_report.pdf",
                mime="application/pdf"
            )
