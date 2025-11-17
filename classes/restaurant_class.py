# Make a class called Restaurant
# Attributes = restaurant_name, cuisine_type
# Methods = describe_restaurant(), open_restaurant()
# Create a restaurant instance.
# Print the two attributes individually, and then call both methods.

class Restaurant:
    def __init__(self, rname, ctype):
        self.restaurant_name = rname
        self.cuisine_type = ctype

    def describe_restaurant(self):
        print("The restaurant name is " + self.restaurant_name)
        print("The cuisine type is " + self.cuisine_type)

    def open_restaurant(self):
        print('The restautant is open')
        return False

# creating restaurant instance
restaurant1 = Restaurant('Gordon ramsey','Eurocentric')

# dot notation
print(restaurant1.restaurant_name)
print(restaurant1.cuisine_type)

restaurant1.describe_restaurant()
restaurant1.open_restaurant()

if restaurant1.open_restaurant():
    print('yes')
else:
    print('no')

italian_restaurant = Restaurant('Fast food', 'Italian')

italian_restaurant.restaurant_name
italian_restaurant.cuisine_type

italian_restaurant.describe_restaurant()
italian_restaurant.open_restaurant()
