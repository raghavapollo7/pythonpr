import random
print("Welcome to number guessing game")
i=0
while i<=10:
    num=random.randint(1,50)
    n2=int(input("Enter your guess:"))
    if n2 ==num:
        print("You guessed correctly")
        break
    else:
        print("Your guess was incorrect")
        i=i+1
print(f"The number was {num}")
print("GAME OVER")
