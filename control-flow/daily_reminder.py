```python
def daily_reminder():
    # Prompt user for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Initialize reminder message
    reminder = f"Reminder: '{task}' is a {priority} priority task"

    # Use match case to handle priority levels
    match priority:
        case "high":
            reminder += " that should be addressed promptly"
        case "medium":
            reminder += " that can be handled with moderate urgency"
        case "low":
            reminder += ". Consider completing it when you have free time"
        case _:
            reminder = f"Reminder: '{task}' has an invalid priority level. Please use high, medium, or low"
            print(reminder)
            return

    # Check if task is time-bound
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    elif time_bound == "no" and priority != "low":
        reminder += " today."
    elif time_bound != "no":
        reminder = f"Reminder: '{task}' has an invalid time-bound input. Please use yes or no"
        print(reminder)
        return

    # Print the customized reminder with exact format
    print(f"Reminder: '{task}' is a {priority} priority task{reminder.split('task')[1]}")

if __name__ == "__main__":
    daily_reminder()
```