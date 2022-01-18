def check_input():
    valid = ["R","P","S"]
    player_input = []
    player1 = input("Player 1: ")
    while player1 not in valid:
        player1 = input("Player 1, please input R, P, or S: ")
    player_input.append(player1)
    player2 = input("Player 2: ")
    while player2 not in valid:
        player2 = input("Player 2, please input R, P, or S: ")
    player_input.append(player2)
    return player_input


def update_score(num, score):
    if num == 1:
        score[0] += 1
    elif num == 2:
        score[1] += 1


def play():
    print("Welcome to a new game of Rock Paper Scissors [Digital Edition]!!\n")
    score = [0, 0]
    while True:
        player_input = check_input()

        if player_input[0] == player_input[1]:
            print("Draw")
        elif player_input == ["R","S"]:
            update_score(1,score)
        elif player_input == ["S","P"]:
            update_score(1,score)
        elif player_input == ["P","R"]:
            update_score(1,score)
        elif player_input == ["S","R"]:
            update_score(2,score)
        elif player_input == ["P","S"]:
            update_score(2,score)
        elif player_input == ["R","P"]:
            update_score(2,score)

        if score[0] == 3:
            print("Game over!!!\nPlayer 1 wins the wager {0}-{1}!!!".format(score[0],score[1]))
            restart = input("Press X to start again: ")
            if restart == "X":
                play()
            else:
                return
        elif score[1] == 3:
            print("Game over!!!\nPlayer 2 wins the wager {0}-{1}!!!".format(score[0],score[1]))
            restart = input("Press X to start again: ")
            if restart == "X":
                play()
            else:
                return


play()