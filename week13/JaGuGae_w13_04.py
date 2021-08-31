def merge(items, temp, low, mid, high):         # items: 정렬을 원하는 리스트, temp: 임시로 합병된 결과를 저장하기 위한 보조 리스트
    i = low                                     # 지역 변수 i와 j 선언 후
    j = mid + 1                                 # 입력 값 low와 high를 참조시킴
    for k in range(low, high + 1):              # 임시로 합병된 결과를 저장하기 위한 리스트 temp에 모든 원소가 저장될 때까지 반복
        if i > mid:                             # if items의 앞부분 원소들을 전부 temp에 저장하였다면
            temp[k] = items[j]                  # 뒷부분 남은 원소들을 차례로 temp에 저장
            j += 1
        elif j > high:                          # elif items의 뒷부분 원소들을 전부 temp에 저장하였다면
            temp[k] = items[i]                  # 앞부분 남은 원소들을 차례로 temp에 저장
            i += 1
        elif items[j] < items[i]:               # elif items[j] 값이 items[i]값보다 작으면
            temp[k] = items[j]                  # temp[k]에 items[j]를 저장하고
            j += 1                              # j를 1 증가시킴
        else:                                   # items[i] 값이 items[j]보다 작으면
            temp[k] = items[i]                  # temp[k]에 items[i]를 저장하고
            i += 1                              # i를 1 증가시킴
    for k in range(low, high + 1):              # temp에 모든 원소가 저장되어 라인 4 for 루프를 탈출했다면
        items[k] = temp[k]                      # temp의 내용을 items에 복사

def merge_sort(items, temp, low, high):
    if high <= low:                             # if items가 하나의 원소로 이루어졌다면
        return None                             # None값 반환 후 종료
    mid = low + (high - low) // 2               # items의 중간 원소의 인덱스 계산
    merge_sort(items, temp, low, mid)           # items의 앞부분에 대해 merge_sort 호출 (재귀 호출)
    merge_sort(items, temp, mid + 1, high)      # items의 뒷부분에 대해 merge_sort 호출 (재귀 호출)
    merge(items, temp, low, mid, high)          # merge 함수를 이용하여 합볌 및 정렬


if __name__ == "__main__":
    items = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
    temp = [None] * len(items)
    print("정렬 전:\t", end='')
    print(items)
    merge_sort(items, temp, 0, len(items) - 1)
    print("정렬 후:\t", end='')
    print(items)