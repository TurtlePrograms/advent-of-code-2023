validnumbers = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    0,
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "zero",
]
stringnumbers = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "zero",
]


def getinput():
    with open("input.txt", "r") as f:
        return f.read().splitlines()


def stringtonumbers(line):
    for string in stringnumbers:
        if string in line:
            line = line.replace(string, str(stringnumbers.index(string) + 1))
    return line


def decode(line: str):
    line = stringtonumbers(line)
    foundnumbers = []
    for number in validnumbers:
        if str(number) in line:
            foundnumbers.append(number)
    return foundnumbers


def decodestring(number):
    if number == "one":
        return 1
    elif number == "two":
        return 2
    elif number == "three":
        return 3
    elif number == "four":
        return 4
    elif number == "five":
        return 5
    elif number == "six":
        return 6
    elif number == "seven":
        return 7
    elif number == "eight":
        return 8
    elif number == "nine":
        return 9
    elif number == "zero":
        return 0
    else:
        return number


def count(foundnumbers):
    total = 0
    for foundnumberlist in foundnumbers:
        number1 = decodestring(foundnumberlist[0])
        number2 = decodestring(foundnumberlist[-1])
        print(number1, number2)
        sum = str(number1) + str(number2)
        total += int(sum)
    return total


def main():
    decoded = []
    for line in getinput():
        decoded.append(decode(line))
    total = count(decoded)
    print(total)


main()
