print("=== Swimming pool entry checker ===")
print("Answer three questions and I will tell you which pool you can use\n")

age = int(input("How old are you? "))
can_swim = input("Can you swim 25 metres? (yes / no): ").lower()
adult_here = input("Is an adult with you? (yes / no): ").lower()

print()
print("=== Entry Decision ===")
print("-" * 32)

if can_swim != "yes" and can_swim != "no":
    print("Error: Please answer 'yes' or 'no' for swimming ability.")
    swim_known = False
else:
    swim_known = True

if adult_here != "yes" and adult_here != "no":
    print("Error: Please answer 'yes' or 'no' for adult presence.")
    adult_known = False
else:
    adult_known = True

if swim_known and adult_known:
    if age < 4:
        if adult_here == "yes":
            print("Age Group: Toddler")
            print("Decision: Allowed in the splash pool only (with your adult).")
        else:
            print("Entry Denied: Toddlers must be accompanied by an adult.")
            
    elif age < 12:
        if adult_here == "yes":
            print("Age Group: Child")
            print("Decision: Allowed in the main pool (with your adult).")
        else:
            print("Entry Denied: Children under 12 must be accompanied by an adult.")
            
    elif age < 18:
        if can_swim == "yes":
            print("Age Group: Teen")
            print("Decision: Allowed in the main pool alone.")
        else:
            if adult_here == "yes":
                print("Age Group: Teen")
                print("Decision: Allowed in the pool since an adult is supervising.")
            else:
                print("Entry Denied: Teens who cannot swim 25m must have an adult present.")
                
    else:
        print("Age Group: Adult")
        print("Decision: All pools are open to you!")
else:
    print("Decision: Cannot determine entry due to invalid inputs.")

print("")
print("Have a safe swim")