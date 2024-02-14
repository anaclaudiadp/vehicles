
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

    print("\n\nTotal of all vehicles:")
    print(sum(distances.values()))
