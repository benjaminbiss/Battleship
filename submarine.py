import ship

class Submarine(ship.Ship):
    
    def __init__(self, name):
        self.size = 3
        super().__init__(name)
