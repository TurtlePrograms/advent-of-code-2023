def calculate_ways_to_beat_record(times, distances):
    total_ways = []
    min_time = 0
    max_time = 0

    for i in range(len(times)):
        race_ways = 0
        print(f"{i} - {times[i]}")
        for j in range(0, times[i]):
            if min_time != 0:
                break
            hold_time = j
            speed = hold_time
            movetime = times[i] - hold_time
            distance = speed * movetime
            if distance > distances[i]:
                print(
                    f"hold_time: {hold_time}- movetime: {movetime} - speed: {speed} - distance: {distance}"
                )
                min_time = hold_time
                break

    for i in range(len(times)):
        race_ways = 0
        print(f"{i} - {times[i]}")
        for j in range(times[i], 0, -1):
            if max_time != 0:
                break
            hold_time = j
            speed = hold_time
            movetime = times[i] - hold_time
            distance = speed * movetime
            if distance > distances[i]:
                print(
                    f"hold_time: {hold_time}- movetime: {movetime} - speed: {speed} - distance: {distance}"
                )
                max_time = hold_time
                break

    print(f"min_time: {min_time} - max_time: {max_time}")
    total_ways.append(max_time)
    total_ways.append(min_time)
    return total_ways


times = [53916768]
distances = [250133010811025]


result = calculate_ways_to_beat_record(times, distances)
total = result[0] - result[1]
print(result, "result")

print(total + 1)
