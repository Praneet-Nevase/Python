print("==========Smart School Day Planner==========")
print("Answer 3 quick questions and I will plan your day\n")
day=     input("Enter the day (Monday-Sunday)").strip().capitalize()
weather= input("Enter weather condition outside(Sunny/Rainy/Cloudy)").strip().capitalize()
homework=input("If your homework done(yes/no)").strip().capitalize()

print("")
print("=== Your plan for today ===")
print("-" * 35)

if day in ("Saturday", "Sunday") :
    print("Weekend! Enjoy your free time!")
elif day == "Monday" :
    print("First school day of the week. Pack your weekly planner")
elif day in ("Tuesday", "Wednesday", "Thursday") :
    print("Regular school day.")
elif day == "Friday" :
    print("Last school day of the week, Return library books.")
else :
    print("Day not recognized, Try again")

if weather=="sunny" and homework=="yes" :
    print("After school: Head to the park - Great weather and homework is done.")
if weather=="rainy" or weather=="cloudy" :
    print("Weather tip - Carry an umbrella")
if not(homework=="yes"):
    print("Homework not done - Finish it before going out")