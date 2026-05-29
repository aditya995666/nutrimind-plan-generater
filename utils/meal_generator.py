from models.gemini_api import generate_meal_with_gemini
from utils.state_foods import get_state_meals
from utils.disease_filter import disease_rules
from utils.nutrition_utils import calculate_macros


def build_prompt(
    age, weight, height, gender, activity,plan_days,
    disease, diabetes_type, thyroid_type,
    bp_level, cholesterol_level, liver_stage, kidney_stage, gastric_issue,
    state, goal, water_require, diet, allergy, regional,
    breakfast, lunch, dinner, chapati_count, eat_rice, rice_type, rice_quantity,
    stress, egg_days, eggs_per_day, chicken_days, chicken_grams,
    fish_days, fish_grams, milk_glass, milk_type,
    workout_type, workout_duration, oil_preference,
    eat_out_food, smoking, alcohol,
    disease_duration, tablet_times,
    rice_per_day, paneer_intake, soy_intake,
    calories=None, macros=None,
    protein_target=None
):

 # -----
    system_calories = f"{calories} kcal/day"
    final_protein = protein_target if protein_target else macros["protein_g"]

    system_macros = (
        f"Protein {final_protein}g | Carbs {macros['carbs_g']}g | Fats {macros['fats_g']}g"
        if macros else "ERROR: Backend macros missing"
    )

    system_water = f"{water_require} L/day"
    fixed_rice_day = rice_per_day if eat_rice.lower() == "yes" else 0

    # -------------------------
    # EATING OUT (ONLY IF APPLICABLE)
    # -------------------------
    outside_food_text = ""
    if eat_out_food and eat_out_food != "None":
        outside_food_text = f"Eating Outside Food: {eat_out_food}"

    return f"""
You are an **Indian Clinical Nutritionist**.
LANGUAGE RULE (STRICT & NON-NEGOTIABLE):
👉 Output MUST be written in **ENGLISH ONLY**
👉 Do NOT use Hindi, Hinglish, or any regional language
👉 Use professional clinical English terminology only

🚨 ABSOLUTE MANDATORY RULE:
👉 You MUST generate a meal plan for **EXACTLY {plan_days} DAYS ONLY**.
👉 You MUST generate **Day 1, Day 2, ... up to Day {plan_days}**.

🚫 NON-NEGOTIABLE HARD RULES:
• You MUST calculate and fill Calories column with actual numbers.
• NEVER estimate macros of food.
• NEVER override backend macros.
• Adjust ONLY quantities to match backend macros.
• NEVER modify meal timing.
• ALWAYS respect user's habitual diet CATEGORY, not exact dishes.
• Avoid repetition unless habits require.
• Use ONLY foods allowed by diet/allergy/state.
• CURRENT DIET = {diet}. If Vegetarian: NO fish, NO chicken, NO egg, NO meat. ONLY plant-based protein.
• DO NOT add any theories (TDEE, BMR, formulas).

⚠ FINAL BACKEND VALUES (MUST MATCH EXACTLY):
Calories/day = {calories}
Protein/day = {final_protein} g
Carbs/day   = {macros['carbs_g']} g
Fats/day    = {macros['fats_g']} g
Water/day   = {system_water}

=====================================
🧍 USER DETAILS
=====================================
Age: {age}
Weight: {weight} kg
Height: {height} cm
Gender: {gender}
Activity: {activity}
Goal: {goal}
Stress Level: {stress}
State: {state}

=====================================
⚕ MEDICAL CONDITIONS
=====================================
Disease: {disease}
{f"Diabetes Type: {diabetes_type}" if disease=='Diabetes' else ""}
{f"Thyroid Type: {thyroid_type}" if disease=='Thyroid' else ""}
{f"BP Level: {bp_level}" if bp_level!='None' else ""}
{f"Cholesterol: {cholesterol_level}" if cholesterol_level!='None' else ""}
{f"Liver Stage: {liver_stage}" if disease=='Fatty Liver' else ""}
{f"Kidney Stage: {kidney_stage}" if disease=='Kidney' else ""}
{f"Gastric Issues: {gastric_issue}" if gastric_issue!='None' else ""}
Disease Duration: {disease_duration}
Medicine Intake: {tablet_times}

=====================================
🚬 LIFESTYLE HABITS
=====================================
Smoking: {smoking}
Alcohol Consumption: {alcohol}

=====================================
🍽 CURRENT EATING PATTERN (HABIT CONTEXT ONLY)
The user usually prefers:
• Breakfast style: {breakfast}
• Lunch style: {lunch}
• Dinner style: {dinner}

Chapati per meal: {chapati_count}
Rice: {eat_rice} ({rice_type}, {rice_quantity})
Rice/day: {fixed_rice_day}
Paneer Intake: {paneer_intake}
Soy Intake: {soy_intake}
Eggs: {egg_days} days/week, {eggs_per_day}/day
Chicken: {chicken_days} days/week, {chicken_grams}g
Fish: {fish_days} days/week, {fish_grams}g
Milk: {milk_glass} glass ({milk_type})
Oil Preference: {oil_preference}
{outside_food_text}

=====================================
📊 BACKEND NUTRITION TARGETS
=====================================
Calories Target: {system_calories}
Macro Targets: {system_macros}
Water Requirement: {system_water}

🚫 DO NOT RECALCULATE ANYTHING.

=====================================
🕒 FIXED MEAL TIMINGS
=====================================
• Breakfast – 08:00
• Snack – 11:00
• Lunch – 14:00
• Snack – 17:00
• Dinner – 20:30

=====================================
📋 OUTPUT FORMAT (STRICT)
=====================================

Day X:
| Meal | Time | Food (Exact g/ml/pcs) | Calories | Protein(g) | Benefit |
|------|------|------------------------|----------|-------------|---------|

Day Summary:
• Total Calories: MUST MATCH {calories}
• Total Protein: MUST MATCH {final_protein}
• Health Benefits Summary

=====================================
📊 FINAL MANDATORY OUTPUT BLOCK
=====================================
📊 AI Validated Nutrition Summary
Final Calories: {calories}
Protein: {final_protein}
Carbs: {macros['carbs_g']}
Fats: {macros['fats_g']}
Water Requirement: {water_require}



⚠ HABIT USAGE RULE (CRITICAL):
• Breakfast, Lunch, and Dinner inputs are REFERENCE PATTERNS ONLY
• DO NOT repeat the same food items verbatim
• You MUST create a proper meal plan using allowed Indian foods
• Meals should be habit-compatible, not habit-duplicated
• Food variety across Day 1–Day {plan_days} is MANDATORY

📌 FOOD VARIETY ENFORCEMENT:
• Breakfast dishes must be DIFFERENT across all {plan_days} days
• Lunch main dish must be DIFFERENT across all {plan_days} days
• Dinner main dish must be DIFFERENT across all {plan_days} days
• Repetition is allowed ONLY for staples (roti/rice), not dishes

"""

def generate_meal_plan(*args, **kwargs):
    """
    Generates 3-day meal plan using Gemini.
    Backend macros MUST be used. No AI recalculation.
    """
    prompt = build_prompt(*args, **kwargs)
    return generate_meal_with_gemini(prompt)