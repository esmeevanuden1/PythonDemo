### Implementatie van opdracht 9: https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

import random 

print("Guessing Game One: guess a number between 1 and 9\nIf you are done with the game, type: exit\nPlease input a number:")
random_number = random.randint(1, 9)

i = 0

guess = int(input("Firt guess: "))

while guess != random_number:

    if guess == "exit":
        break 

    guess = int(guess)

    if (guess > 9) or (guess < 1):
        guess = input(f"We are guessing between 1 and 9. Try again: ")
        continue

    if guess > random_number:
        guess = input(f"Too high, try agian: ")
    elif guess < random_number:
        guess = input(f"Too low, try again: ")

    i += 1


if guess == "exit":
    print("The game is finished upon request.")

else:
    if i == 0:
        print(f"Well Done!! It only took you 1 try.")
    else:
        print(f"Well Done!! It only took you {i} tries.")


##############################################################################################################

# ### Opdracht 4: https://www.practicepython.org/exercise/2014/02/26/04-divisors.html\

# print("We are going to check whether the given number is prime.\nRecall that prime number is only divisible by itself and one (1)")
# number = int(input("Input number: "))

# if number <= 1:
#     number = int(input("Please provide a digit greater than 1: "))

# element = 1
# for element in range(2, number):
#     if (number % element) == 0:
#         print(f"This number is not a prime, since it can be divided by (at least): {element}")
#         break

# if (element + 1) == number:
#     print(f"This number is a prime!")