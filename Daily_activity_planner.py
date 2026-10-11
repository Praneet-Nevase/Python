homework_time = int(input("Enter your homework time in minutes: "))

if homework_time > 60:
    plan = "start homework now"
    print("That is a long homework session.")
else:
    plan = "finish homework quickly"
    print("That is a short homework session.")

free_time = input("Is there free time after homework? (yes/no): ").lower()

if free_time == "yes":
    print("Don't forget to pick a hobby!")

print("===== DAILY PLAN =====")
print(f"Homework Minutes: {homework_time}")
print(f"Plan: {plan}")
print(f"Free Time: {free_time}")
