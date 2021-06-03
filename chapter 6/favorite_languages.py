polls = {
  'lily': 'Python',
  'judy': 'Java',
  'cathy': 'JS',
  'andy': 'Python',
  'caven': 'C',
}

# 遍历键值对
for key,value in polls.items():
  print(f"{key}'s favorite language is {value}")

# 只遍历key, keys()得到由key组成的数组
for key in polls.keys():
  print(key)

# key排序
for key in sorted(polls.keys()):
  print(key)

# 与上面等价,默认是遍历key
for key in polls:
  print(key)

# 遍历值
for value in polls.values():
  print(value)

# value去重, set不允许存储重复值
for value in set(polls.values()):
  print(value)


# 声明一个set
a_set = {'cat', 'dog', 'cow', 'horse'}

