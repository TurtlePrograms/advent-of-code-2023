def getinput():
    with open("day_2\\input.txt", "r") as f:
        return f.read().splitlines()


def control_game(line):
    id = line.split(":")[0].split(" ")[1]
    games = line.split(":")[1].split(";")
    blue = 0
    red = 0
    green = 0
    bluemax = 14
    redmax = 12
    greenmax = 13
    for game in games:
        blue = 0
        red = 0
        green = 0
        game = game.split(",")
        for i in range(len(game)):
            if "blue" in game[i]:
                amount = int(game[i].split(" ")[1])
                blue += amount
            if "red" in game[i]:
                amount = int(game[i].split(" ")[1])
                red += amount
            if "green" in game[i]:
                amount = int(game[i].split(" ")[1])
                green += amount
        if blue > bluemax or red > redmax or green > greenmax:
            return 0
    if blue > bluemax or red > redmax or green > greenmax:
        return 0
    else:
        return int(id)


def main():
    lines = getinput()
    ids = []
    for line in lines:
        ids.append(control_game(line))
    total = sum(ids)
    print(total)


main()
