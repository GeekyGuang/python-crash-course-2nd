from random import randint


class Die:
    """A simple attempt to represent a die"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


die = Die()
die_20 = Die(20)

print("10-sided die")
for i in range(10):
    die.roll_die()

print("20-sided die")
for i in range(10):
    die_20.roll_die()
