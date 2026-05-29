import streamlit as st
import re
from fpdf import FPDF
import tempfile
import traceback

# ==================================================
# CUSTOM CSS STYLING - DARK MODE
# ==================================================
st.markdown("""
<style>
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main background - Dark Black */
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%);
    }
    
    /* Main container */
    .main {
        max-width: 1400px;
        margin: 0 auto;
    }
    
    /* Hero Section - Neon Green */
    .hero {
        text-align: center;
        padding: 50px 20px;
        background: linear-gradient(135deg, #00b894 0%, #009432 100%);
        border-radius: 20px;
        margin-bottom: 30px;
        color: white;
        box-shadow: 0 10px 30px rgba(0,184,148,0.3);
    }
    
    .hero h1 {
        font-size: 2.8rem;
        margin-bottom: 10px;
        font-weight: 800;
        letter-spacing: -0.5px;
    }
    
    .hero p {
        font-size: 1.2rem;
        opacity: 0.95;
    }
    
    /* Stats Container */
    .stats-container {
        background: #1e1e2e;
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.3);
        margin-bottom: 25px;
        border: 1px solid #00b894;
    }
    
    /* Feature Cards - Equal Size */
    .feature-card {
        background: #1e1e2e;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        transition: all 0.3s ease;
        border: 1px solid #00b894;
        height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0,184,148,0.2);
        border-color: #00ffb3;
    }
    
    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 15px;
    }
    
    .feature-title {
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 8px;
        color: #00b894;
    }
    
    .feature-desc {
        font-size: 0.85rem;
        color: #a0a0b0;
    }
    
    /* Radio Button Styling */
    .stRadio > div {
        gap: 20px;
        justify-content: center;
        background: #1e1e2e;
        padding: 12px;
        border-radius: 50px;
        border: 1px solid #00b894;
    }
    
    .stRadio label {
        background: #2a2a3e;
        padding: 10px 35px;
        border-radius: 40px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        color: #ffffff;
    }
    
    .stRadio label:hover {
        background: #00b894;
        color: white;
    }
    
    /* Gradient Button - Neon Green */
    .stButton > button {
        background: linear-gradient(135deg, #00b894 0%, #009432 100%);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 14px 30px;
        font-weight: 700;
        font-size: 1rem;
        width: 100%;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 20px rgba(0,184,148,0.5);
    }
    
    /* Sidebar Styling - Dark */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e 0%, #0f0f1a 100%);
        border-right: 1px solid #00b894;
    }
    
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3 {
        color: #00b894;
    }
    
    [data-testid="stSidebar"] label {
        color: #ffffff;
        font-weight: 500;
    }
    
    [data-testid="stSidebar"] .stSelectbox div,
    [data-testid="stSidebar"] .stNumberInput input {
        background: #2a2a3e;
        color: white;
        border-radius: 10px;
    }
    
    /* Metric Cards */
    [data-testid="stMetric"] {
        background: #1e1e2e;
        border-radius: 15px;
        padding: 15px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.3);
        border: 1px solid #00b894;
    }
    
    [data-testid="stMetric"] label {
        color: #00b894;
    }
    
    [data-testid="stMetric"] .stMetricValue {
        color: white;
    }
    
    /* Success Alert */
    .stSuccess {
        background: #0a2e1a;
        border-left: 5px solid #00b894;
        border-radius: 10px;
        padding: 15px;
        color: #00ffb3;
    }
    
    /* Table Styling */
    table {
        width: 100%;
        background: #1e1e2e;
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 2px 10px rgba(0,0,0,0.3);
        border-collapse: collapse;
    }
    
    th {
        background: linear-gradient(135deg, #00b894 0%, #009432 100%);
        color: white;
        padding: 12px;
        font-weight: 700;
    }
    
    td {
        padding: 10px;
        border-bottom: 1px solid #2a2a3e;
        color: #e0e0e0;
        background: #1e1e2e;
    }
    
    tr:hover td {
        background: #2a2a3e;
    }
    
    /* Text Colors */
    .stMarkdown {
        color: #e0e0e0;
    }
    
    p, li, span {
        color: #e0e0e0;
    }
    
    /* Divider */
    hr {
        margin: 25px 0;
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, #00b894, transparent);
    }
    
    /* Info Box */
    .stAlert {
        border-radius: 12px;
        border-left: 4px solid #00b894;
        background: #1a1a2e;
        color: #e0e0e0;
    }
    
    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        color: #00b894;
    }
    
    /* Subheader */
    .stSubheader {
        color: #00b894;
    }
    
    /* Number Input */
    .stNumberInput input {
        color: white;
    }
    
    /* Selectbox */
    .stSelectbox div {
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ADULT IMPORTS
from components.sidebar import sidebar_inputs
from utils.nutrition_utils import (
    calculate_bmi,
    calculate_bmr,
    calculate_tdee,
    adjust_calories_for_goal,
    calculate_macros
)
from utils.meal_generator import generate_meal_plan

# CHILD IMPORTS
from children.form_inputs import get_inputs_form
from children.prompt_builder import build_prompt as child_build_prompt
from children.gemini_api import call_gemini as child_call_gemini

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="AI Meal Plan Generator",
    layout="wide",
    page_icon="🥗",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# HERO SECTION
# ---------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>🥗 AI Meal Plan Generator</h1>
    <p>Your Personal AI Nutritionist | Smart Meal Planning for a Healthier You</p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# FEATURE CARDS - Equal size columns
# ---------------------------------------------------
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🎯</div>
        <div class="feature-title">Personalized Plans</div>
        <div class="feature-desc">Based on your health profile</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🥗</div>
        <div class="feature-title">Indian Cuisine</div>
        <div class="feature-desc">North & South Indian options</div>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <div class="feature-title">Nutrient Tracked</div>
        <div class="feature-desc">Calories, Protein, Carbs, Fats</div>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">💚</div>
        <div class="feature-title">Health Focused</div>
        <div class="feature-desc">Weight loss & disease management</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ---------------------------------------------------
# RADIO BUTTONS FOR MODE SELECTION
# ---------------------------------------------------
mode = st.radio("", ["👤 Adult Meal Plan", "👶 Child Meal Plan"], horizontal=True)

# ---------------------------------------------------
# INITIALIZE SESSION STATE
# ---------------------------------------------------
if "adult_generated" not in st.session_state:
    st.session_state.adult_generated = False
if "child_generated" not in st.session_state:
    st.session_state.child_generated = False
if "child_response" not in st.session_state:
    st.session_state.child_response = None

# ---------------------------------------------------
# REMOVE NUTRITION SUMMARY (For Adult)
# ---------------------------------------------------
def remove_nutrition_lines(text):
    return re.sub(
        r"📊 AI Validated Nutrition Summary[\s\S]*?Water Requirement:.*?(?=\n|$)",
        "",
        text,
        flags=re.IGNORECASE
    ).strip()

# ---------------------------------------------------
# CACHED FUNCTIONS
# ---------------------------------------------------
@st.cache_data(show_spinner=False)
def cached_generate_meal_plan(*args, **kwargs):
    return generate_meal_plan(*args, **kwargs)

# ==================================================
# ADULT MEAL PLAN
# ==================================================
if mode == "👤 Adult Meal Plan":
    # Clear sidebar and add adult content
    st.sidebar.empty()
    with st.sidebar:
        st.markdown("### 📋 Health Profile")
        st.markdown("---")
        (
            age, weight, height, gender, activity, plan_days,
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

    plan_button_text = f"🚀 Generate {plan_days} Day Meal Plan"

    if st.button(plan_button_text, use_container_width=True, key="adult_gen_btn"):
        if not age or not weight or not height:
            st.error("⚠️ Please fill all required personal details in the sidebar.")
        else:
            st.session_state.adult_generated = True
            st.session_state.child_generated = False

    if st.session_state.adult_generated:
        try:
            workout_duration = workout_duration or 0

            bmi = calculate_bmi(weight, height)
            bmr = calculate_bmr(weight, height, age, gender)
            tdee = calculate_tdee(bmr, activity, workout_duration)
            calories = adjust_calories_for_goal(tdee, goal)

            initial_macros = calculate_macros(
                weight=weight,
                calories=calories,
                activity=activity,
                goal=goal,
                workout_minutes=workout_duration
            )

            protein_target = initial_macros["protein_g"]

            with st.spinner("✨ Creating your personalized meal plan..."):
                ai_output = cached_generate_meal_plan(
                    age, weight, height, gender, activity, plan_days,
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

            meal_plan_clean = remove_nutrition_lines(ai_output)

            st.success("🎉 Meal Plan Generated Successfully!")

            # Stats Container
            st.markdown('<div class="stats-container">', unsafe_allow_html=True)
            st.subheader("📊 Nutrition Summary")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("🎯 Goal", goal)
                st.metric("📊 BMI", f"{bmi:.1f}")
            with col2:
                st.metric("🔥 Daily Calories", f"{calories:.0f} kcal")
                st.metric("💪 Daily Protein", f"{initial_macros['protein_g']:.0f} g")
            with col3:
                st.metric("🍚 Daily Carbs", f"{initial_macros['carbs_g']:.0f} g")
                st.metric("🥑 Daily Fats", f"{initial_macros['fats_g']:.0f} g")
            with col4:
                st.metric("💧 Water Intake", f"{water_require} L")
                st.metric("📅 Plan Duration", f"{plan_days} Days")
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown("---")
            st.subheader("🍽️ Your Personalized Meal Plan")
            st.markdown(meal_plan_clean, unsafe_allow_html=True)

            # PDF Download
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", "B", 16)
            pdf.cell(200, 10, "AI Meal Plan", ln=True, align="C")
            pdf.ln(10)
            pdf.set_font("Arial", "B", 12)
            pdf.cell(200, 10, "Nutrition Summary", ln=True)
            pdf.set_font("Arial", size=11)
            summary = f"""
Goal: {goal}
BMI: {bmi:.1f}
Calories: {calories:.0f}
Protein: {initial_macros['protein_g']:.0f} g
Carbs: {initial_macros['carbs_g']:.0f} g
Fats: {initial_macros['fats_g']:.0f} g
Water: {water_require} L
"""
            pdf.multi_cell(0, 8, summary)
            pdf.ln(5)
            pdf.set_font("Arial", "B", 12)
            pdf.cell(200, 10, "Meal Plan", ln=True)
            pdf.set_font("Arial", size=10)
            safe_text = meal_plan_clean.encode("latin-1", "ignore").decode("latin-1")
            pdf.multi_cell(0, 7, safe_text)
            pdf_data = pdf.output(dest="S").encode("latin-1")

            col1, col2, col3 = st.columns([1,2,1])
            with col2:
                st.download_button(
                    label="📥 Download as PDF",
                    data=pdf_data,
                    file_name="meal_plan.pdf",
                    mime="application/pdf",
                    key="adult_pdf",
                    use_container_width=True
                )

            if st.button("🔄 Start New Plan", key="adult_reset", use_container_width=True):
                st.session_state.adult_generated = False
                st.rerun()

        except Exception as e:
            st.error("❌ Unexpected Error Occurred!")
            st.exception(e)

# ==================================================
# CHILD MEAL PLAN
# ==================================================
else:
    # Clear sidebar and add child content only
    st.sidebar.empty()
    with st.sidebar:
        st.markdown("### 👶 Child Mode")
        st.markdown("---")
        st.info("📋 Fill the form below to generate your child's personalized diet plan.")
        st.markdown("")
        st.markdown("**Child Guidelines:**")
        st.markdown("- ✅ No calorie calculations")
        st.markdown("- ✅ Focus on growth & immunity")
        st.markdown("- ✅ Indian household foods")
        st.markdown("- ✅ 3-Day plan only")
    
    st.subheader("🍎 AI Child Diet Planner")
    st.caption("ICMR/NIN Aligned • Parent Friendly")
    
    st.info(
        "✨ This tool generates a **3-Day AI-validated child diet plan**.\n\n"
        "✔ Child-specific nutrition guidelines\n"
        "✔ Indian household based & parent-safe\n"
        "✔ Focus on growth, immunity & healthy eating habits"
    )

    child_data = get_inputs_form()
    
    if child_data:
        with st.spinner("✨ Preparing your child's diet plan..."):
            try:
                child_prompt = child_build_prompt(child_data)
                child_response = child_call_gemini(child_prompt)
                
                if child_response and len(child_response.strip()) > 50:
                    st.success("🎉 Your Child's Diet Plan is Ready!")
                    st.divider()
                    st.markdown(child_response, unsafe_allow_html=True)
                    
                    pdf = FPDF()
                    pdf.add_page()
                    pdf.set_font("Arial", "B", 16)
                    pdf.cell(200, 10, "AI Child Diet Plan", ln=True, align="C")
                    pdf.ln(10)
                    pdf.set_font("Arial", size=10)
                    safe_text = child_response.encode("latin-1", "ignore").decode("latin-1")
                    pdf.multi_cell(0, 7, safe_text)
                    pdf_data = pdf.output(dest="S").encode("latin-1")

                    col1, col2, col3 = st.columns([1,2,1])
                    with col2:
                        st.download_button(
                            label="📥 Download as PDF",
                            data=pdf_data,
                            file_name="child_diet_plan.pdf",
                            mime="application/pdf",
                            key="child_pdf",
                            use_container_width=True
                        )
                else:
                    st.error("❌ AI failed to generate a valid child diet plan. Please try again.")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.code(traceback.format_exc())

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("---")
st.markdown("<p style='text-align: center; color: #00b894;'>© 2024 AI Meal Plan Generator | Powered by Groq AI</p>", unsafe_allow_html=True)