def getinput():
    with open("day_3\\input.txt", "r") as f:
        return f.read()


def getFullNumber(data, row, col):
    fullNumber = ""
    point = data[row][col]
    # find starting point of number
    while point in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        try:
            col -= 1
            point = data[row][col]
        except IndexError:
            break
    try:
        col += 1
        point = data[row][col]
    except IndexError:
        pass

    while point in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        try:
            point = data[row][col]
            fullNumber += point
            col += 1
        except IndexError:
            break
    for item in [".", "*", "#", "$", "\\", "/", "+", "-", "@", "&", "=", "%"]:
        fullNumber = fullNumber.replace(item, "")
    if fullNumber == "":
        return "0"
    return fullNumber


def sumNumbers(data):
    total_sum = 0
    for row in range(len(data)):
        usednumbers = []
        for col in range(len(data[row])):
            if data[row][col].isdigit():
                if any(
                    (
                        symbol != "."
                        and symbol
                        not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
                    )
                    for symbol in getAdjacentSymbols(data, row, col)
                ):
                    fullNumber = getFullNumber(data, row, col)
                    if fullNumber not in usednumbers:
                        usednumbers.append(fullNumber)
                        total_sum += int(fullNumber)
                        if fullNumber == "0":
                            print("found at row: " + str(row) + " col: " + str(col))
    return total_sum


def getAdjacentSymbols(data, row, col, depth=0):
    adjacent_symbols = []
    for i in range(-1 - depth, 2 + depth):
        for j in range(-1, 2):
            if row + i >= 0 and col + j >= 0:
                try:
                    adjacent_symbols.append(data[row + i][col + j])
                except IndexError:
                    pass
    return adjacent_symbols


data = getinput().split("\n")
total = sumNumbers(data)
print("\nTotal:")
print(total)
