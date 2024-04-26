def calc_distance(point1, point2):
    sum_squares = 0
    for i in range(len(point1)):
        sum_squares += (point2[i] - point1[i]) ** 2
    return sum_squares ** 0.5

def my_map(func, list1, list2):
    results = []
    for i in range(len(list1)):
        result = func(list1[i], list2[i])
        results.append(result)
    return results

points1 = [(1.0, 1.0, 1.0), (2.0, 2.0, 2.0), (3.0, 3.0, 3.0)]
points2 = [(4.0, 4.0, 4.0), (5.0, 5.0, 5.0), (6.0, 6.0, 6.0)]

distances = my_map(calc_distance, points1, points2)
print(distances)