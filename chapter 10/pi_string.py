file_name = 'pi_million_digits.txt'

with open(file_name) as file_object:
    file_list = file_object.readlines()

pi_string = ''
for line in file_list:
    pi_string += line.strip()

birthday = input("Please enter your birthday in the form mmddyy:")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi")
    print(pi_string.index(birthday))
else:
    print("Your birthday doesn't appear in the first million digits of pi")
