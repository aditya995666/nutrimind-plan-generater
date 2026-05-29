import streamlit as st

def get_inputs_form():
    with st.form("child_form"):

        st.header("👶 Child Profile")
        age = st.number_input("Age (years)", 1, 18)
        gender = st.selectbox("Gender", ["Male", "Female"])

        col1, col2 = st.columns(2)
        with col1:
            height = st.number_input("Height (cm)", 50, 200)
        with col2:
            weight = st.number_input("Weight (kg)", 5, 100)

        # ---------------- Behaviour ----------------
        st.header("🧠 Behaviour Patterns")
        behaviour = st.multiselect(
            "Observed Eating Patterns",
            [
                "Picky Eater",
                "Skips Breakfast",
                "Overeats Snacks",
                "Prefers Taste Over Nutrition",
                "Irregular Meal Schedule",
                "Frequent Packaged Foods",
                "Good Eating Habits"
            ]
        )

        # ---------------- Goals ----------------
        st.header("🎯 Primary Goal")
        goals = st.multiselect(
            "Select goals:",
            [
                "Healthy growth",
                "Improve immunity",
                "Increase weight",
                "Reduce junk habits",
                "Manage medical condition"
            ]
        )

        # ---------------- Diet Preferences ----------------
        diet_type = st.selectbox(
            "Diet Type",
            ["Vegetarian", "Eggetarian", "Non-Vegetarian", "Jain"]
        )

        food_region = st.selectbox(
            "Preferred Regional Cuisine",
            ["North Indian", "South Indian", "Gujarati", "Bengali", "Rajasthani", "Mixed"]
        )

        sleep_hours = st.slider("Average Sleep per day (hours)", 5, 12, 9)

        activity_level = st.selectbox(
            "Physical Activity Level",
            ["Light", "Moderate", "High"]
        )

        # ---------------- Milk & Food Intake (NEW) ----------------
        st.header("🥛 Daily Intake")

        milk_qty = st.slider(
            "Milk Intake per day (ml)",
            min_value=0,
            max_value=1000,
            value=250,
            step=50
        )

        food_intake = st.selectbox(
            "Daily Fruit / Healthy Food Intake",
            [
                "None",
                "1 serving",
                "2 servings",
                "3+ servings"
            ]
        )

        # ---------------- Allergies ----------------
        allergies = st.multiselect(
            "Food Allergies",
            ["Milk/Dairy", "Nuts", "Egg", "Gluten/Wheat", "Soy", "Fish", "None"]
        )

        # ---------------- Food Recall ----------------
        st.header("⏰ 24-Hour Food Recall")
        breakfast = st.text_input("Breakfast (What & When?)")
        school_snack = st.text_input("School Lunchbox / Snacks")
        lunch_lunch = st.text_input("Lunch")
        dinner = st.text_input("Dinner")

        submitted = st.form_submit_button("🎯 Generate Child Diet Plan", use_container_width=True)

        if submitted:
            allergies = [a for a in allergies if a != "None"]

            return {
                "age": age,
                "gender": gender,
                "height_cm": height,
                "weight_kg": weight,
                "behaviour": behaviour,
                "goals": goals,
                "diet_type": diet_type,
                "food_region": food_region,
                "sleep_hours": sleep_hours,
                "activity_level": activity_level,
                "milk_qty": milk_qty,              # ✅ added
                "food_intake": food_intake,        # ✅ added
                "allergies": allergies,
                "breakfast": breakfast,
                "school_tiffin": school_snack,
                "lunch": lunch_lunch,
                "dinner": dinner
            }

    return None
