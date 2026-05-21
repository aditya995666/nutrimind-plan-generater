# utils/state_foods.py
import json
import os

STATE_FILE = os.path.join("data", "state_foods.json")

if os.path.exists(STATE_FILE):
    with open(STATE_FILE, "r", encoding="utf-8") as f:
        state_foods = json.load(f)
else:
    # sensible defaults
    state_foods = {
        "UP": ["poha", "paratha", "dal-chawal"],
        "Delhi": ["chole bhature", "tandoori roti"],
        "South India": ["idli", "dosa", "sambar"],
        # add more as needed
    }

def get_state_meals(state):
    return state_foods.get(state, [])
