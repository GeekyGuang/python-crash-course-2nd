motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# 修改
motorcycles[0] = 'ducati'
print(motorcycles)

# 加到末尾
motorcycles.append('ducati')
print(motorcycles)

# 插入
motorcycles.insert(2, 'hhhh')
print(motorcycles)

# 从指定index移除
del motorcycles[2]
print(motorcycles)

# 从末尾移除，并得到移除的值
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)