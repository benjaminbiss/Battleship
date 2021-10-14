import player
class Gamespace():

    def __init__(self) -> None:
        pass

    def run_game(self):
        self.add_players()

    def add_players(self):
        self.player1 = player.Player(input('Player 1, enter your name: '))
        self.player2 = player.Player(input('Player 2, enter your name: '))