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
    for i in range(0, len(characterers)):
        explored = explored + characterers[i]

        for spelledNum in spelledNums:
            if spelledNum in explored and not foundfirst:
                first = spelledNums.index(spelledNum) + 1
                print("found " + spelledNum, "in", explored)
                foundfirst = True
            if str(spelledNums.index(spelledNum) + 1) in explored and not foundfirst:
                first = spelledNums.index(spelledNum) + 1
                print("found " + str(spelledNums.index(spelledNum) + 1), "in", explored)
                foundfirst = True
    print("first", first)
    explored = ""
    for i in reversed(range(len(characterers))):
        explored = characterers[i] + explored
        # print(explored)
        for spelledNum in spelledNums:
            if foundlast:
                break
            if spelledNum in explored and not foundlast:
                last = spelledNums.index(spelledNum) + 1
                print("found " + spelledNum, "in", explored)
                foundlast = True
            if str(spelledNums.index(spelledNum) + 1) in explored and not foundlast:
                last = spelledNums.index(spelledNum) + 1
                print("found " + str(spelledNums.index(spelledNum) + 1), "in", explored)
                foundlast = True

    return str(first) + str(last)


def main():
    input = getinput()
    decoded = []
    for line in input:
        decoded.append(decode(line))
    total = 0
    for i in range(len(decoded)):
        print(i + 1, decoded[i])
        total = total + int(decoded[i])
    print("total", total)


main()
