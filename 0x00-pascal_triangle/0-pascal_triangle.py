#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle, buffer_list = [], []
    for x in range(n):
        if x == 0:
            triangle.append([1])
            continue
        if x == 1:
            triangle.append([1, 1])
            continue

        sum_list = triangle[-1]
        for i in range(len(sum_list) + 1):
            if i in [0, len(sum_list)]:
                buffer_list.append(1)
                continue
            buffer_list.append(sum_list[i] + sum_list[i - 1])

        triangle.append(buffer_list)
        buffer_list = []

    return triangle
