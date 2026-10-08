import streamlit as st
from workout_tracker import load_workouts, save_workouts, calculate_volume
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
    if not exercise.strip():
        st.error("Please enter an exercise name.")
    else:
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

st.subheader("Workout History")
if not workouts:
    st.info("No workouts added yet.")
else:
    for workout in workouts:
        workout["volume"] = calculate_volume(workout)
    st.dataframe(workouts)


workout_options = []

for workout in workouts:
    # Create a label using an f-string
    label = f"{workout['exercise']} — {workout['sets']} x {workout['reps']} @ {workout['weight']} lbs"
    # Add the label to workout_options
    workout_options.append(label)
if workouts:
    st.subheader("Delete Workout")
    selected = st.selectbox("Choose a workout", options=range(len(workout_options)),
    format_func=lambda i: workout_options[i])
    if st.button("Delete Workout"):
        deleted_workout = workouts.pop(selected)
        save_workouts(workouts)
        #st.success(f"Deleted {deleted_workout['exercise']}!")
        st.rerun()

