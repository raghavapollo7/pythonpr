import random
print("Welcome to the game of rolling a dice")
while True:
    choice=input("Press Enter to continue or 'q' to quit: ")
    if choice=="q":
        print("Goodbye")
        break
    elif choice=="":
        num=random.randint(1,6)
        print(f"The number rolled is {num}")
    else:
        print("Invalid input")