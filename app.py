import streamlit as st
from workout_tracker import load_workouts, save_workouts
from datetime import date
workouts = load_workouts()

st.title("Workout Tracker")

with st.form("add_workout_form"):
    st.subheader("Add Workout")

    exercise = st.text_input("Exercise")
    sets = st.number_input("Sets", min_value=1, step=1)
    reps = st.number_input("Reps", min_value=1, step=1)
    weight = st.number_input("Weight", min_value=0, step=5)
    
    submitted = st.form_submit_button("Add Workout")

if submitted:
    workout = {
        "exercise": exercise,
        "sets": sets,
        "reps": reps,
        "weight": weight,
        "date": str(date.today())
    }
    workouts.append(workout)
    st.write(exercise, sets, reps, weight)
    st.success("Workout added successfully!")
    save_workouts(workouts)
    