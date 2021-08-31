def shell_sort(items):
    h = len(items) // 2
    while h >= 1:
        for i in range(h, len(items)):
            j = i
            while j >= h and items[j] < items[j - h]:
                items[j], items[j - h] = items[j - h], items[j]
                j -= h
        print("{}-정렬 결과: ".format(h), items)
        h //= 2