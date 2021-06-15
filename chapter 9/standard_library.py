from random import randint
from random import choice

print(randint(1, 6))  # 产生一个[1,6]区间的数

players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)  # 返回list或tuple中的任意一个元素
print(first_up)
