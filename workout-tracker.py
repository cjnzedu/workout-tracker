def main():
    workouts = []
    while True:
        show_menu()
        choice = input("What do you want to do:  ")
        if choice == "1":
            add_workout(workouts)
        elif choice == "2":
            view_workouts(workouts)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid Option")

def show_menu():
    print("\nWorkout Tracker")
    print("1. Add Workout")
    print("2. View Workouts")
    print("3. Quit")
        

def add_workout(workouts):
    print("Add Workouts Selected")
    while True:
        exercise = input("What Exercise do you want to add: ").strip()
        if exercise:
            break
        print("Enter a valid exercise name")
    
    sets = get_positive_number("Sets: ")
    reps = get_positive_number("Reps: ")
    weight = get_positive_number("Weight: ")

    workout = {
        "exercise": exercise,
        "sets": sets,
        "reps": reps,
        "weight": weight
    }
    workouts.append(workout)
    print("Workout Added!")

def view_workouts(workouts):
    print("View Workouts Selected")
    if not workouts:
        print("No workouts added yet...")
        return
    for index, workout in enumerate(workouts, start=1):
        print(f"{index}. {workout['exercise']} {workout['sets']} x {workout['reps']} @{workout['weight']} lbs")

def get_positive_number(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num <= 0:
                other = prompt.strip(" :")
                print(f"{other} must be greater than 0...")
            else:
                return num
        except ValueError:
            print("Please enter a whole number")


main()