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
        self.gameboard = gameboard.Gameboard()
        self.guess_board = self.gameboard.create_board()
        self.player_board = self.gameboard.create_board()

    def assign_ship_location(self, ship):
        orientation = input(f"{self.name} is placing their {ship.name}.\nWould you like to place your ship vertically or horizontally?\nEnter 'v' or 'h':  ")
        if orientation == 'v':
            ship.x_axis_start = int(input('Which column do you want to place your ship?'))
            ship.x_axis_end = ship.x_axis_start
            ship.y_axis_start = int(input('Which row do you want to place the top of your ship?'))
            ship.y_axis_end = ship.y_axis_start + ship.size
        else:
            ship.y_axis_start = int(input('Which row do you want to place your ship?'))
            ship.y_axis_end = ship.y_axis_start
            ship.x_axis_start = int(input('Which column do you want to place the left end of your ship?'))
            ship.x_axis_end = ship.x_axis_start + ship.size

    def update_guess_board(self):
        pass

    def display_board(self):
        for rows in self.guess_board:
            print(rows)