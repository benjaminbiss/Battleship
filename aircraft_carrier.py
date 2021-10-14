import ship

class AircraftCarrier(ship.Ship):
    
    def __init__(self, name):
        self.size = 5
        super().__init__(name)
