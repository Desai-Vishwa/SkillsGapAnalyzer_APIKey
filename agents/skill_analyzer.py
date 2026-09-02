"""
skill_analyzer.py
-----------------
Agent 1 – Skill Analyzer

Responsibilities:
  - Compare the student's current skills against industry requirements
    for their target job role.
  - Identify skill gaps (technical and soft).
  - Return a structured analysis that the next agent (Career Agent) can use.
"""

from utils.llm_client import call_llm


# ---------------------------------------------------------------------------
# Prompt template
# ---------------------------------------------------------------------------
SKILL_ANALYZER_PROMPT = """
You are an expert Skill Analyzer AI for college students.

A student has shared the following profile:
- Degree / Branch   : {degree}
- Year of Study     : {year}
- Technical Skills  : {technical_skills}
- Soft Skills       : {soft_skills}
- Interests         : {interests}
- Projects / Experience : {projects}
- Target Job Role   : {target_role}

Your task:
1. List the key technical skills REQUIRED for the target role (at least 8–10 skills).
2. List the key soft skills REQUIRED for the target role (at least 4–5 skills).
3. Compare with what the student already has and identify SKILL GAPS clearly.
4. Rate the student's overall readiness for the target role (percentage, 0–100%).
5. Give a brief 2–3 line summary of the student's strengths.

Format your response EXACTLY as follows (use these headings):

## Required Technical Skills
<bullet list>

## Required Soft Skills
<bullet list>

## Skill Gaps (Technical)
<bullet list>

## Skill Gaps (Soft Skills)
<bullet list>

## Overall Readiness
<percentage and one-line reason>

## Strengths Summary
<2–3 sentences>
"""


def analyze_skills(student_profile: dict) -> str:
    """
    Run the Skill Analyzer agent.

    Parameters
    ----------
    student_profile : dict
        Keys: degree, year, technical_skills, soft_skills,
              interests, projects, target_role

    Returns
    -------
    str
        Formatted skill analysis from the LLM.
    """
    prompt = SKILL_ANALYZER_PROMPT.format(
        degree=student_profile.get("degree", "N/A"),
        year=student_profile.get("year", "N/A"),
        technical_skills=student_profile.get("technical_skills", "N/A"),
        soft_skills=student_profile.get("soft_skills", "N/A"),
        interests=student_profile.get("interests", "N/A"),
        projects=student_profile.get("projects", "N/A"),
        target_role=student_profile.get("target_role", "N/A"),
    )
    return call_llm(prompt)
