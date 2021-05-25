# sort
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# sorted
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
print(sorted(cars, reverse=True))
print(cars)


# 反转
cars.reverse()
print(cars)

# length
print(len(cars))

cars[100] = 'hahahaha'
print(cars)