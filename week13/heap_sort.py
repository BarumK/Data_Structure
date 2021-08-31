def downheap(i, size):
    while (2 * i + 1) <= size:
        k = 2 * i + 1
        if (k < size - 1) and (items[k] < items[k + 1]):
            k += 1
        if items[i] >= items[k]:
            break
        items[i], items[k] = items[k], items[i]
        i = k

def heapify(items):
    hsize = len(items)
    for i in range(hsize // 2 - 1, -1, -1):
        downheap(i, hsize)

def heap_sort(items):
    N = len(items)
    for i in range(N):
        items[0], items[N - 1] = items[N - 1], items[0]
        downheap(0, N - 2)
        N -= 1