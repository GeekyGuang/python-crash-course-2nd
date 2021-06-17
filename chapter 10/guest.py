name = input("Please tell me your name: ")

with open('guest.txt', 'w') as file_object:
    file_object.write(name)
