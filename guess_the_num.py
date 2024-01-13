import random
num=random.randint(1,100)
i=int(input("How many guesses you want->"))

j=1
while(j<=i):

    print("You have ",i," guesses left")
    guess=int(input("Guess the number->"))
    if(i==j):
     print("You Loose the game>Game over")
     break
    
    if(guess<num):
        print("Your guess is small,Try again")
    elif(guess>num):
        print("your guess is lagrer,Try again")
    elif(guess==num):
        print("Congrulation your guess is right")
        break
    else:
        print("cant take input rather then numbers,try again")
    i=i-1



