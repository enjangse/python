import random

print('Hello, what is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 10. Take a guess')

#get random secretNumber
secretNumber =  random.randint(1,10)

for guessesTaken in range(1,7):
    print('Take a guess')
    guess =  int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break #if the guess number is correct, break the program

if guess == secretNumber:
    print('Good job, ' + name + '! your guesss my number')
else:
    print ('Nope, the number i was thinking ' + guess )
