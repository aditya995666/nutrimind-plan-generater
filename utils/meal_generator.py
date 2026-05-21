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
👉 Generate a meal plan for EXACTLY {plan_days} DAYS
• If 3 Days selected → generate Day 1 to Day 3
• If 7 Days selected → generate Day 1 to Day 7
• Do NOT generate extra days

🚫 NON-NEGOTIABLE HARD RULES:
• NEVER leave Calories column blank or empty
• NEVER override backend macros
• Use realistic Indian nutrition values
• Nutrition values should be approximately accurate
• Portion sizes must be realistic
• Avoid impossible calorie combinations
• Daily calories can vary slightly (±50 kcal)

🔥 CRITICAL DIET RULE 🔥
• User's Diet Type = {diet}
• If diet = "Vegetarian" → NO egg, NO chicken, NO fish, NO meat
• If diet = "Non-Vegetarian" → eggs, chicken, fish allowed
• If diet = "Vegan" → NO dairy, NO eggs, NO animal products
• CURRENT USER DIET = {diet} → STRICTLY follow this!

🔥 REGIONAL FOOD ENFORCEMENT:
• If region = North Indian or state = UP:
  use foods like roti, dal, sabzi, poha, upma, khichdi,
  chole, rajma, curd, seasonal vegetables, oats, sprouts


• Avoid foreign foods unless explicitly requested
• Do NOT generate foods like tacos, quesadilla, pasta, sushi, burgers
• STRICTLY follow selected rice type
• If rice type = white rice → do not use brown rice

• Nutrition values should vary naturally based on ingredients
• Avoid repeating identical calories and protein values across meals

• Use medically realistic calorie estimations
• Avoid unrealistically low calorie values

• Use realistic Indian dish naming conventions

🚫 FOOD AVOIDANCE RULE:
• NEVER include foods marked as "None"
• If Paneer Intake = None → no paneer dishes
• If Soy Intake = None → no tofu/soy dishes


• STRICTLY NEVER include foods marked as "None"
• If Paneer Intake = None → paneer dishes are completely prohibited
• If Soy Intake = None → tofu/soy dishes are completely prohibited 

⚠ FINAL BACKEND TARGETS (APPROXIMATE RANGE):
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

Use backend targets as primary guidance.
Nutrition values should remain approximately close to backend targets.

=====================================
🕒 FIXED MEAL TIMINGS
=====================================
• Breakfast – 08:00
• Snack – 11:00
• Lunch – 14:00
• Snack – 17:00
• Dinner – 20:30

=====================================
📋 OUTPUT FORMAT (MUST FOLLOW EXACTLY)
=====================================

YOUR TARGET: {calories} CALORIES PER DAY 

INTERNAL AI INSTRUCTIONS (DO NOT DISPLAY TO USER):
• Maintain healthy variety across all selected days
• Avoid repeating the same MAIN DISH consecutively
• Staples like roti, rice, dal may repeat naturally
• Meals must look like realistic Indian household meals
• Prefer authentic regional Indian foods
• Breakfast should contain approximately 20–25% of daily calories
• Snack should contain approximately 5–10% of daily calories
• Lunch should contain approximately 30–35% of daily calories
• Dinner should contain approximately 30–35% of daily calories
• Do NOT print these rules in final output

Day 1:
Day 1:

| Meal | Time | Food (Exact g/ml/pcs) | Approx Calories | Approx Protein(g) | Benefit |
|------|------|------------------------|------------------|-------------------|---------|
| Breakfast | 08:00 | [FOOD with quantity] | [REALISTIC VALUE] | [REALISTIC VALUE] | [BENEFIT] |
| Snack | 11:00 | [FOOD with quantity] | [REALISTIC VALUE] | [REALISTIC VALUE] | [BENEFIT] |
| Lunch | 14:00 | [FOOD with quantity] | [REALISTIC VALUE] | [REALISTIC VALUE] | [BENEFIT] |
| Snack | 17:00 | [FOOD with quantity] | [REALISTIC VALUE] | [REALISTIC VALUE] | [BENEFIT] |
| Dinner | 20:30 | [FOOD with quantity] | [REALISTIC VALUE] | [REALISTIC VALUE] | [BENEFIT] |
Day Summary:
• Total Calories: {calories}
• Total Protein: {final_protein}
• Health Benefits Summary: [Write 2-3 lines]



Continue generating all days until the selected duration is completed.
Every day must contain different meals and realistic Indian foods.

NOW GENERATE YOUR MEAL PLAN:

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
• Food variety across all generated days is MANDATORY

📌 FOOD VARIETY ENFORCEMENT:
• Breakfast dishes must be different across all generated days
• Lunch main dishes must be different across all generated days
• Dinner main dishes must be different across all generated days
• Repetition is allowed ONLY for staples (roti/rice), not dishes

"""

def generate_meal_plan(*args, **kwargs):
    """
    Generates 3-day meal plan using Gemini.
    Backend macros MUST be used. No AI recalculation.
    """
    prompt = build_prompt(*args, **kwargs)
    return generate_meal_with_gemini(prompt)
