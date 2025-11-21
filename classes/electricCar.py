# import car, battery

# from car import Car
# from battery import Battery

# from car import Car1, Car2

# alias
from car import Car as myCar
from battery import Battery as myBattery



# Inheritance
# Child Class
class ElectricCar(myCar):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.batery_details = myBattery()
        # self.engine_details = Engine()

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