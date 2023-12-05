input = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""


# converts things like [[50, 98, 2],[52, 50, 48]] to [[range(first,first+last),range(second,second+last)],[range(first,first+last),range(second,second+last)]]
# (in this case [[range(50,50+2),range(98,98+2)],[range(52,52+48),range(50,50+48)]]) or [[[50,51],[98,99]],[52,53,54,55,...,(52+48-1)],[50,51,52,53,...,(50+48-1)]]]
def generate_map(map: str):
    lines = map.split("\n")
    numberlines = lines[1:]
    # converts the lines to lists of numbers
    for i in range(len(numberlines)):
        numbers = numberlines[i].split(" ")
        for j in range(len(numbers)):
            if numbers[j] != "":
                numbers[j] = int(numbers[j])
        numberlines[i] = numbers

    # converts the lists of numbers to lists of ranges
    for i in range(len(numberlines)):  # i is line number
        firstrange = range(numberlines[i][0], numberlines[i][0] + numberlines[i][2])
        secondrange = range(numberlines[i][1], numberlines[i][1] + numberlines[i][2])
        numberlines[i] = [firstrange, secondrange]

    # converts the lists of ranges to lists of numbers
    for i in range(len(numberlines)):
        firstrange = numberlines[i][0]
        secondrange = numberlines[i][1]
        firstlist = []
        secondlist = []
        for j in firstrange:
            firstlist.append(j)
        for j in secondrange:
            secondlist.append(j)
        numberlines[i] = [firstlist, secondlist]

    return numberlines


def calculate_soil(seed, seed_to_soil_map):
    destinationranges = []
    sourceranges = []
    index = None
    for i in range(len(seed_to_soil_map)):
        if seed in seed_to_soil_map[i][0]:
            destinationranges.append(seed_to_soil_map[i][1])
    for i in range(len(seed_to_soil_map)):
        if seed in seed_to_soil_map[i][1]:
            sourceranges.append(seed_to_soil_map[i][0])
    for i in range(len(destinationranges)):
        if seed in destinationranges[i]:
            index = destinationranges[i].index(seed)
    if index != None:
        if index in range(len(sourceranges[0])):
            return sourceranges[0][index]
    else:
        index = seed
    return index


def calculate_seeds(
    seed: int,
    seed_to_soil_map,
    soil_to_fertilizer_map,
    fertilizer_to_water_map,
    water_to_light_map,
    light_to_temperature_map,
    temperature_to_humidity_map,
    humidity_to_location_map,
):
    # calculate soil
    soil = calculate_soil(seed, seed_to_soil_map)
    print("soil is " + str(soil), "for seed", seed)


def main():
    print("start")
    lines = input.split("\n\n")
    seeds = lines[0].split(": ")[1].split(" ")
    for i in range(len(seeds)):
        seeds[i] = int(seeds[i])
    print(seeds)
    seed_to_soil_map = generate_map(lines[1])
    soil_to_fertilizer_map = None
    fertilizer_to_water_map = None
    water_to_light_map = None
    light_to_temperature_map = None
    temperature_to_humidity_map = None
    humidity_to_location_map = None

    # soil_to_fertilizer_map = generate_map(lines[2])
    # fertilizer_to_water_map = generate_map(lines[3])
    # water_to_light_map = generate_map(lines[4])
    # light_to_temperature_map = generate_map(lines[5])
    # temperature_to_humidity_map = generate_map(lines[6])
    # humidity_to_location_map = generate_map(lines[7])

    # run the simulation
    for i in range(len(seeds)):
        calculate_seeds(
            seeds[i],
            seed_to_soil_map,
            soil_to_fertilizer_map,
            fertilizer_to_water_map,
            water_to_light_map,
            light_to_temperature_map,
            temperature_to_humidity_map,
            humidity_to_location_map,
        )

    print("end")


main()
