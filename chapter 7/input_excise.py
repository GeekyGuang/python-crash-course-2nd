car = input("what kind of rental car would you like? ")
print(f"Let me see if I can find you a {car}")

people_number = int(input("How many people are there in your dinner group? "))
if people_number > 8:
    print("Sorry, You'll have to wait for a table")
else:
    print("Your table is ready.")

number = int(input("please enter a number: "))
if number % 10 == 0:
    print(f"the number {number} is a multiple of 10")
else:
    print(f"the number {number} is not a multiple of 10")
