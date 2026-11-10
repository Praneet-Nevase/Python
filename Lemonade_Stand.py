def greet():
    print("Welcome to the Lemonade Stand!")
    print("Get fresh lemonade here!")

greet()

ppc = int(input("Enter price per cup: "))
noc = int(input("Enter number of cups: "))

def calculate_total(p,c):
    total = p * c
    return total

total_cost = calculate_total(ppc,noc)

print("Your total cost is:", total_cost)

Amount_paid = float(input("Enter amount paid: "))
def calculate_change(paid, total):
    change = paid - total
    return change

changegive = calculate_change(Amount_paid, total_cost)

print("Change due is: ", changegive)

def thankyou(cups):
    if cups>=5:
        return "Thanks for your support! Please visit again!"
    else:
        return "Thanks for standing by! Visit again!"

closingmessage = thankyou(noc)

print(closingmessage)