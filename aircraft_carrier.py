import ship

class AircraftCarrier(ship.Ship):
    
    def __init__(self, name):
        self.size = 5
        self.code = 'A'
        super().__init__(name)
