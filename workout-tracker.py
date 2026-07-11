workouts = []

while True:
    print("\nWorkout Tracker")
    print("1. Add Workout")
    print("2. View Workouts")
    print("3. Quit")

    choice = input("What do you want to do:  ")

    if choice == "1":
        print("Add Workouts Selected")
        exercise = input("What Exercise do you want to add: ")
        sets = int(input("Sets: "))
        reps = int(input("Reps: "))
        weight = int(input("Weight: "))

        workout = {
            "exercise": exercise,
            "sets": sets,
            "reps": reps,
            "weight": weight
        }
        workouts.append(workout)
        print("Workout Added!")

    elif choice == "2":
        print("View Workouts Selected")
        if len(workouts) == 0:
            print("No workouts added yet...")
        for index, workout in enumerate(workouts, start=1):
            print(f"{index}. {workout['exercise']} {workout['sets']} x {workout['reps']} @{workout['weight']} lbs")

    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid Choice!")