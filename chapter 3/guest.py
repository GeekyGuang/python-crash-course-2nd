guests = ['Jose', 'Bruce Lee', 1900, 'Rose']

print(f"{guests[2]} please come for dinner")
print(f"{guests[-1]} please come for dinner")

print("sorry, 1900 can't make it to come")
guests.remove(1900)

print("I've found a bigger table")
guests.insert(1, 'Jack')
guests.insert(0, 'annie')
guests.insert(-1, 'robin')
guests.append('judy')
print(guests)

print("Sorry, I can only invite two people")
popped_name = guests.pop()
print(f"Sorry, {popped_name}")
popped_name = guests.pop(2)
print(f"Sorry, {popped_name}")
popped_name = guests.pop()
print(f"Sorry, {popped_name}")
popped_name = guests.pop(1)
print(f"Sorry, {popped_name}")
popped_name = guests.pop()
print(f"Sorry, {popped_name}")

print(guests)

del guests[0]
del guests[0]

print(guests)