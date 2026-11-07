print("=== Number Guessing Game")
print("I have a secret number from 1 to 50 and you have to guess it in 5 trys!")

secretnumber = 32
guess = 0
guesscount = 0
lives = 5
print("I have chosen number.")
while guesscount < lives and guess != secretnumber:
    guess = int(input("Enter your guess: "))
    guesscount = guesscount + 1

    if guess == secretnumber:
        print("Correct! You win!!")
    else:
        print("Wrong! Try again")
    
        if guess > secretnumber:
            diff = guess - secretnumber
        else:
            diff = secretnumber - guess

        if diff >= 20:
            print("🧊 Ice cold! You are very far away.")
        elif diff >= 10:
            print("🥶 Cold. You are still quite a distance away.")
        elif diff >= 5:
            print("🌡️   Warm! You are getting closer.")
        else:
            print("🔥 Hot! Really close!")

        remaininglives = lives - guesscount
        if remaininglives > 0:
            print("Lives left: ", end="")
            for i in range(remaininglives):
                print("❤️ ", end="")
            print()
            print()

if guess != secretnumber:
    print("======================================")
    print("💀 Game over! You used all 5 attempts.")
    print("   The secret number was:", secretnumber)
    print("======================================")