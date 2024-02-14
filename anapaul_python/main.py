from functools import reduce

if __name__ == '__main__':
    left = open('../left.csv', 'r')
    distances = {}

    for line in left.readlines():
        data = line.strip('\n').split(',')
        distance = distances[data[1]] if data[1] in distances else 0
        distances[data[1]] = distance + int(data[2])

    print("\n\nDistances for vehicles:")
    for k, v in distances.items():
        print(k, v)

    # Question 2
    print("\n\nTotal of all vehicles:")
    print(sum(distances.values()))
    print(reduce(lambda acc, each: acc + each, distances.values()))
    # this reducer is adding the values together one at a time, then returning the the total - the same as sum.

    def function(top, each):
        if top is None:
            return each

        if top[1] < each[1]:
            return each
        else:
            return top

    # Question 3
    maximum1 = reduce(function, distances.items())
    # maximum using a function
    maximum2 = reduce(lambda top, each: each if top[1] < each[1] else top, distances.items())
    # maximum using a lambda and a ternary statement
    maximum3 = max(distances.items(), key=lambda d: d[1])

    print(maximum1)
    print(maximum2)
    print(maximum3)

    # Question 4

    left = open('../left.csv', 'r')
    collection = {}

    for line in left.readlines():
        data = line.strip('\n').split(',')

        vehicle_name = data[1]
        if vehicle_name not in collection:
            five_minutes = []
            collection[vehicle_name] = (five_minutes, 0)

        five_minutes = collection[vehicle_name][0]

        distance = int(data[2])
        if len(five_minutes) < 5:
            five_minutes.append(distance)
            continue

        minutes_distance = sum(five_minutes[1:]) + distance
        five_minutes.pop(0)
        five_minutes.append(distance)
        collection[vehicle_name] = (five_minutes, minutes_distance)\
            if collection[vehicle_name][1] < minutes_distance\
            else (five_minutes, collection[vehicle_name][1])

    print(
        "\n\nFurthest 5 minute interval\nVehicle: {0[0]}\nDistance: {0[1]}"
        .format(max(map(lambda e: (e[0], e[1][1]), collection.items()), key=lambda e: e[1]))
    )

    # Question 5
    left = open('../left.csv', 'r')

    vehicle_names = list(distances.keys())
    passing = dict()
    v1 = vehicle_names[0]
    v2 = vehicle_names[1]
    passing[v1] = 0
    passing[v2] = 0

    times_passed = 0

    times = dict()

    for line in left.readlines():
        data = line.strip('\n').split(',')
        vehicle_id = data[1]

        if data[0] not in times:
            times[data[0]] = (0, 0)

        if vehicle_id == v1:
            times[data[0]] = (data[2], times[data[0]][1])
        elif vehicle_id == v2:
            times[data[0]] = (times[data[0]][0], data[2])

    for time, data in times.items():
        current_distance_v1 = passing[v1] + int(data[0])
        current_distance_v2 = passing[v2] + int(data[1])

        if passing[v1] < passing[v2] and current_distance_v2 < current_distance_v1:
            times_passed = times_passed + 1

        passing[v1] = current_distance_v1
        passing[v2] = current_distance_v2

    # Question 5
    print("\n\nVehicle 1 passed Vehicle 2 %d times" % times_passed)

