"""
career_agent.py
---------------
Agent 2 – Career Agent

Responsibilities:
  - Use the student's profile AND the skill-gap analysis from Agent 1.
  - Recommend 3 suitable career paths with explanations.
  - Suggest the best-fit role and why.
  - Output structured recommendations for Agent 3 (Learning Agent).
"""

from utils.llm_client import call_llm


# ---------------------------------------------------------------------------
# Prompt template
# ---------------------------------------------------------------------------
CAREER_AGENT_PROMPT = """
You are an expert Career Guidance AI for college students.

Student Profile:
- Degree / Branch   : {degree}
- Year of Study     : {year}
- Technical Skills  : {technical_skills}
- Soft Skills       : {soft_skills}
- Interests         : {interests}
- Projects / Experience : {projects}
- Target Job Role   : {target_role}

Skill Gap Analysis (from Skill Analyzer Agent):
{skill_analysis}

Your task:
1. Recommend 3 career paths that best match the student's profile and interests.
   For each path include: title, brief description, why it suits this student,
   average salary range (India & Global), and top hiring companies.
2. Identify the BEST-FIT career path with a clear justification.
3. List 3–5 certifications or credentials that would significantly boost
   employability for the best-fit path.
4. Mention 2–3 alternative roles the student could also explore.

Format your response EXACTLY as follows (use these headings):

## Career Path 1: <Title>
**Description:** ...
**Why it suits you:** ...
**Salary Range:** India – ₹X LPA | Global – $X K/yr
**Top Companies:** ...

## Career Path 2: <Title>
**Description:** ...
**Why it suits you:** ...
**Salary Range:** India – ₹X LPA | Global – $X K/yr
**Top Companies:** ...

## Career Path 3: <Title>
**Description:** ...
**Why it suits you:** ...
**Salary Range:** India – ₹X LPA | Global – $X K/yr
**Top Companies:** ...

## Best-Fit Career Path
<Title and detailed justification>

## Recommended Certifications
<numbered list>

## Alternative Roles to Explore
<bullet list>
"""


def recommend_careers(student_profile: dict, skill_analysis: str) -> str:
    """
    Run the Career Agent.

    Parameters
    ----------
    student_profile : dict
        Same dict passed to the Skill Analyzer.
    skill_analysis : str
        Output from the Skill Analyzer agent.

    Returns
    -------
    str
        Formatted career recommendations from the LLM.
    """
    prompt = CAREER_AGENT_PROMPT.format(
        degree=student_profile.get("degree", "N/A"),
        year=student_profile.get("year", "N/A"),
        technical_skills=student_profile.get("technical_skills", "N/A"),
        soft_skills=student_profile.get("soft_skills", "N/A"),
        interests=student_profile.get("interests", "N/A"),
        projects=student_profile.get("projects", "N/A"),
        target_role=student_profile.get("target_role", "N/A"),
        skill_analysis=skill_analysis,
    )
    return call_llm(prompt)
