fruits = ['apple', 'banana', 'orange', 'pineapple', 'pear', 'plum']
print(fruits[1:4])  # index 1, 2, 3
print(fruits[2:])   # index 2到最后
print(fruits[:4])   # index 0到3
print(fruits[-3:])  # 最后3个
print(fruits[1:4:2])  # 第三个参数为步长，默认为1  index 1, 3
print(fruits[-3::-1])  # 步长为负数则反向 ['pineapple', 'orange', 'banana', 'apple']
print(fruits[:])  # 复制整个list

copied_fruits = fruits[:]
fruits.pop()
copied_fruits.append('coconut')
print(fruits)
print(copied_fruits)
