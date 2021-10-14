import ship

class Battleship(ship.Ship):
    
    def __init__(self, name):
        self.size = 4
        super().__init__(name)
