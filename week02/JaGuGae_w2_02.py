# 선형 탐색 알고리즘에 대한 최악의 경우 분석
def linear_search(target, dataset):
    for i in range(len(dataset)):
        if dataset[i] == target: # 기본 연산 부분
            return i
    return "Not found"

dataset = [15, 40, 30, 80, 10, 70, 50, 90, 20, 95]
result = linear_search(95, dataset)

# 실행 횟수: 10 (n회 중 n회 실행되는 최악의 경우), -> 입력 크기가 n일 경우 W(n) = n