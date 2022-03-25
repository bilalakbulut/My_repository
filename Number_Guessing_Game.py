from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

def check_the_guess(g,n):
    if g != n:
        global attemp
        attemp -= 1
        if n < g:
            print("Too high.")
        else:
            print("Too low.")
    else:
        print(f"You got it! The answer was {number}.")
        attemp = 0

import random
number = random.randint(0,100)


easy_or_hard = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
if easy_or_hard == "easy":
    attemp = 10
elif easy_or_hard == "hard":
    attemp = 5

should_continue = True
while attemp != 0:
    print(f"You have {attemp} attempts remaining to guess the number.")
    guess = int(input("Make a guess:"))
    check_the_guess(guess,number)
    


















