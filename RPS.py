import random
import inquirer

GAME_CHOICE = [
  inquirer.List('answer',
                message="Choose your choice ..",
                choices=['ROCK', 'PAPER', 'SCISSORS', '', 'QUIT'],
            ),
]

PLAY_AGAIN = [
  inquirer.List('answer',
                message="Do you want to play again?",
                choices=['YES', 'NO'],
            ),
]

GAME_CHOICE_VALUE = {
  "ROCK" : 'r',
  "PAPER" : "p",
  "SCISSORS" : "r",
  "QUIT" : "q"
}

print("*****Rock Paper Scissors*****\nInitial score given is 5 to both player and computer\n")

def current_score(round, player_score, computer_score):
    score_log = f"Round {round}\nPlayer Score: {player_score}\ncomputer_score: {computer_score}\n"
    return score_log

def start():
    player_score = 5
    computer_score = 5
    i = 1

    while i <= 11:
        car = ["r", "p", "s"]

        comp = random.choice(car)
        # print(comp)

        # person = input(f"R :: ROCK\nP :: PAPER\nS :: SCISSORS\n\n->").lower()
 
        answers = inquirer.prompt(GAME_CHOICE)
        person = GAME_CHOICE_VALUE.get(answers["answer"])

        if person == "q":
            print("\nThanks for playing")
            exit()
        if (person == "r" and comp =="s"):
            print(f"Computer had SCISSORS\nYou Won the round\n")
            player_score += 1
            computer_score -= 1
            print(current_score(i, player_score, computer_score))
        elif (person == "r" and comp == "p"):
            print(f"Computer had PAPER\nYou Lost the round\n")
            player_score -= 1
            computer_score += 1
            print(current_score(i, player_score, computer_score))
        elif (person == "p" and comp == "r"):
            print(f"Computer had ROCK\nYou Won the round\n")
            player_score += 1
            computer_score -= 1
            print(current_score(i, player_score, computer_score))
        elif (person == "p" and comp == "s"):
            print(f"Computer had SCISSORS\nYou Lost the round\n")
            player_score -= 1
            computer_score += 1
            print(current_score(i, player_score, computer_score))
        elif (person == "s" and comp == "p"):
            print(f"Computer had PAPER\nYou Won the round\n")
            player_score += 1
            computer_score -= 1
            print(current_score(i, player_score, computer_score))
        elif (person == "s" and comp == "r"):
            print(f"Computer had SCISSORS\nYou Lost the round\n")
            player_score -= 1
            computer_score += 1
            print(current_score(i, player_score, computer_score))
        elif ((person == "r" and comp == "r") or (person == "p" and comp == "p") or (person == "s" and comp == "s")):
            print("Its a Tie\n")
            i -= 1
            print(current_score(i, player_score, computer_score))
        else:
            print("Invalid input!!!\n")

        i += 1
            
    if player_score <= computer_score:
        print(f"You lost the game!!\nYour score :: {player_score}\nComputer score :: {computer_score}\n")
    elif computer_score <= player_score:
        print(f"You Won the game!!\nYour score :: {player_score}\nComputer score :: {computer_score}\n")
    elif computer_score == player_score:
        print(f"Game is draw!!\nYour score :: {player_score}\nComputer score :: {computer_score}\n")

    # again = input("Do you want to play again?\nY :: Yes\nN :: No\n").lower()
    again = inquirer.prompt(PLAY_AGAIN)

    if (again["answer"] == "YES"):
        start()
    else:
        print("\nThanks For playing")
        exit()

start()
