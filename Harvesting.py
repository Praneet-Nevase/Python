field1=100
field2=80
field3=120
field4=145
field5=155

total=field1+field2+field3+field4+field5
average=total/5

print(f"Total harvest: {total}kg")
print(f"Average harvest per field: {average}kg")

price_per_kg=15
total_earning=15 * total
print(f"Total earning: {total_earning}rs")

bag= total//25
leftover=total%25
print(f"Bags packed: {bag}")
print(f"Leftover kgs: {leftover}kg")

lastyear=500
print(f"Better than last year?: {total>lastyear}")
print(f"Same as last year?: {total==lastyear}")
print(f"At least as good?: {total>=lastyear}")

total += 50
print(f"After bonus crop: {total}kg")

total -= 10
print(f"Seed reserve after 1 year: {total}kg")

bag = total//25
leftover=total%25
print(f"Bags packed now: {bag}")
print(f"Leftover kgs: {leftover}kg")