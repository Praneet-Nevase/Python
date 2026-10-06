temp=int(input("Enter temperature"))

if temp>20 :
    outfit="t-shirt"
    print("it is hot today")
    print("Wear a", outfit)
else :
    outfit="jacket/sweater"
    print("It is cold today")
    print("Wear a", outfit)

raining=input("Enter if it is raining(yes/no all lowercase)")

if raining=="yes" :
    needumbrella="yes"
    print("It is raining today")
    print("Take umbrella")
else :
    needumbrella="no"
    print("It is not raining")
    print("No need of umbrella")

windspeed = int(input("Enter wind speed"))

if windspeed>30 :
    needwindbreaker="yes"
    print("It is windy")
    print("You need a wind breaker")
else :
    needwindbreaker="no"
    print("It is not windy")
    print("You do not need a wind breaker")

puddles=input("Enter if puddles are outside(yes/no)")

if puddles=="yes" :
    needboots="yes"
    print("There are puddles outside")
    print("You need boots")
else :
    needboots="no"
    print("There are not puddles outside")
    print("You can wear sneakers")

print("Summary")
print("Temperature:", temp)
print("Outfit:",outfit)
print("Is raining:", needumbrella)
print("Boots:",needboots)
print("Sneakers",needboots)
print("Needed windbreaker:",needwindbreaker)