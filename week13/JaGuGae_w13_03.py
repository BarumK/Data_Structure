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


if __name__ == "__main__":
    items = [39, 23, 15, 47, 11, 56, 61, 16, 12, 19, 21, 41]
    print('힙 정렬 전: ', end='')
    print(items)
    heapify(items)
    print('최대 힙: ', end='')
    print(items)
    heap_sort(items)
    print('힙 정렬 후: ', end='')
    print(items)