person_name = input("Enter your name: ")
goal_name = input("Enter one skill you want to get better at: ")
target_month = input("Enter the month you want to reach it by: ")

daily_minutes = 30

print("\nMY PERSONAL GOAL PLAN\n")

print("Name:", person_name)
print("Goal:", goal_name)
print("Target month:", target_month)
print("Daily practice:", daily_minutes, "minutes")

print("Status:", end=" ")
print("Not started")
print("Reminder:", end=" - ")
print("Practise every day!")

print("In one sentence:")
print(person_name + " wants to get better at " + goal_name + " by practicing " + str(daily_minutes) + " minutes daily until " + target_month + ".")