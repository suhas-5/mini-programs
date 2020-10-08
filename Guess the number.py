import random
A = random.randint(0,100)
while True :
        U = int(input("enter a number"))
        if U<A:
            print("the guessed number is low")
        elif U>A :
            print("the guessed number is high")
        else :
            print("the guessed number is correct",U)
            break
        
        

    
