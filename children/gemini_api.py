import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError("❌ ERROR: GEMINI_API_KEY is missing")

# Initialize Groq client instead of Gemini
genai = Groq(api_key=API_KEY)

def call_gemini(prompt: str) -> str:
    """Simple working version - now using Groq"""
    try:
        # Groq compatible call
        chat_completion = genai.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama-3.1-8b-instant",  # You can change to: "mixtral-8x7b-32768" or "gemma2-9b-it"
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"❌ API Error: {str(e)}"
        