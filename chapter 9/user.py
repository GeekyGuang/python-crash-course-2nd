class User:
  """model a user"""
  def __init__(self, first_name, last_name, age):
    self.full_name = f"{first_name} {last_name}"
    self.age = age
    self.login_attempts = 0
  
  def describe_user(self):
    print(f"name: {self.full_name} age: {self.age}")

  def greet_user(self, message):
    print(f"{message}, {self.full_name}")

  def increment_login_attempts(self):
    self.login_attempts += 1

  def reset_login_attempts(self):
    self.login_attempts = 0

user = User('rose', 'clark', 20)
user.describe_user()
user.greet_user('Hello')

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)