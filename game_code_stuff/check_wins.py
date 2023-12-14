def player1_health_check(player1_health):
    if player1_health == 0:
        return True
    return False

def player2_health_check(player2_health):
    if player2_health == 0:
        return True
    return False


def check_win(player1_health, player2_health):
    if player1_health_check(player1_health):
        print("Player 1 health is 0")
        print("Player 2 wins")
        return True
    elif player1_health_check(player2_health):
        print("Player 2 health is 0")
        print("Player 1 wins")
        return True
    else:
        return False