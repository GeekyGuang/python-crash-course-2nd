class User:
  """model a user"""
  def __init__(self, first_name, last_name, age):
    self.full_name = f"{first_name} {last_name}"
    self.age = age
  
  def describe_user(self):
    print(f"name: {self.full_name} age: {self.age}")

  def greet_user(self, message):
    print(f"{message}, {self.full_name}")

user = User('rose', 'clark', 20)
user.describe_user()
user.greet_user('Hello')