class Car:
    def __init__(self, make, model, year):
        self.__maker = make #private attribute
        self.model_name = model
        self.year_of_manufacutre = year
        self.odometer_reading = 20

    
    def get_descriptive_name(self):
        return f"{self.__maker} {self.model_name} {self.year_of_manufacutre}"
    
    def get_descesriptive_name_upper(self):
        
        return f"{self.__maker.upper()} {self.model_name.upper()} {self.year_of_manufacutre}"

    
    # Getter
    def get_maker(self):
        return self.__maker
    
    # Setter
    def set_maker(self, updatedMaker):
        self.__maker = updatedMaker

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
# print(audi.__maker)
# print(audi.get_descriptive_name())

# Modifying an Attribute’s Value Directly
# audi.odometer_reading = 20
# print(audi.odometer_reading)

# Modifying an Attribute’s Value Through a Method
# audi.update_odometer(40)
# print(audi.odometer_reading)

# print(audi.__maker)
print(audi.get_maker())

audi.set_maker('Ferrari')
print(audi.get_maker())






# Composition
# Create a Engine class and use its instance as attribute in the ElectricCar class attribute.

# Inheritance
# Create a ElectricSportCar class from ElectricCar class.
# Add its own attributes and methods.
# Create instances from it.

# Modules