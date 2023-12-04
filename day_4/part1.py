def getinput():
    with open(r"day_4\input.txt") as f:
        lines = f.readlines()
    return lines


def parse_lists(lst):
    toremove = []
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == "":
            toremove.append(i)
    for i in toremove:
        lst.pop(i)
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    return lst


def getwinningscore(winning, numbers):
    score = 0
    for i in range(len(winning)):
        if winning[i] in numbers:
            score += 1
    worth = 0

    if score >= 1:
        worth = 1
        score -= 1
    if score > 0:
        for i in range(0, score):
            worth *= 2
    return worth


def parse_card(line):
    id = line.split(":")[0].split(" ")[1]
    winning = line.split(":")[1].split("|")[0].split(" ")
    numbers = line.split(":")[1].split("|")[1].split(" ")
    winning = parse_lists(winning)
    numbers = parse_lists(numbers)
    return id, winning, numbers


def main():
    total = 0
    for line in getinput():
        id, winning, losing = parse_card(line)
        score = getwinningscore(winning, losing)
        total += score
    print(total)


main()
