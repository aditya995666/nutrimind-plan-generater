import streamlit as st

def sidebar_inputs():
    st.sidebar.header("🧍 User Profile")

    # --- Personal Info ---
    age = st.sidebar.number_input("Age", 10, 100, 25)
    weight = st.sidebar.number_input("Weight (kg)", 20.0, 200.0, 70.0)
    height = st.sidebar.number_input("Height (cm)", 100.0, 250.0, 170.0)
    gender = st.sidebar.selectbox("Gender", ["male", "female"])
    activity = st.sidebar.selectbox("Activity Level", ["low", "medium", "high"])
    goal = st.sidebar.selectbox(
        "Goal Type",
        ["Weight Loss", "Weight Gain", "Muscle Gain", "Fat Loss", "PCOS Reversal",
         "Diabetes Control", "Thyroid Support", "Gut Health", "Maintenance", "Cholesterol Control"]
    )
    allergy = st.sidebar.selectbox(
        "Food Allergies",
        ["None", "Dairy-Free", "Gluten-Sensit   ivity", "Peanut-Allergy", "Lactose Intolerant", "Seafood Allergy"]
    )
    regional = st.sidebar.selectbox(
        "Regional Cuisine Preference",
        ["North Indian", "South Indian", "East Indian", "West Indian", "No Preference"]
    )

    # --- Medical Conditions ---
    disease = st.sidebar.selectbox(
        "Select Disease",
        ["None", "Diabetes", "PCOS/PCOD", "Fat Loss / Overweight", "Fatty Liver",
         "Acidity / Gas", "Thyroid", "Kidney", "Heart"]
    )
    diabetes_type = thyroid_type = bp_level = cholesterol_level = liver_stage = kidney_stage = gastric_issue = "None"
    if disease == "Diabetes":
        diabetes_type = st.sidebar.selectbox("Diabetes Type", ["Type 1", "Type 2", "Prediabetes"])
    if disease == "Thyroid":
        thyroid_type = st.sidebar.selectbox("Thyroid Type", ["Hypothyroid", "Hyperthyroid"])
    if disease in ["Heart", "Fat Loss / Overweight"]:
        bp_level = st.sidebar.selectbox("BP Level", ["Normal", "High", "Low"])
    if disease in ["Cholesterol Control", "Heart", "Fat Loss / Overweight"]:
        cholesterol_level = st.sidebar.selectbox("Cholesterol Level", ["High", "Borderline", "Normal"])
    if disease == "Fatty Liver":
        liver_stage = st.sidebar.selectbox("Fatty Liver Grade", ["Grade 1", "Grade 2", "Grade 3"])
    if disease == "Kidney":
        kidney_stage = st.sidebar.selectbox("CKD Stage", ["Stage 1", "Stage 2", "Stage 3", "Stage 4", "Stage 5"])
    if disease in ["Acidity / Gas", "Gut Health"]:
        gastric_issue = st.sidebar.selectbox("Gastric Issue", ["Acidity", "IBS", "Constipation"])

    state = st.sidebar.selectbox(
        "Select State",
        ["UP", "Delhi", "Punjab", "Gujarat", "Bihar", "Rajasthan",
         "South India", "Maharashtra", "Tamil Nadu", "Karnataka", "West Bengal", "Madhya Pradesh"]
    )
    # Disease Duration
    disease_duration = "None"
    if disease != "None":
        disease_duration = st.sidebar.selectbox(
        "Disease Duration",
        ["< 6 months", "6 months - 1 year", "1-3 years", "3-5 years", "5+ years"]
    )
    plan_days = st.sidebar.selectbox(
    "Meal Plan Duration",
    ["3 Days", "7 Days"]
)
    # --- Diet & Workout ---
    diet = st.sidebar.selectbox("Diet Type", ["Vegetarian", "Non-Vegetarian", "Vegan", "Eggetarian"])
    workout_type = st.sidebar.selectbox("Workout", ["Cardio", "Strength", "Yoga", "No Workout"])
    workout_duration = st.sidebar.number_input("Workout Duration (min/day)", 0, 180, 30)
    oil_preference = st.sidebar.selectbox("Preferred Cooking Oil", ["Mustard", "Olive", "Sunflower", "Ghee"])
    stress = st.sidebar.selectbox("Stress Level", ["Low", "Medium", "High"])

    # --- Food Habits ---
    breakfast = st.sidebar.text_input("Breakfast", "")
    lunch = st.sidebar.text_input("Lunch", "")
    dinner = st.sidebar.text_input("Dinner", "")

    # Chapati
    chapati_choice = st.sidebar.selectbox("Chapati Per Day", ["0", "1-2", "3-4", "5+"])
    chapati_map = {"0": 0, "1-2": 2, "3-4": 4, "5+": 6}
    chapati_count = chapati_map[chapati_choice]

    # Rice
    eat_rice = st.sidebar.selectbox("Do you eat Rice?", ["yes", "no"])
    rice_type = rice_quantity = "None"
    rice_per_day = 0
    if eat_rice == "yes":
        rice_type = st.sidebar.selectbox("Rice Type", ["white", "brown", "steamed", "basmati"])
        rice_quantity = st.sidebar.selectbox("Rice Quantity", ["1/2 plate", "1 plate", "2 plates"])
        rice_per_day = st.sidebar.number_input("Rice Times/Day", 0, 3, 1)

    # Paneer / Soy
    paneer_map = {"None": 0, "1-2 times": 2, "3-5 times": 4, "Daily": 7}
    soy_map = paneer_map
    paneer_intake = soy_intake = 0
    if diet in ["Vegetarian", "Vegan", "Eggetarian"]:
        paneer_intake = paneer_map[st.sidebar.selectbox("Paneer Intake", paneer_map.keys())]
        soy_intake = soy_map[st.sidebar.selectbox("Soy/Tofu Intake", soy_map.keys())]

    # Eggs
    if diet in ["Non-Vegetarian", "Eggetarian"]:
        egg_days = st.sidebar.number_input("Egg Eating Days/Week", 0, 7, 3)
        eggs_per_day = st.sidebar.number_input("Eggs Per Day", 0, 6, 2)
    else:
        egg_days = eggs_per_day = 0

    # Chicken
    if diet == "Non-Vegetarian":
        chicken_days = st.sidebar.number_input("Chicken Days/Week", 0, 7, 2)
        chicken_grams = st.sidebar.selectbox("Chicken Quantity", ["50g", "100g", "150g", "200g"])
    else:
        chicken_days, chicken_grams = 0, "0g"

    # Fish
    if diet == "Non-Vegetarian":
        fish_days = st.sidebar.number_input("Fish Days/Week", 0, 7, 1)
        fish_grams = st.sidebar.selectbox("Fish Quantity", ["50g", "100g", "150g", "200g"])
    else:
        fish_days, fish_grams = 0, "0g"

    # Milk
    if allergy != "Lactose Intolerant":
        milk_glass = st.sidebar.number_input("Milk Glass/day", 0, 5, 1)
        milk_type = st.sidebar.selectbox("Milk Type", ["Low Fat", "Full Cream"])
    else:
        milk_glass, milk_type = 0, "None"

    # Eating Out
    # Eating Out Details
    # Eating Out Frequency
    eat_out = st.sidebar.number_input(
    "how  many time eat outside/day",
    0, 14, 0
)

