import random


def play():
    user = input(
        "Escoge una opción: 'pi' para piedra, 'pa' para papel, 'ti' para tijeras. \n").lower()
    computer = random.choice(['pi', 'pa', 'ti'])

    if user == computer:
        return "¡Empate!"
    elif player_win(user, computer):
        return "¡Ganaste!"
    return "¡Perdiste!"


def player_win(player1, player2):
    if ((player1 == "pi" and player2 == "pa") or (player1 == "ti" and player2 == "pa") or (player1 == "pa" and player2 == "pi")):
        return True
    else:
        return False


print(play())
