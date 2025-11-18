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