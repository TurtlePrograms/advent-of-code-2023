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


def getinput():
    with open("input.txt", "r") as f:
        return f.read().splitlines()


def decode(line: str):
    found_numbers = []
    for validnumber in validnumbers:
        if str(validnumber) in line:
            line = line.replace(str(validnumber), "")
            found_numbers.append(validnumber)
    print(found_numbers)


def main():
    for line in getinput():
        decode(line)


main()
