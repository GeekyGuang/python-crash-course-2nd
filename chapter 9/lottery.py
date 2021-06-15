from random import choice
possibilities = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']
result = []

while len(result) < 4:
    generate = choice(possibilities)

    if generate not in result:
        print(f"We pull out a {generate}")
        result.append(generate)


print(f"Any ticket matching {result} wins a prize")
