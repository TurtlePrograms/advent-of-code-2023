def getinput():
    with open("input.txt", "r") as f:
        return f.read().splitlines()


def decode(line):
    characters = list(line)
    foundnums = []
    for char in characters:
        if char.isnumeric():
            foundnums.append(char)
    return foundnums


def gettotal(nums):
    num1 = nums[0]
    num2 = nums[-1]
    return str(num1) + str(num2)


def main():
    decoded = []
    for line in getinput():
        decoded.append(decode(line))
    totals = []
    for nums in decoded:
        totals.append(gettotal(nums))
    total = 0
    for num in totals:
        total += int(num)
    print(total)


main()
