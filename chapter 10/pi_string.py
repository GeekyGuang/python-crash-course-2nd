file_name = 'pi_digits.txt'

with open(file_name) as file_object:
  file_list = file_object.readlines()

pi_string = ''
for line in file_list:
  pi_string += line.strip()

print(pi_string[:12])


