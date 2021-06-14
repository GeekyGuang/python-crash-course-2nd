class Restaurant:
  def __init__(self, restaurant_name, cuisine_type):
    """class for restaurant"""
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
    self.number_served = 0

  def describe_restaurant(self):
    print(f"name: {self.restaurant_name}, cuisine: {self.cuisine_type}")
  
  def open_restaurant(self):
    print("The restaurant is open.")
  
  def set_number_served(self, number):
    self.number_served = number

  def increment_number_served(self, number):
    self.number_served += number

restaurant = Restaurant('全聚德', '京')
restaurant.number_served = 100
print(restaurant.number_served)
restaurant.set_number_served(200)
print(restaurant.number_served)
restaurant.increment_number_served(500)
print(restaurant.number_served)

