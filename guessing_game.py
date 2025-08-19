import random
print("Welcome to Guessing Game!\n")
print("Guess between numbers 1-100!\n")
while True:
    state = random.getstate()         #gpt aid I also could not have used get/setState, but it's my very first code, so I don't care lmao
    random_number = random.randrange(1, 101)    #you can change the numbers here
    guess = int(input("Your guess is : "))
#print("Random Number is:", random_number) << This line was used to test if the code was working fine or not
    if guess == random_number:
        print("You guessed right!\n")
    else:
        print("Try again!\n")
        random.setstate(state)
    continuation = input("Press enter to play again or press 'q' to quit.\n")
    if continuation.lower() == "q":
            break
    else:
        continue
