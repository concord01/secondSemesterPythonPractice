import random
random_num = random.randint(0,100)
guess_num = 0
while True:
    guess = int(input("Guess a number \n"))
    if guess < random_num:
        print("The number you want is higher.")
    elif guess > random_num:
        print("The number you want is lower")
    else:
        print("Congrats! You guessed it!")
        print("You guessed " + str(guess_num) +" times until you hit the right number on try " + str(guess_num + 1))
        break
    guess_num += 1