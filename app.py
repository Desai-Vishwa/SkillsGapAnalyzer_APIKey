"""
app.py
------
CareerPilot – AI Career Mentor
Main Streamlit application entry point.

Run with:
    streamlit run app.py

Workflow:
    Student Input → Skill Analyzer Agent → Career Agent → Learning Agent
                                                         → Final Career Roadmap
"""

import sys
import os

# ---------------------------------------------------------------------------
# Make sure sibling packages (agents/, utils/) are importable when the script
# is launched from any working directory.
# ---------------------------------------------------------------------------
sys.path.insert(0, os.path.dirname(__file__))

import streamlit as st
from agents.skill_analyzer import analyze_skills
from agents.career_agent import recommend_careers
from agents.learning_agent import create_learning_plan

# ---------------------------------------------------------------------------
# Page configuration
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="CareerPilot – AI Career Mentor",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------------
# Custom CSS – minimal, clean
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>
        .main-header {
            text-align: center;
            padding: 1rem 0 0.5rem 0;
        }
        .agent-badge {
            display: inline-block;
            background: #1e3a5f;
            color: #ffffff;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.82rem;
            font-weight: 600;
            margin-bottom: 0.4rem;
        }
        .section-divider {
            border: none;
            border-top: 2px solid #e5e7eb;
            margin: 1.5rem 0;
        }
        .stButton > button {
            width: 100%;
            background-color: #1e3a5f;
            color: white;
            font-size: 1.05rem;
            font-weight: 600;
            border-radius: 8px;
            padding: 0.6rem 1.2rem;
            border: none;
        }
        .stButton > button:hover {
            background-color: #2a4f7c;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
st.markdown(
    """
    <div class="main-header">
        <h1>🚀 CareerPilot – AI Career Mentor</h1>
        <p style="color:#57606a; font-size:1.05rem;">
            Your personalised, AI-powered career guidance powered by three specialised agents.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Sidebar – how it works
# ---------------------------------------------------------------------------
with st.sidebar:
    st.image(
        "https://img.icons8.com/fluency/96/rocket.png",
        width=64,
    )
    st.title("How It Works")
    st.markdown(
        """
        **Three Specialised AI Agents work in sequence:**

        1. 🔍 **Skill Analyzer Agent**
           Compares your skills with industry requirements and identifies gaps.

        2. 🎯 **Career Agent**
           Recommends career paths tailored to your profile.

        3. 📚 **Learning Agent**
           Creates a personalised 6-month roadmap + project ideas + interview prep.

        ---
        **Workflow**
        ```
        Your Input
           ↓
        Skill Analyzer
           ↓
        Career Agent
           ↓
        Learning Agent
           ↓
        Career Roadmap
        ```
        ---
        *Powered by Google Gemini 2.5 Flash*
        """
    )

# ---------------------------------------------------------------------------
# Student Input Form
# ---------------------------------------------------------------------------
st.subheader("📋 Student Profile")
st.caption("Fill in your details below — the more detail you provide, the better the guidance.")

with st.form("student_profile_form"):
    col1, col2 = st.columns(2)

    with col1:
        degree = st.text_input(
            "🎓 Degree / Branch",
            placeholder="e.g. B.Tech – Computer Science",
        )
        year = st.selectbox(
            "📅 Year of Study",
            ["1st Year", "2nd Year", "3rd Year", "4th Year", "Graduated"],
        )
        technical_skills = st.text_area(
            "💻 Technical Skills",
            placeholder="e.g. Python, SQL, Machine Learning, React, Git",
            height=100,
        )
        soft_skills = st.text_area(
            "🤝 Soft Skills",
            placeholder="e.g. Communication, Teamwork, Problem Solving",
            height=80,
        )

    with col2:
        interests = st.text_area(
            "💡 Interests",
            placeholder="e.g. AI/ML, Web Development, Data Analytics, Cybersecurity",
            height=80,
        )
        projects = st.text_area(
            "🛠️ Projects / Experience",
            placeholder=(
                "e.g. Built a movie recommendation system using collaborative filtering. "
                "Interned at XYZ as a data analyst for 2 months."
            ),
            height=120,
        )
        target_role = st.text_input(
            "🎯 Target Job Role",
            placeholder="e.g. Machine Learning Engineer",
        )

    submitted = st.form_submit_button("🚀 Generate My Career Roadmap")

# ---------------------------------------------------------------------------
# Validation helper
# ---------------------------------------------------------------------------
def validate_inputs(degree, technical_skills, target_role):
    """Return (is_valid, error_message)."""
    if not degree.strip():
        return False, "Please enter your Degree / Branch."
    if not technical_skills.strip():
        return False, "Please enter at least one Technical Skill."
    if not target_role.strip():
        return False, "Please enter your Target Job Role."
    return True, ""

# ---------------------------------------------------------------------------
# Agent pipeline – runs only after form submission
# ---------------------------------------------------------------------------
if submitted:
    is_valid, error_msg = validate_inputs(degree, technical_skills, target_role)

    if not is_valid:
        st.error(f"❌ {error_msg}")
    else:
        # Build the student profile dict passed through the agent chain
        student_profile = {
            "degree": degree,
            "year": year,
            "technical_skills": technical_skills,
            "soft_skills": soft_skills,
            "interests": interests,
            "projects": projects,
            "target_role": target_role,
        }

        st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)
        st.subheader("🤖 Agent Pipeline – Running…")

        # -------------------------------------------------------------------
        # Agent 1 – Skill Analyzer
        # -------------------------------------------------------------------
        with st.status("🔍 Agent 1: Skill Analyzer is working…", expanded=True) as status1:
            st.write("Analysing your skills vs. industry requirements for **{}**…".format(target_role))
            skill_analysis = analyze_skills(student_profile)

            if skill_analysis.startswith("⚠️"):
                st.error(skill_analysis)
                st.stop()

            status1.update(label="✅ Agent 1: Skill Analysis Complete", state="complete", expanded=False)

        # -------------------------------------------------------------------
        # Agent 2 – Career Agent
        # -------------------------------------------------------------------
        with st.status("🎯 Agent 2: Career Agent is working…", expanded=True) as status2:
            st.write("Generating career path recommendations…")
            career_recommendations = recommend_careers(student_profile, skill_analysis)

            if career_recommendations.startswith("⚠️"):
                st.error(career_recommendations)
                st.stop()

            status2.update(label="✅ Agent 2: Career Recommendations Ready", state="complete", expanded=False)

        # -------------------------------------------------------------------
        # Agent 3 – Learning Agent
        # -------------------------------------------------------------------
        with st.status("📚 Agent 3: Learning Agent is working…", expanded=True) as status3:
            st.write("Building your personalised learning roadmap…")
            learning_plan = create_learning_plan(
                student_profile, skill_analysis, career_recommendations
            )

            if learning_plan.startswith("⚠️"):
                st.error(learning_plan)
                st.stop()

            status3.update(label="✅ Agent 3: Learning Roadmap Ready", state="complete", expanded=False)

        # -------------------------------------------------------------------
        # Results – display in tabs
        # -------------------------------------------------------------------
        st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)
        st.subheader("📊 Your Personalised Career Roadmap")
        st.caption(
            f"Generated for **{degree}** student targeting **{target_role}** | {year}"
        )

        tab1, tab2, tab3 = st.tabs(
            [
                "🔍 Skill Analysis & Gaps",
                "🎯 Career Recommendations",
                "📚 Learning Roadmap & Interview Prep",
            ]
        )

        with tab1:
            st.markdown('<span class="agent-badge">Agent 1 · Skill Analyzer</span>', unsafe_allow_html=True)
            st.markdown(skill_analysis)

        with tab2:
            st.markdown('<span class="agent-badge">Agent 2 · Career Agent</span>', unsafe_allow_html=True)
            st.markdown(career_recommendations)

        with tab3:
            st.markdown('<span class="agent-badge">Agent 3 · Learning Agent</span>', unsafe_allow_html=True)
            st.markdown(learning_plan)

        # -------------------------------------------------------------------
        # Download button – combined report as plain text
        # -------------------------------------------------------------------
        st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)
        full_report = (
            f"# CareerPilot – Career Report\n"
            f"**Student:** {degree} | {year}\n"
            f"**Target Role:** {target_role}\n\n"
            f"---\n\n"
            f"## Skill Analysis\n{skill_analysis}\n\n"
            f"---\n\n"
            f"## Career Recommendations\n{career_recommendations}\n\n"
            f"---\n\n"
            f"## Learning Roadmap & Interview Prep\n{learning_plan}\n"
        )

        st.download_button(
            label="⬇️ Download Full Report (.txt)",
            data=full_report,
            file_name=f"careerpilot_report_{target_role.replace(' ', '_')}.txt",
            mime="text/plain",
        )

        st.success(
            "✅ All three agents completed successfully! "
            "Review each tab above for your full career roadmap."
        )
