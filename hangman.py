import random
L = ["Googly","Tennis","Runner","Labour","Sister","Attack","school","Readymade",          // list containing words
     "Kidnapped","Power","Jackpot"]
print(L)
count = 3
R = random.choice(L)                                                                     // Selects a random word from the list
print("The length of the word is {}".format(len(R)))    
def single_letter():
    A = input("Enter a letter:").strip()                                                // Function to check whether the user has entered single letter at a time or not
    while len(A)!=1:
        print("invalid! Plz enter again")
        A = input("Enter a letter:").strip()
    return A
def if_correct():                                                                     // Function to check whether the guessed word is correct or not
    S = input("enter the word :").strip()
    if S==R:
        return print("The guessed word is correct. It is",S)                               
    else :
        return print(" The guessed word is wrong. The word was ",R)
while True:
    A = single_letter()
    if A in R:
        print('''The letter entered is present {} times in the word                 // Checks whether the entered letter is present in the word or not , if present specifies 
           and at {}th position '''.format(R.count(A),R.index(A)))                     the number of times it is present and also gives the 1st position of the letter present
        D = input("Are you able to guess the word ? Y or N").strip()                   in the word
        if D=='Y':
            if_correct()
            break
    else :
        count = count - 1                                                            // reduces the number of chances available if the entered letter is not present 
        if count!=0:                                                                 
            print('''The letter entered is not present in the guessing word.
             The number of chances remaining is {}'''.format(count))
        else:
            print(''' The letter entered is wrong and the number                     // if the number of chances remaining  is 0, it prints the correct word 
            of remaining chances is zero. The word was {}'''.format(R))
            break
        
            

    
    
    







    



