import streamlit as st
from components.form_inputs import get_inputs_form
from utils.prompt_builder import build_prompt
from utils.gemini_api import call_gemini
import traceback

#
# 
st.set_page_config(
    page_title="AI Child Diet Planner",
    page_icon="🍎",
    layout="wide"
)

# ---------------- Main App ----------------
def main():
    st.title("🍎 AI Child Diet Planner")
    st.caption("ICMR/NIN Aligned • Backend Controlled • Parent Friendly")

    st.info(
        "🧠 This tool generates a **STRICT 3-Day AI-validated child diet plan**.\n\n"
        "✔ Calories & macros are calculated in backend only\n"
        "✔ AI is NOT allowed to recalculate nutrition\n"
        "✔ BMI is used **only for health status reference**\n"
        "✔ Diet is Indian household based & parent-safe"
    )

    # -------- Collect Input --------
    data = get_inputs_form()
    if not data:
        st.warning("👆 Please fill the form and click **Generate Diet Plan**")
        return

    st.divider()
    st.subheader("🤖 AI Pediatric Nutritionist at Work")

    # -------- AI Generation --------
    with st.spinner("⏳ Preparing a clinically aligned 3-day diet plan..."):
        try:
            prompt = build_prompt(data)
            response = call_gemini(prompt)
        except Exception:
            st.error("❌ Error while generating the diet plan.")
            st.code(traceback.format_exc())
            return

    # -------- Output --------
    st.success("🎉 Your Child’s 3-Day Diet Plan is Ready!")
    st.markdown(response, unsafe_allow_html=True)

    # -------- Download --------
    st.download_button(
        label="📥 Download Diet Plan (Text)",
        data=response,
        file_name="child_3_day_diet_plan.txt",
        mime="text/plain"
    )

    # -------- Debug / Transparency --------
    with st.expander("🔍 View AI Prompt (For Clinical Review)"):
        st.code(prompt, language="markdown")


# ---------------- Run App ----------------
if __name__ == "__main__":
    main()
