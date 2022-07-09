import random
options=['magnificent','secret','happy','world','hilarious','computer','python','programming','hangman','botanical','coronavirus','pandemic','epidemic']
print("---Welcome To Hangman---")
print()
name=input("Enter your name to start the game!-  ")
print()
print("Hello {}! Welcome to the game".format(name))
ch='Y'
while(ch=='Y'):
    search=random.choice(options)
    print("The word to be searched- ")
    print("*"*len(search))
    print("You have to search a {} lettered word.".format(len(search)))
    print("Rules for the Game - ")
    turns=len(search)+2
    print("You have {} turns in total to guess the word with all lowercase letters".format(turns))
    print()
    print("Goodluck!")
    print()
    count=0
    guess=''
    while turns>0:
        failed=0
        ch=input("Enter your character")
        guess=guess+ch
        for c in search:
            if c in guess:
                print(c,end='')
            else:
                print('*',end='')
                failed+=1
                
        print()
        if failed==0:
            print("Hurray! You Won")
            break
        turns-=1
    if turns==0:
        print("The word was- "+search)
        print("Better Luck next time!")

    ch=input("Do You Want To Play Again[Press Y to Continue]? ")
