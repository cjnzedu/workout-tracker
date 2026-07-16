import json

def main():
    workouts = load_workouts()
    while True:
        show_menu()
        choice = input("What do you want to do:  ")
        if choice == "1":
            add_workout(workouts)
        elif choice == "2":
            view_workouts(workouts)
        elif choice == "3":
            delete_workout(workouts)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid Option")

def show_menu():
    print("\nWorkout Tracker")
    print("1. Add Workout")
    print("2. View Workouts")
    print("3. Delete Workout")
    print("4. Quit")
        

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
    save_workouts(workouts)
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
                field_name = prompt.strip(" :")
                print(f"{field_name} must be greater than 0...")
            else:
                return num
        except ValueError:
            print("Please enter a whole number")

def save_workouts(workouts):
    with open("workouts.json", "w") as file:
        json.dump(workouts, file, indent=4)

def load_workouts():
    try:
        with open("workouts.json", "r") as file:
            workouts = json.load(file)
            return workouts
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def delete_workout(workouts):
    if not workouts:
        print("No workouts to delete...")
        return
    
    view_workouts(workouts)
    while True:
        try:
            choice = int(input("Delete workout number: "))
            if choice > len(workouts):
                print("\nThere's not that many workouts")
            elif choice < 1:
                print("\nInvalid Workout number")
            else:
                deleted = workouts.pop(choice - 1)
                save_workouts(workouts)
                print(f"Successfully deleted {deleted['exercise']}")
                view_workouts(workouts)
                return
        except ValueError:
            print("\nInvalid workout number.")
    

if __name__ == "__main__":
    main()