from random import choice
possibilities = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']


def generate_lottery():
    result = []
    while len(result) < 4:
        generate = choice(possibilities)

        if generate not in result:
            print(f"We pull out a {generate}")
            result.append(generate)

    return result


def check_ticket(played_ticket, lottery_ticket):
    for item in played_ticket:
        if item not in lottery_ticket:
            return False

    return True


lottery = generate_lottery()

count = 0
while True:
    count += 1
    my_lottery = generate_lottery()
    if check_ticket(my_lottery, lottery):
        print("You win the lottery")
        break

print(count)
