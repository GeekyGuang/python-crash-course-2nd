
while True:
    name = input("please tell me your name, press 'q' to quit: ")
    if name == 'q':
        break
    with open('guest_book.txt', 'a') as file_object:
        file_object.write(name+'\n')
    print(f"welcome {name}")
