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


    maximum1 = reduce(function, distances.items())
    # maximum using a function
    maximum2 = reduce(lambda top, each: each if top[1] < each[1] else top, distances.items())
    # maximum using a lambda and a ternary statement

    print(maximum1)
    print(maximum2)

