def merge(items, temp, low, mid, high):
    i = low
    j = mid + 1
    for k in range(low, high + 1):
        if i > mid:
            temp[k] = items[j]
            j += 1
        elif j > high:
            temp[k] = items[i]
            i += 1
        elif items[j] < items[i]:
            temp[k] = items[j]
            j += 1
        else:
            temp[k] = items[i]
            i += 1
    for k in range(low, high + 1):
        items[k] = temp[k]

def merge_sort(items, temp, low, high):
    if high <= low:
        return None
    mid = low + (high - low) // 2
    merge_sort(items, temp, low, mid)
    merge_sort(items, temp, mid + 1, high)
    merge(items, temp, low, mid, high)