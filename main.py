habit_data = []

while True:
    print("\n=== Habit Tracker ===")
    print("1. Add Today's Habits")
    print("2. View Summary")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        water = input("How many glasses of water did you drink today? ")
        sleep = input("How many hours did you sleep? ")
        exercise = input("Minutes of exercise today: ")

        record = {
            "Water": water,
            "Sleep": sleep,
            "Exercise": exercise
        }

        habit_data.append(record)
        print("Habits saved successfully!")

    elif choice == "2":
        print("\n=== Summary ===")
        if len(habit_data) == 0:
            print("No records found.")
        else:
            for i, day in enumerate(habit_data, start=1):
                print(f"Day {i}: Water = {day['Water']} glasses, Sleep = {day['Sleep']} hrs, Exercise = {day['Exercise']} mins")

    elif choice == "3":
        print("Thank you for using the Habit Tracker!")
        break

    else:
        print("Invalid choice, please try again.")
