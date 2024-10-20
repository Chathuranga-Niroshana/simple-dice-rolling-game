import random

while True:
    choice = input("Roll the dice? (y/n): ").lower()

    if choice == "y":
        n = int(input("How many time you need to roll the dice? "))

        if n > 0:
            for i in range(0, n):
                a = random.randint(1, 6)
                b = random.randint(1, 6)
                print(f" {i+1}. ({a}, {b})")
    elif choice == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")
