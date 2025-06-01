# Prompt user for task details
task = input("Enter your task: ")
priority = input("Enter the task’s priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Initialize the reminder message
reminder = ""

# Match Case to respond based on priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a HIGH priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a MEDIUM priority task."
    case "low":
        reminder = f"Reminder: '{task}' is a LOW priority task."
    case _:
        reminder = f"Reminder: '{task}' has an UNKNOWN priority."

# Conditional addition if time-bound
if time_bound == "yes":
    reminder += " It requires immediate attention today!"

# Use a loop to display the reminder 3 times (as an example of loop use)
for i in range(3):
    print(reminder)

