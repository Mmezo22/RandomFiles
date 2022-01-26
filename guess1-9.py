import random

answer = random.randint(1,10)
guess_count = 0

while True:
    user = input("Input a number from 1 to 10: ")
    if user == "exit":
        break
    elif int(user) == answer:
        guess_count += 1
        print("Congrats! You've found us out!")
        print("\nNumber of guesses: {0}".format(guess_count))
        break
    elif int(user) > answer:
        print("Sorry, too high; try again\n")
        guess_count += 1
    elif int(user) < answer:
        print("Sorry, too low; try again\n")
        guess_count += 1



