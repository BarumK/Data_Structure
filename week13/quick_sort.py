def partion(items, pivot, high):
    i = pivot + 1
    j = high
    while True:
        while i < high and items[i] < items[pivot]:
            i += 1
        while j > pivot and items[j] > items[pivot]:
            j -= 1
        if j <= i:
            break
        items[i], items[j] = items[j], items[i]
        i += 1
        j -= 1
    items[pivot], items[j] = items[j], items[pivot]
    return j

def quick_sort(items, low, high):
    if low < high:
        pivot = partion(items, low, high)
        quick_sort(items, low, pivot - 1)
        quick_sort(items, pivot + 1, high)