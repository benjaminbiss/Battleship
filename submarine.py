import ship

class Submarine(ship.Ship):
    
    def __init__(self, name):
        self.size = 3
        self.code = 'S'
        super().__init__(name)
