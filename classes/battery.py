# Composition = breaking code into smaller pieces.
class Battery:
    def __init__(self):
        self.battery_size = 0
        self.energy_density = 0
        self.voltage = 0
        self.power_output = 0
        self.charging_speed = 0
        self.self_discharge_rate = 0

    def lifespan_Cycle_life(self):
        return "Lifespan/Cycle life"

    def thermal_and_chemical_stability(self):
        return "Thermal and chemical stability"
    
# b1 = Battery()