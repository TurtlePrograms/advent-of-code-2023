numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
spelledNums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def getinput():
    with open("input.txt", "r") as f:
        return f.read().splitlines()


def decode(input):
    #     print(input, type(input))
    characterers = [x for x in input]
    first = None
    foundfirst = False
    last = None
    foundlast = False
    explored = ""
    for i in range(len(characterers)):
        explored = explored + characterers[i]

        for spelledNum in spelledNums:
            if foundfirst:
                break
            if spelledNum in explored and not foundfirst:
                first = spelledNums.index(spelledNum) + 1
                # print("found " + spelledNum, "in", explored)
                foundfirst = True
            if str(spelledNums.index(spelledNum) + 1) in explored and foundfirst:
                first = spelledNums.index(spelledNum) + 1
                # print("found " + str(spelledNums.index(spelledNum) + 1), "in", explored)
                foundfirst = True

    explored = ""
    for i in range(len(characterers) - 1, 0 - 1, -1):
        explored = characterers[i] + explored
        # print(explored)
        for spelledNum in spelledNums:
            if foundlast:
                break
            if spelledNum in explored and not foundlast:
                last = spelledNums.index(spelledNum) + 1
                # print("found " + spelledNum, "in", explored)
                foundlast = True
            if str(spelledNums.index(spelledNum) + 1) in explored and foundlast:
                last = spelledNums.index(spelledNum) + 1
                # print("found " + str(spelledNums.index(spelledNum) + 1), "in", explored)
                foundlast = True

    return first, last


def main():
    input = getinput()
    decoded = []
    for line in input:
        decoded.append(decode(line))
    for i in range(len(decoded)):
        print(i + 1, decoded[i])


main()
"""
1 22
2 94
3 26
4 28
5 57
6 47
7 69
8 95
9 52
10 11
"""
