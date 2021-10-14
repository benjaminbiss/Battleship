import ship

class Destroyer(ship.Ship):
    
    def __init__(self, name):
        self.size = 2
        self.code = 'd'
        super().__init__(name)
