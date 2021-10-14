import gameboard

import aircraft_carrier
import battleship
import submarine
import destroyer

class Player():

    def __init__(self, name) -> None:
        self.name = name
        self.acc = aircraft_carrier.AircraftCarrier('Aircraft Carrier')
        self.battle = battleship.Battleship('Battleship')
        self.sub = submarine.Submarine('Submarine')
        self.dest = destroyer.Destroyer('Destroyer')
        self.guess_board = gameboard.Gameboard()
        self.player_board = gameboard.Gameboard()

    def create_opponent_board(self):
        pass

    def create_player_board(self):
        pass

    def assign_ship_location(self):
        pass