total = 4
og = 4
print(f"You have {total} chores to complete")

completed = 0
chore_num = 1

while chore_num<=total :
    if chore_num == 1 :
        next_task = "Make your bed"
    elif chore_num == 2:
        next_task = "Feed your pet"
    elif chore_num == 3 :
        next_task = "Take out the trash"
    else :
        next_task = "Wash the dishes"

    answer = input(f"Have you completed:{next_task}").lower()

    if answer == "yes":
        completed = completed + 1
        chore_num = chore_num + 1
        print("Nice")
    else :
        print("Please complete your chore")

    print("Chores remaining:",total-completed,)

print("YAY! You have completed all your chores! Ask your dad to bring a chocolate for you as your reward")

test = 0
count = 0
while test<=0 :
    count += 1
    print(test)