answer = 5

print("Please guess number between 1 and 10: ")
guess = int (input())

if guess != answer:
   if guess < answer:
        print("Please guess higher")
   else:
        print("Please guess lower")
   guess = int(input())
   if guess == answer:
        print ("Well done, you guessed it")
   else:
        print ("Wrong Guesses, Sorry")
else:
   print("You got in first time")


##########################################################################################

answer = 5

print("Please guess number between 1 and 10: ")
guess = int (input())

if guess == answer:
    print("You got in first time")
else:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")

    guess = int(input())
    if guess == answer:
        print ("Well done, you guessed it")
    else:
        print ("Wrong Guesses, Sorry")

print("Hello, What is your name?")

name = input("")

print("Nice to meet you " +name)

print("How old are you?")

age = int(input(""))

if 18 <= age < 31:
    print ("Welcome to Hotel California")
else:
    print ("Sorry....Have a nice day")

##########################################################################################

import random

highest = 10
answer  = random.randint(1, highest)
print(answer)   #TODO: Remove after testing

print ("Please guess number between 1 and {}: ".format(highest))
guess = int(input())

if guess == answer:
    print("You got it the first time")
else:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess == int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have NOT guessed correctly")


##########################################################################################

import random

number = random.randint(1, 1000)
guesses = 0

print("I'm thinking of a number between 1 and 1000.")

while True:
    guess = int(input("\nWhat do you think it is? "))
    guesses += 1

    if guess > number:
        print("{0} is too high.".format(guess))
    elif guess < number:
        print("{0} is too low.".format(guess))
    else:
        break

print("\n Congratulations, you got it in {0} guesses!\n".format(guesses))






