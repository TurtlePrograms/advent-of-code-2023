def calculate_ways_to_beat_record(times, distances):
    total_ways = []  # Initialize the total ways to beat the record

    for i in range(len(times)):
        race_ways = 0  # Initialize the ways for the current race
        print(f"{i} - {times[i]}")
        for j in range(0, times[i]):
            hold_time = j
            speed = hold_time
            movetime = times[i] - hold_time
            distance = speed * movetime
            if distance > distances[i]:
                print(
                    f"hold_time: {hold_time}- movetime: {movetime} - speed: {speed} - distance: {distance}"
                )
                race_ways += 1
        total_ways.append(race_ways)
    return total_ways


# Example input
times = [7, 15, 30]
distances = [9, 40, 200]

result = calculate_ways_to_beat_record(times, distances)
total = 1
for i in result:
    total *= i
print(result)
print(total)
