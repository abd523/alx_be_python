task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

reminder = f"Note: '{task}' is a {priority} priority task"

match priority:
    case "high":
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Please aim to complete it soon."
    case "medium":
        if time_bound == "yes":
            reminder += " that should be addressed today."
        else:
            reminder += ". Plan to work on it soon."
    case "low":
        if time_bound == "yes":
            reminder += " but needs attention today."
        else:
            reminder += ". Consider completing it when you have free time."
    case _:
        reminder = f"Error: Invalid priority level for '{task}'. Please use high, medium, or low."

print(reminder)