# Class = Blueprint
# We create instances (objects) from class blueprint

# Mobile Phones class
class MobilePhones:
    # Methods
    def __init__(self, display, camera, chipset, battery):
        # Attributes
        self.display_size = display
        self.camera_pixels = camera
        self.chipset_model = chipset
        self.battery_capacity = battery

    def calling(self):
        print('calling') 

    def taking_photos(self):
        print("taking photos")   

samsung_galaxy_m17 = MobilePhones(6.7, 50, 'Exynos 1330', 5000)

print(samsung_galaxy_m17.display_size)
print(samsung_galaxy_m17.camera_pixels)
print(samsung_galaxy_m17.chipset_model)
print("This model " + samsung_galaxy_m17.chipset_model + " has " + str(samsung_galaxy_m17.battery_capacity) + " battery capacity.")

samsung_galaxy_m17.calling()
samsung_galaxy_m17.taking_photos()

apple_iPhone_17 = MobilePhones(6.3, 48, "Apple A19", 3692)

print(apple_iPhone_17.display_size)
print(apple_iPhone_17.camera_pixels)
print(apple_iPhone_17.chipset_model)
print(apple_iPhone_17.battery_capacity)

apple_iPhone_17.calling()
apple_iPhone_17.taking_photos()
