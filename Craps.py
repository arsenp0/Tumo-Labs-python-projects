import random

def roll():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1, 6)
    summ = dice1 + dice2
    print(f"The sum of dice: {dice1} + {dice2} = {summ}.\n")
    return summ

s = roll()

if s == 7 or s == 11:
    print("You won!")
elif s == 2 or s == 3 or s == 12:
    print("Casino wins!")
else:
    goal = s
    print(f"Now your goal is {goal}.\n")
    while True:
        s = roll()
        if s == goal:
            print("You win!")
            break
        elif s == 7:
            print("Casino wins!")
            break


