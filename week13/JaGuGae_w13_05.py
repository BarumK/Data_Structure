def partion(items, pivot, high):
    i = pivot + 1                                       # 지역 변수 i와 j 선언 후
    j = high                                            # pivot + 1 (피봇 다음 위치)과 high (마지막 위치)를 참조시킴
    while True:                                         # break를 만나기 전까지 while 루프 실행
        while i < high and items[i] < items[pivot]:     # i가 리스트의 길이를 초과하지 않고, items[i]가 피봇보다 작으면
            i += 1                                      # i를 1씩 증가시킴
        while j > pivot and items[j] > items[pivot]:    # j가 피봇의 인덱스보다 크고, items[j]가 피봇보다 크면
            j -= 1                                      # j를 1씩 감소시킴
        if j <= i:                                      # if j <= i이면, 라인 4의 루프 탈출
            break
        items[i], items[j] = items[j], items[i]         # items[i]와 items[j] 교환
        i += 1                                          # i를 1 증가하고
        j -= 1                                          # j를 1 감소 후 라인 4의 while 루프 실행
    items[pivot], items[j] = items[j], items[pivot]     # 라인 4의 while 루프 탈출 후 피봇과 items[j] 교환 후
    return j                                            # 피봇의 인덱스 반환

def quick_sort(items, low, high):
    if low < high:                                      # if 리스트의 사이즈가 1보다 크면
        pivot = partion(items, low, high)               # partition 함수를 호출하여 두 개의 서브리스트로 분할(note: partition 함수는 피봇의 인덱스를 반환)
        quick_sort(items, low, pivot - 1)               # 왼쪽 서브리스트에 대해 퀵 정렬 수행(quick_sort 재귀호출)
        quick_sort(items, pivot + 1, high)              # 오른쪽 서브리스트에 대해 퀵 정렬 수행(quick_sort 재귀호출)


if __name__ == "__main__":
    items = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
    print("정렬 전: ", items)
    quick_sort(items, 0, len(items) - 1)
    print("정렬 후: ", items)