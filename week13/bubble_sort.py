def bubble_sort(item):
    for i in range(len(item) - 1, 0, -1):
        for j in range(i):
            if item[j] > item[j + 1]:
                item[j], item[j + 1] = item[j + 1], item[j]