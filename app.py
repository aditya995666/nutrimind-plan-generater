import streamlit as st
import re

from components.sidebar import sidebar_inputs
from utils.nutrition_utils import (
    calculate_bmi,
    calculate_bmr,
    calculate_tdee,
    adjust_calories_for_goal,
    calculate_macros
)
from utils.meal_generator import generate_meal_plan


# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="AI Meal Plan Generator",
    layout="wide",
    page_icon="🥗"
)

st.title("🥗 AI Meal Plan Generator")
st.write("Get a personalized AI-powered meal plan based on your health profile.")

# ---------------------------------------------------
# SAFE REGEX EXTRACTION
# ---------------------------------------------------
def extract_value(pattern, text, default=None):
    try:
        match = re.search(pattern, text, re.IGNORECASE)
        return match.group(1).strip() if match else default
    except:
        return default


# ---------------------------------------------------
# REMOVE ONLY AI NUTRITION SUMMARY
# ---------------------------------------------------
def remove_nutrition_lines(text):
    return re.sub(
        r"📊 AI Validated Nutrition Summary[\s\S]*?Water Requirement:.*?(?=\n|$)",
        "",
        text,
        flags=re.IGNORECASE
    ).strip()


# ---------------------------------------------------
# SIDEBAR INPUTS
# ---------------------------------------------------
(
    age, weight, height, gender, activity,plan_days,
    disease, diabetes_type, thyroid_type,
    bp_level, cholesterol_level, liver_stage, kidney_stage, gastric_issue,
    state, goal, water_require, diet, allergy, regional,
    breakfast, lunch, dinner, chapati_count,
    eat_rice, rice_type, rice_quantity,
    stress, egg_days, eggs_per_day,
    chicken_days, chicken_grams,
    fish_days, fish_grams,
    milk_glass, milk_type,
    workout_type, workout_duration, oil_preference,
    rice_per_day, paneer_intake, soy_intake,
    eat_out, eat_out_food,
    smoking, alcohol,
    disease_duration, tablet_times
) = sidebar_inputs()



# ---------------------------------------------------
# CACHE MEAL PLAN
# ---------------------------------------------------
@st.cache_data(show_spinner=False)
def cached_generate_meal_plan(*args, **kwargs):
    return generate_meal_plan(*args, **kwargs)


# ---------------------------------------------------
# MAIN APP LOGIC
# ---------------------------------------------------
plan_button_text = f"🚀 Generate {plan_days} Meal Plan"

if st.button(plan_button_text, use_container_width=True):
    if not age or not weight or not height:
        st.error("⚠ Please fill all required personal details.")
        st.stop()

    try:
        workout_duration = workout_duration or 0

        # ---------------- BMI ----------------
        bmi = calculate_bmi(weight, height)

        # ----------- BMR → TDEE → Calories ----
        bmr = calculate_bmr(weight, height, age, gender)
        tdee = calculate_tdee(bmr, activity, workout_duration)
        calories = adjust_calories_for_goal(tdee, goal)

        # ---------------- MACROS --------------
        initial_macros = calculate_macros(
            weight=weight,
            calories=calories,
            activity=activity,
            goal=goal,
            workout_minutes=workout_duration
        )

        protein_target = initial_macros["protein_g"]

        # ------------ CALL GEMINI -------------
        with st.spinner("⏳ Creating your personalized meal plan..."):
            ai_output = cached_generate_meal_plan(
                age, weight, height, gender, activity,plan_days,
                disease, diabetes_type, thyroid_type,
                bp_level, cholesterol_level, liver_stage, kidney_stage, gastric_issue,
                state, goal, water_require, diet, allergy, regional,
                breakfast, lunch, dinner, chapati_count,
                eat_rice, rice_type, rice_quantity,
                stress, egg_days, eggs_per_day,
                chicken_days, chicken_grams,
                fish_days, fish_grams,
                milk_glass, milk_type,
                workout_type, workout_duration, oil_preference,
                eat_out_food, smoking, alcohol,
                disease_duration, tablet_times,
                rice_per_day, paneer_intake, soy_intake,
                calories=calories,
                macros=initial_macros,
                protein_target=protein_target
            )

        if not ai_output or len(ai_output.strip()) < 50:
            st.error("❌ AI failed to generate a valid plan. Try again.")
            st.stop()

        # -------- EXTRACT FINAL VALUES --------
        calories_ai = calories
        protein_ai  = initial_macros["protein_g"]
        carbs_ai    = initial_macros["carbs_g"]
        fats_ai     = initial_macros["fats_g"]
        water_ai    = water_require


        calories_ai = int(float(calories_ai))
        protein_ai  = float(protein_ai)
        carbs_ai    = float(carbs_ai)
        fats_ai     = float(fats_ai)

        # -------- CLEAN OUTPUT TEXT ----------
        meal_plan_clean = remove_nutrition_lines(ai_output)

        # ------------- DISPLAY ---------------
        st.success("🎯 Meal Plan Generated Successfully!")

        st.subheader("📊 Your AI Verified Nutrition Summary")
        st.markdown(f"""
| Metric | Value |
|--------|-------|
| **Goal** | `{goal}` |
| **BMI** | `{bmi}` |
| **Calories/day** | `{calories}` kcal |
| **Protein/day** | `{initial_macros["protein_g"]} g` |
| **Carbs/day** | `{initial_macros["carbs_g"]} g` |
| **Fats/day** | `{initial_macros["fats_g"]} g` |
| **Water Requirement** | `{water_require}` L |
""")


        st.write("---")
        st.markdown(meal_plan_clean)

    except Exception as e:
        st.error("❌ Unexpected Error Occurred!")
        st.exception(e)


# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.info("👉 Fill all inputs from the sidebar and click **Generate** to get your customized diet plan.")
