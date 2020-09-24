import random

def dice_roller():
    print(random.randint(1,6))
    return 0
dice_roller()
while True:
    Choice = input("you would like to roll again? Y or N").strip()
    if Choice == 'Y':
        dice_roller()
    else: break

    
