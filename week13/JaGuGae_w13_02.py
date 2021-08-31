def selection_sort(items):
    for i in range(0, len(items) - 1):
        minimun = i
        for j in range(i, len(items)):
            if items[minimun] > items[j]:
                minimum = j
        items[i], items[minimum] = items[minimum], items[i]

def insertion_sort(items):
    for i in range(1, len(items)):                                  # Python 리스트 items의 첫 번째 원소 items[0]은 이미 정렬된 부분이므로 i = 1부터 시작
        for j in range(i, 0, -1):                                   # 뒤에서 앞으로 비교해 나간다는 것에 유의
            if items[j - 1] > items[j]:
                items[j], items[j - 1] = items[j - 1], items[j]
            else:
                break

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


if __name__ == "__main__":
    items = [40, 70, 60, 30, 10, 50]
    print('선택 정렬 전: ', end='')
    print(items)
    selection_sort(items)
    print('선택 정렬 후: ', end='')
    print(items)

    items = [40, 70, 60, 30, 10, 50]
    print('삽입 정렬 전: ', end='')
    print(items)
    insertion_sort(items)
    print('삽입 정렬 후: ', end='')
    print(items)

    items = [39, 23, 15, 47, 11, 56, 61, 16, 12, 19, 21, 41]
    print('셸 정렬 전: ', end='')
    print(items)
    shell_sort(items)
    print('셸 정렬 후: ', end='')
    print(items)