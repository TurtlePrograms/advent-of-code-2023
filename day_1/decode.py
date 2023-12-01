def getinput():
    with open("input.txt", "r") as f:
        return f.read().splitlines()


def decode(line):
    print(line)


def main():
    for line in getinput():
        decode(line)


main()
