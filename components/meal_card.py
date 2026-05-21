# components/meal_card.py
import streamlit as st

def show_meal_card(title, content):
    st.markdown(f"### 🍽️ {title}")
    st.info(content)
