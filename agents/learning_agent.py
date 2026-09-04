"""
learning_agent.py
-----------------
Agent 3 – Learning Agent

Responsibilities:
  - Use the skill gaps (from Agent 1) and the career recommendations (from Agent 2).
  - Build a personalised, month-by-month learning roadmap.
  - Recommend specific projects the student should build.
  - Provide interview preparation tips for the best-fit role.
"""

from utils.llm_client import call_llm


# ---------------------------------------------------------------------------
# Prompt template
# ---------------------------------------------------------------------------
LEARNING_AGENT_PROMPT = """
You are an expert Learning Path Designer AI for college students.

Student Profile:
- Degree / Branch   : {degree}
- Year of Study     : {year}
- Target Job Role   : {target_role}

Skill Gap Analysis:
{skill_analysis}

Career Recommendations:
{career_recommendations}

Your task — create a COMPLETE personalised learning plan:

1. A month-by-month roadmap (6 months) to close the skill gaps and prepare for
   the best-fit career. Each month should have: focus area, specific topics,
   free/paid resources (course name + platform).
2. 5 hands-on projects the student should build (with brief descriptions and
   the skills each project demonstrates).
3. Interview preparation plan covering:
   - Key DSA / CS fundamentals topics to revise
   - Domain-specific technical topics
   - Behavioural / HR questions to prepare
   - Mock interview strategy
4. Daily study schedule recommendation (hours per day, split across topics).

Format your response EXACTLY as follows (use these headings):

## 6-Month Learning Roadmap

### Month 1: <Focus Area>
**Topics:** ...
**Resources:** ...

### Month 2: <Focus Area>
**Topics:** ...
**Resources:** ...

### Month 3: <Focus Area>
**Topics:** ...
**Resources:** ...

### Month 4: <Focus Area>
**Topics:** ...
**Resources:** ...

### Month 5: <Focus Area>
**Topics:** ...
**Resources:** ...

### Month 6: <Focus Area>
**Topics:** ...
**Resources:** ...

## Recommended Projects

### Project 1: <Name>
**Description:** ...
**Skills Demonstrated:** ...

### Project 2: <Name>
**Description:** ...
**Skills Demonstrated:** ...

### Project 3: <Name>
**Description:** ...
**Skills Demonstrated:** ...

### Project 4: <Name>
**Description:** ...
**Skills Demonstrated:** ...

### Project 5: <Name>
**Description:** ...
**Skills Demonstrated:** ...

## Interview Preparation

### DSA & CS Fundamentals
<bullet list of topics>

### Domain-Specific Technical Topics
<bullet list of topics>

### Behavioural / HR Questions
<bullet list of sample questions>

### Mock Interview Strategy
<3–5 actionable tips>

## Daily Study Schedule
<Recommended hours and topic split>
"""


def create_learning_plan(
    student_profile: dict,
    skill_analysis: str,
    career_recommendations: str,
    api_key: str | None = None,
) -> str:
    """
    Run the Learning Agent.

    Parameters
    ----------
    student_profile : dict
        Same dict passed to the previous agents.
    skill_analysis : str
        Output from the Skill Analyzer agent.
    career_recommendations : str
        Output from the Career Agent.
    api_key : str | None
        Gemini API key. Falls back to the GEMINI_API_KEY env var if not provided.

    Returns
    -------
    str
        Formatted learning roadmap from the LLM.
    """
    prompt = LEARNING_AGENT_PROMPT.format(
        degree=student_profile.get("degree", "N/A"),
        year=student_profile.get("year", "N/A"),
        target_role=student_profile.get("target_role", "N/A"),
        skill_analysis=skill_analysis,
        career_recommendations=career_recommendations,
    )
    return call_llm(prompt, api_key=api_key)
