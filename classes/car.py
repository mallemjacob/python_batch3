class Car:
    def __init__(self, make, model, year):
        self.maker = make
        self.model_name = model
        self.year_of_manufacutre = year
        self.odometer_reading = 20

    def get_descriptive_name(self):
        return f"{self.maker} {self.model_name} {self.year_of_manufacutre}"
    def read_odometer(self):
        print(self.odometer_reading)

    def update_odometer(self, milage):
        if milage > self.odometer_reading:
            self.odometer_reading = milage #40
        else:
            print('Milage must be greater than odometer reading.')

# Creating an instance
audi = Car('Audi','f1',2015)

# Accessing aatibutes and methods using dot notation
print(audi.maker)
print(audi.get_descriptive_name())

# Modifying an Attribute’s Value Directly
audi.odometer_reading = 20
print(audi.odometer_reading)

# Modifying an Attribute’s Value Through a Method
audi.update_odometer(40)
print(audi.odometer_reading)


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


# Inheritance
# Child Class
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.batery_details = Battery()

    def get_descriptive_name(self):
        print(f"{self.maker}, {self.model_name}, {self.year_of_manufacutre}")

ec1 = ElectricCar('Tesla', 'A1', 2025)
ec2 = ElectricCar('Tata','Nexon',2026)

print(ec1.maker)
print(ec1.get_descriptive_name())

ec1.batery_details.battery_size = 100
print(ec1.batery_details.battery_size)
print(ec1.batery_details.lifespan_Cycle_life())

print(ec2.batery_details.battery_size)