# Eating Outside Food (ONLY if eats outside)
    eat_out_food = "None"
    if eat_out > 0:
        eat_out_food = st.sidebar.text_input(
        "What do you usually eat outside?",
        placeholder="e.g. Burger, Pizza, Chaat, Biryani"
    )

    # Smoking & Alcohol
    smoking = st.sidebar.selectbox(
    "Smoking Habit",
    ["No", "Occasionally", "Daily"]
)

    alcohol = st.sidebar.selectbox(
    "Alcohol Consumption",
    ["No", "Occasionally", "Weekly", "Daily"]
)

    # Medicine Intake (Written / Text)
    tablet_times = "None"
    if disease != "None":
        tablet_times = st.sidebar.text_input(
        "How many times do you take medicine per day?",
        placeholder="e.g. Once, Twice, Morning & Night, 3 times"
    )

    water_require = round(weight * 0.035, 2)
    st.sidebar.info(f"💧 Drink approx {water_require} Liters/day")

    return (
    age, weight, height, gender, activity,plan_days,
    disease, diabetes_type, thyroid_type,
    bp_level, cholesterol_level, liver_stage, kidney_stage, gastric_issue,
    state, goal, water_require, diet, allergy, regional,

    breakfast, lunch, dinner,
    chapati_count,
    eat_rice, rice_type, rice_quantity,
    stress,

    egg_days, eggs_per_day,
    chicken_days, chicken_grams,
    fish_days, fish_grams,

    milk_glass, milk_type,

    workout_type, workout_duration, oil_preference,

    rice_per_day, paneer_intake, soy_intake,

    eat_out, eat_out_food,

    smoking, alcohol,

    disease_duration, tablet_times
)

