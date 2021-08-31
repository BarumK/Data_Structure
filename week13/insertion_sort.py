def insertion_sort(items):
    for i in range(1, len(items)):
        for j in range(i, 0, -1):
            if items[j - 1] > items[j]:
                items[j], items[j - 1] = items[j - 1], items[j]
            else:
                break