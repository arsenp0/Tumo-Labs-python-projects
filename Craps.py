import random

def roll():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1, 6)
    summ = dice1 + dice2
    print(f"The sum of dice: {dice1} + {dice2} = {summ}.\n")
    return summ

s = roll()

#You could write this in a more Pythonic way for readability
#Its shorter and easier to read
if s in (7, 11):
    print("You won!")
#Same here
elif s in (2, 3, 12):
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


