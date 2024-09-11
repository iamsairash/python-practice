import random

while True:
    ans = input("Roll the dice (y/n?): ").lower
    if ans == 'y':
        d1= random.randint(1,6)
        d2= random.randint(1,6)
        print(f"({d1},{d2})")       #writing this some similar as $"{var}" in c#
    elif ans == 'n':
        print("Game terminated.")
        break
    else:
        print("Invalid input. Press 'y' to roll the dice and 'n' to end.")
