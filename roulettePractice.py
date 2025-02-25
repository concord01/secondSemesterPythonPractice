import random
import time

# function to generate a wheel
def generate_wheel():
    spaces = []
    for i in range(18):
        spaces.append("red")
        spaces.append("black")
    for i in range(2):
        spaces.append("green")
    return spaces

# function to return a random space landed on
def spin_wheel(spaces):
    return random.choice(spaces)
# roulette game
def play_game():
    money = 1000
    spaces = generate_wheel()
    while True:
        print("You have $" + str(money) + " available.")
        bet = input("How much do you want to bet? (Or enter 'stop' if you want to exit)\n")
        if (bet.lower() == "stop"):
            break
        else:
            bet = int(bet)
            while bet > money:
                print("You don't have that much money to bet!")
                bet = input("How much do you want to bet?\n")
                bet = int(bet)
            color = input("What color do you want to bet on?\n")

            print("The wheel is spinning...")
            time.sleep(2)
            landed = spin_wheel(spaces)
            print("The wheel landed on "+landed+".")
            if (landed == color):
                print("Congratulations! You win $" + str(bet) + " dollars!")
                money = money + bet
            else:
                print("You lost $" + str(bet) + " dollars, better luck next time!")
                money = money - bet


play_game()