sandwich_orders = ['ham', 'pastrami', 'apple',
                   'beacon', 'pastrami', 'tuna', 'pastrami']
finished_sandwiches = []

print("The Deli has run out of Pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

making = True
while making:
    if sandwich_orders:
        current = sandwich_orders.pop()
        print(f"I made your {current} sandwiches")

        finished_sandwiches.append(current)
    else:
        making = False

print(finished_sandwiches)
