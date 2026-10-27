print("===ATM CASH DISPENSER===")
total100= total50 = total20 = total10 = total5 = total1 = 0
customers = 0
total = 0

while True:
    name = input("Enter your name: ")
    amount = int(input(f"Hello {name}! Enter your amount: "))
    if amount <= 0:
        print("Invalid amount, try again")
        continue

    id = 1
    while id<=6:
        if id==1: value = 100
        elif id==2: value = 50
        elif id==3: value = 20
        elif id==4: value = 10
        elif id==5: value = 5
        else: value = 1
        count = amount//value
        amount = amount % value
        if count > 0:
            print(f"{count} X {value} - Unit note")
            if value == 100: total100 += count
            elif value == 50: total50 += count
            elif value == 20: total20 += count
            elif value == 20: total20 += count
            elif value == 10: total10 += count
            else: total1 += count

        id = id+ 1

    again = input("Another customer? (Yes/no)")
    if again != "yes":
        break 