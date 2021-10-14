import random

print("*****Rock Paper Scissors*****\nInitial score given is 5 to both player and computer\nEnter 'Q' anytime to exit\n")

def start():
    player_score = 5
    computer_score = 5
    i = 0

    while i <= 10:
        car = ["r", "p", "s"]

        comp = random.choice(car)
        # print(comp)

        person = input(f"R :: ROCK\nP :: PAPER\nS :: SCISSORS\n\n->").lower()
        if person == "q":
            print("\nThanks for playing")
            exit()
        if (person == "r" and comp =="s"):
            print(f"Computer had SCISSORS\nYou Won the round\n")
            player_score += 1
            computer_score -= 1
        elif (person == "r" and comp == "p"):
            print(f"Computer had PAPER\nYou Lost the round\n")
            player_score -= 1
            computer_score += 1
        elif (person == "p" and comp == "r"):
            print(f"Computer had ROCK\nYou Won the round\n")
            player_score += 1
            computer_score -= 1
        elif (person == "p" and comp == "s"):
            print(f"Computer had SCISSORS\nYou Lost the round\n")
            player_score -= 1
            computer_score += 1
        elif (person == "s" and comp == "p"):
            print(f"Computer had PAPER\nYou Won the round\n")
            player_score += 1
            computer_score -= 1
        elif (person == "s" and comp == "r"):
            print(f"Computer had SCISSORS\nYou Lost the round\n")
            player_score -= 1
            computer_score += 1
        elif ((person == "r" and comp == "r") or (person == "p" and comp == "p") or (person == "s" and comp == "s")):
            print("Its a Tie\n")
            i -= 1
        else:
            print("Invalid input!!!\n")

        i += 1
            
    if player_score <= computer_score:
        print(f"You lost the game!!\nYour score :: {player_score}\nComputer score :: {computer_score}\n")
    elif computer_score <= player_score:
        print(f"You Won the game!!\nYour score :: {player_score}\nComputer score :: {computer_score}\n")
    elif computer_score == player_score:
        print(f"Game is draw!!\nYour score :: {player_score}\nComputer score :: {computer_score}\n")
    again = input("Do you want to play again?\nY :: Yes\nN :: No\n").lower()
    if (again == "y"):
        start()
    else:
        print("\nThanks For playing")
        exit()

start()
