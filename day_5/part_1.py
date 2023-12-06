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


def turn_to_range(list_of_lists):
    # input:
    # [[50, 98, 2], [52, 50, 48]]
    # output:
    # [[[range(50, 100)], [range(52, 100)]],[[range(98,100)], [range(50,48)]]]
    for i, list in enumerate(list_of_lists):
        for j, num in enumerate(list):
            if j == 0:
                list_of_lists[i][j] = [range(num, 100)]
            elif j == 1:
                list_of_lists[i][j] = [range(list_of_lists[i][j - 1], num)]
            else:
                list_of_lists[i][j] = [(range(list_of_lists[i][j - 1], num))]
    return list_of_lists


def main():
    data = input.strip().split("\n\n")
    seeds = [int(s) for s in data[0].split()[1:]]
    seed_to_soil = [
        [int(s) for s in line.split()] for line in data[1].split("\n")[1:]
    ]  # [[50, 98, 2], [52, 50, 48]]
    soil_to_fertilizer = [
        [int(s) for s in line.split()] for line in data[2].split("\n")[1:]
    ]  # [[0, 15, 37], [37, 52, 2], [39, 0, 15]]
    fertilizer_to_water = [
        [int(s) for s in line.split()] for line in data[3].split("\n")[1:]
    ]  # [[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]]
    water_to_light = [
        [int(s) for s in line.split()] for line in data[4].split("\n")[1:]
    ]  # [[88, 18, 7], [18, 25, 70]]
    light_to_temperature = [
        [int(s) for s in line.split()] for line in data[5].split("\n")[1:]
    ]  # [[45, 77, 23], [81, 45, 19], [68, 64, 13]]
    temperature_to_humidity = [
        [int(s) for s in line.split()] for line in data[6].split("\n")[1:]
    ]  # [[0, 69, 1], [1, 0, 69]]
    humidity_to_location = [
        [int(s) for s in line.split()] for line in data[7].split("\n")[1:]
    ]  # [[60, 56, 37], [56, 93, 4]]

    seed_to_soil = turn_to_range(seed_to_soil)
    soil_to_fertilizer = turn_to_range(soil_to_fertilizer)
    fertilizer_to_water = turn_to_range(fertilizer_to_water)
    water_to_light = turn_to_range(water_to_light)
    light_to_temperature = turn_to_range(light_to_temperature)
    temperature_to_humidity = turn_to_range(temperature_to_humidity)
    humidity_to_location = turn_to_range(humidity_to_location)

    print(
        seed_to_soil,
        soil_to_fertilizer,
        fertilizer_to_water,
        water_to_light,
        light_to_temperature,
        temperature_to_humidity,
        humidity_to_location,
        sep="\n",
    )


main()
