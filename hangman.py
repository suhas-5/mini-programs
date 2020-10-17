import random
L = ["Googly","Tennis","Runner","Labour","Sister","Attack","school","Readymade",
     "Kidnapped","Power","Jackpot"]
print(L)
count = 3
R = random.choice(L)
print("The length of the word is {}".format(len(R)))    
def single_letter():
    A = input("Enter a letter:").strip()
    while len(A)!=1:
        print("invalid! Plz enter again")
        A = input("Enter a letter:").strip()
    return A
def if_correct():
    S = input("enter the word :").strip()
    if S==R:
        return print("The guessed word is correct. It is",S)
    else :
        return print(" The guessed word is wrong. The word was ",R)
while True:
    A = single_letter()
    if A in R:
        print('''The letter entered is present {} times in the word
           and at {}th position '''.format(R.count(A),R.index(A)))
        D = input("Are you able to guess the word ? Y or N").strip()
        if D=='Y':
            if_correct()
            break
    else :
        count = count - 1
        if count!=0:
            print('''The letter entered is not present in the guessing word.
             The number of chances remaining is {}'''.format(count))
        else:
            print(''' The letter entered is wrong and the number
            of remaining chances is zero. The word was {}'''.format(R))
            break
        
            

    
    
    







    



