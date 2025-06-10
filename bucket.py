import streamlit as st

# GUI title
st.title("Livstidskalkulator for sædvolum")

# Intro text
st.markdown(
    """
    🤔 **Kor mange gonger pr. veke?**  
    Her kan du rekne ut omtrent kor mykje sæd ein mann vil ejakulere i løpet av eit liv, basert på vanleg frekvens per veke.
    
    **Merk:** Dette er berre eit overslag basert på gjennomsnittstal.
    """
)

# Input from user
freq_per_week = st.slider("Kor mange gonger pr. veke?", min_value=0, max_value=30, value=3)

# Constants
years = 60  # 15 to 75 years old
weeks_per_year = 52
ejaculate_volume_ml = 3.5  # average per ejaculation
ml_per_liter = 1000

# Calculation
total_ejaculations = freq_per_week * weeks_per_year * years
total_volume_ml = total_ejaculations * ejaculate_volume_ml
total_volume_liters = total_volume_ml / ml_per_liter

# Output
st.subheader("Resultat:")
st.write(f"Totalt antal utløysingar i livet: **{total_ejaculations:,}**")
st.write(f"Forventa mengde sæd i liter: **{total_volume_liters:.2f} liter**")
st.write(f"Eller  **{total_volume_liters/10:.2f} bøtter**")
