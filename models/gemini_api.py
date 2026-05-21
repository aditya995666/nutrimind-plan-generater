from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env file")

genai = Groq(api_key=API_KEY)

def generate_meal_with_gemini(prompt):
    try:
        response = genai.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama-3.1-8b-instant",  # ya "mixtral-8x7b-32768"
            max_tokens=4096,  # 🔥 YEH ADD KARO (default 1024 hai)
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error from Groq API: {str(e)}"