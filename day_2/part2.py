def getinput():
    with open("day_2\\input.txt", "r") as f:
        return f.read().splitlines()


def control_game(line):
    id = line.split(":")[0].split(" ")[1]
    games = line.split(":")[1].split(";")
    blue = 0
    red = 0
    green = 0
    for game in games:
        newblue = 0
        newred = 0
        newgreen = 0
        game = game.split(",")
        for i in range(len(game)):
            if "blue" in game[i]:
                amount = int(game[i].split(" ")[1])
                newblue += amount
            if "red" in game[i]:
                amount = int(game[i].split(" ")[1])
                newred += amount
            if "green" in game[i]:
                amount = int(game[i].split(" ")[1])
                newgreen += amount
        if newblue > blue:
            blue = newblue
        if newred > red:
            red = newred
        if newgreen > green:
            green = newgreen
    print("red, green, blue")
    print(red, green, blue)
    power = red * green * blue
    return power


def main():
    lines = getinput()
    power = []
    for line in lines:
        power.append(control_game(line))
    total = sum(power)
    print(total)


main()
