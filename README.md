# 🚀 CareerPilot – AI Career Mentor

A **Streamlit-based Agentic AI application** that guides college students from their current skill set to a fully personalised career roadmap — powered by **Google Gemini 2.0 Flash**.

---

## 📐 Architecture

```
Student Input
     │
     ▼
┌─────────────────────┐
│  Skill Analyzer     │  Agent 1 – Identifies skill gaps vs. target role
│  Agent              │
└─────────────────────┘
     │  skill_analysis
     ▼
┌─────────────────────┐
│  Career Agent       │  Agent 2 – Recommends career paths & certifications
└─────────────────────┘
     │  career_recommendations
     ▼
┌─────────────────────┐
│  Learning Agent     │  Agent 3 – Builds 6-month roadmap + projects + interview prep
└─────────────────────┘
     │
     ▼
 Final Career Roadmap (displayed in tabbed UI + downloadable report)
```

---

## 📁 Project Structure

```
careerpilot/
├── app.py                   # Streamlit entry point
├── agents/
│   ├── __init__.py
│   ├── skill_analyzer.py    # Agent 1
│   ├── career_agent.py      # Agent 2
│   └── learning_agent.py    # Agent 3
├── utils/
│   ├── __init__.py
│   └── llm_client.py        # Gemini API wrapper
├── requirements.txt
├── .env.example             # Template – copy to .env
├── .gitignore
└── README.md
```

---

## ⚙️ Setup

### 1. Clone / download the project

```bash
git clone <repo-url>
cd careerpilot
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your Gemini API key

```bash
cp .env.example .env
```

Open `.env` and replace `your_gemini_api_key_here` with your actual key from [Google AI Studio](https://aistudio.google.com/app/apikey).

```
GEMINI_API_KEY=AIza...
```

### 5. Run the application

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🖥️ Usage

1. Fill in the **Student Profile** form:
   - Degree / Branch
   - Year of Study
   - Technical Skills
   - Soft Skills
   - Interests
   - Projects / Experience
   - Target Job Role

2. Click **"🚀 Generate My Career Roadmap"**.

3. Watch the three agents run in sequence and then review results in three tabs:
   - **Skill Analysis & Gaps**
   - **Career Recommendations**
   - **Learning Roadmap & Interview Prep**

4. Download the full report as a `.txt` file.

---

## 🔑 Getting a Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Sign in with your Google account.
3. Click **Create API Key**.
4. Copy the key into your `.env` file.

The free tier is sufficient for testing this application.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| UI | Streamlit |
| LLM | Google Gemini 2.0 Flash |
| Language | Python 3.9+ |
| API Client | `google-generativeai` |
| Config | `python-dotenv` |

---

## 📄 License

MIT – free to use, modify, and distribute.
