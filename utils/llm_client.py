"""
llm_client.py
-------------
Centralised Gemini API client used by all agents.
API key is supplied at call time (from the UI) or falls back to the .env file.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai

# Resolve .env relative to the careerpilot/ package root (two levels up from this file)
_ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=_ENV_PATH)


def get_llm_client(api_key: str | None = None):
    """
    Initialise and return a configured Gemini GenerativeModel instance.

    Parameters
    ----------
    api_key : str | None
        API key supplied directly (e.g. from the UI).
        Falls back to the GEMINI_API_KEY environment variable if not provided.

    Raises a clear error if no key is available from either source.
    """
    key = api_key or os.getenv("GEMINI_API_KEY")
    if not key:
        raise EnvironmentError(
            "Gemini API key not provided. "
            "Enter your key in the sidebar or create a .env file (see .env.example)."
        )
    genai.configure(api_key=key)
    model = genai.GenerativeModel(model_name="gemini-2.5-flash")
    return model


def call_llm(prompt: str, api_key: str | None = None) -> str:
    """
    Send a prompt to the Gemini model and return the response text.

    Parameters
    ----------
    prompt : str
        The complete prompt string to send to the model.
    api_key : str | None
        API key supplied directly (e.g. from the UI).
        Falls back to the GEMINI_API_KEY environment variable if not provided.

    Returns
    -------
    str
        The model's text response, or an error message string.
    """
    try:
        model = get_llm_client(api_key=api_key)
        response = model.generate_content(prompt)
        # Extract plain text from the response
        return response.text.strip()
    except EnvironmentError as env_err:
        return f"⚠️ Configuration Error: {env_err}"
    except Exception as e:
        return f"⚠️ LLM Error: {str(e)}"
