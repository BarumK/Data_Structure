def selection_sort(items):
    for i in range(0, len(items) - 1):
        minimun = i
        for j in range(i, len(items)):
            if items[minimun] > items[j]:
                minimum = j
        items[i], items[minimum] = items[minimum], items[i]