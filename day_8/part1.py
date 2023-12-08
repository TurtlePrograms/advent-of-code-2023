def get_input():
    with open("input.txt") as f:
        return f.read().splitlines()


def getareas(lines):
    areas = {}
    for line in lines:
        if line == "":
            continue
        data = line.split(" ")
        name = data[0]
        left = data[2].split(",")[0]
        right = data[3].split(",")[0]
        left = left.split("(")[1]
        right = right.split(")")[0]
        areas[name] = [left, right]

    return areas


def run(directions, areas):
    keys = list(areas.keys())
    index = keys.index("AAA")
    currentArea = keys[index]
    total = 0
    print(currentArea)
    while currentArea != "ZZZ":
        print("loop")
        for i in range(len(directions)):
            if i % 1000 == 0:
                print(total, currentArea)
            total += 1

            if currentArea == "ZZZ":
                print(
                    "Reached SPQ at index",
                    i,
                    "with direction",
                    directions[i],
                    "and area",
                    currentArea,
                )
                break
            if directions[i] == "R":
                currentArea = areas[currentArea][1]
            elif directions[i] == "L":
                currentArea = areas[currentArea][0]
    print(currentArea, total)


def main():
    lines = get_input()
    directions = list(lines[0])
    areas = getareas(lines[1:])
    run(directions, areas)


main()
