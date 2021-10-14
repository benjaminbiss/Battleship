import player
class Gamespace():

    def __init__(self) -> None:
        self.player1 = player.Player(input('Player 1, enter your name: '))
        self.player2 = player.Player(input('Player 2, enter your name: '))

    def run_game(self):
        self.welcome()
        self.ship_location_select(self.player1)
        self.ship_placement(self.player1)
        

    def welcome(self):
        print('Welcome to the game battleship! Below is the board you will be playing on:')
        self.player1.display_board()

    def ship_location_select(self, player):
        player.assign_ship_location(player.acc)
        player.assign_ship_location(player.battle)
        player.assign_ship_location(player.sub)
        player.assign_ship_location(player.dest)

    def ship_placement(self, player):
        player.gameboard.place_ships(player.acc, player.player_board)
        player.gameboard.place_ships(player.battle, player.player_board)
        player.gameboard.place_ships(player.sub, player.player_board)
        player.gameboard.place_ships(player.dest, player.player_board)