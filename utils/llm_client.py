"""
llm_client.py
-------------
Centralised Gemini API client used by all agents.
Reads the API key from the .env file (never hard-coded).
"""

import os
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai

# Resolve .env relative to the careerpilot/ package root (two levels up from this file)
_ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=_ENV_PATH)


def get_llm_client():
    """
    Initialise and return a configured Gemini GenerativeModel instance.
    Raises a clear error if the API key is missing.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "GEMINI_API_KEY not found. "
            "Please create a .env file with your key (see .env.example)."
        )
    genai.configure(api_key=api_key)
    # gemini-2.5-flash is the latest available flash model (also known as gemini-3.6-flash)
    model = genai.GenerativeModel(model_name="gemini-2.5-flash")
    return model


def call_llm(prompt: str) -> str:
    """
    Send a prompt to the Gemini model and return the response text.

    Parameters
    ----------
    prompt : str
        The complete prompt string to send to the model.

    Returns
    -------
    str
        The model's text response, or an error message string.
    """
    try:
        model = get_llm_client()
        response = model.generate_content(prompt)
        # Extract plain text from the response
        return response.text.strip()
    except EnvironmentError as env_err:
        return f"⚠️ Configuration Error: {env_err}"
    except Exception as e:
        return f"⚠️ LLM Error: {str(e)}"
