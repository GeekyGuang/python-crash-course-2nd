class Restaurant:
  def __init__(self, restaurant_name, cuisine_type):
    """class for restaurant"""
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type

  def describe_restaurant(self):
    print(f"name: {self.restaurant_name}, cuisine: {self.cuisine_type}")
  
  def open_restaurant(self):
    print("The restaurant is open.")

restaurant1 = Restaurant('全聚德', '京')
restaurant2 = Restaurant('渔人码头', '赣')
restaurant3 = Restaurant('火锅', '渝')


restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant2.describe_restaurant()
restaurant2.open_restaurant()
restaurant3.describe_restaurant()
restaurant3.open_restaurant()