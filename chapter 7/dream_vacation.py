vacation_polls = {}

while True:
    name = input("What's your name? ")
    vacation = input("If you could visit one place in the world," +
                     "\nwhere would you go? ")

    vacation_polls[name] = vacation

    another_poll = input("another poll? (yes/no)")
    if another_poll == 'no':
        break

for name, vacation in vacation_polls.items():
    print(f"{name}'s dream vacation is {vacation}")
