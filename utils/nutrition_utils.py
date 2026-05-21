def calculate_bmi(weight, height_cm):
    """Calculate BMI."""
    height_m = height_cm / 100
    return round(weight / (height_m ** 2), 1)



def calculate_bmr(weight, height_cm, age, gender):
    """
    BMR using Mifflin–St Jeor Equation.
    Most accurate for modern humans.
    """
    gender = gender.lower()

    if gender == "male":
        return round((10 * weight) + (6.25 * height_cm) - (5 * age) + 5, 1)
    else:
        return round((10 * weight) + (6.25 * height_cm) - (5 * age) - 161, 1)



def calculate_tdee(bmr, activity, workout_minutes):
    """
    TDEE = BMR × Activity Factor + Workout Calories
    Workout calories = 8 kcal/min
    """

    activity_map = {
        "low": 1.1,
        "medium": 1.3,
        "high": 1.5
    }

    # fallback value
    factor = activity_map.get(activity.lower(), 1.3)

    workout_calories = workout_minutes * 8

    return round((bmr * factor) + workout_calories, 1)



def adjust_calories_for_goal(tdee, goal):
    """
    Adjust calories depending on user goal (gain, loss, maintenance).
    Includes strict minimum and maximum calorie limits.
    """

    goal = goal.lower()

    MIN_CAL = 1200
    MAX_CAL = 4000

    if "loss" in goal or "fat" in goal:
        calories = tdee * 0.80   # 20% deficit
    elif "muscle" in goal:
        calories = tdee * 1.15   # 15% surplus
    elif "gain" in goal:
        calories = tdee * 1.10
    else:
        calories = tdee

    calories = round(calories, 1)

    # Avoid extreme calories
    calories = max(MIN_CAL, min(calories, MAX_CAL))

    return calories



def calculate_macros(weight, calories, activity, goal, workout_minutes):
    """
    Updated & scientifically correct macro calculation:
    - Protein increases with activity, workout, and goal
    - Fats = 25% of total calories
    - Carbs = remaining calories + workout carbs
    """

    activity = activity.lower()

    activity_map = {
        "low": 1.0,        # sedentary
        "medium": 1.2,     # light active
        "high": 1.4        # highly active
    }

    activity_factor = activity_map.get(activity, 1.2)

    # -------------------------------
    # 2️⃣ GOAL MULTIPLIER
    # -------------------------------
    goal = goal.lower()

    if "muscle" in goal or "gain" in goal:
        goal_factor = 0.4     # extra protein for gaining
    elif "loss" in goal or "fat" in goal:
        goal_factor = 0.1     # slight increase for fat loss
    else:
        goal_factor = 0.2     # maintenance

    # -------------------------------
    # 3️⃣ WORKOUT MULTIPLIER
    # -------------------------------
    # Gym/shred coaches use 0.15g per minute
    workout_factor = workout_minutes * 0.15 / weight

    # -------------------------------
    # 4️⃣ FINAL PROTEIN MULTIPLIER
    # -------------------------------
    final_multiplier = activity_factor + goal_factor + workout_factor

    protein_g = round(weight * final_multiplier, 1)

  

    protein_calories = protein_g * 4

    # -------------------------------
    # 5️⃣ FAT (minimum g/kg based)
    # -------------------------------
    if "loss" in goal or "fat" in goal:
        fats_g = (calories * 0.22) / 9
    elif "muscle" in goal or "gain" in goal:
        fats_g = (calories * 0.28) / 9
    else:
        fats_g = (calories * 0.25) / 9

# safety minimum
    fats_g = max(fats_g, weight * 0.6)
    fats_g = round(fats_g, 1)
    fat_calories = fats_g * 9


    # -------------------------------
    # 6️⃣ CARBS (controlled)
    # -------------------------------
    # ------------------------------- 
# CARBS (controlled)
# -------------------------------
    carbs_calories = calories - (protein_calories + fat_calories)

    carb_limit_map = {
        "loss": 0.40,
        "fat": 0.40,
        "maintenance": 0.50,
        "muscle": 0.55,
        "gain": 0.55
    }

    max_carb_percent = 0.50  # default
    for key, value in carb_limit_map.items():
        if key in goal:
            max_carb_percent = value
            break

    max_carbs_cal = calories * max_carb_percent
    if carbs_calories > max_carbs_cal:
        carbs_calories = max_carbs_cal

    # safety fallback
    if carbs_calories < 0:
        carbs_calories = calories * 0.15

    carbs_g = round(carbs_calories / 4, 1)

    return {
        "protein_g": protein_g,
        "carbs_g": carbs_g,
        "fats_g": fats_g
    }