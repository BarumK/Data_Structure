"""
+) 평균의 경우 분석
입력 값의 확률 분포를 "가정"해야 한다. 그 후 평균을 계산하는 것이므로 주로 평균보다는 최악의 경우를 많이 분석한다.

+) 모든 경우의 분석
복잡도가 항상 일정한 경우에만 모든 경우의 분석이 가능함
-> 즉, 모든 경우의 경우의 분석이 가능하다면 최악, 최선, 평균의 경우 시간 복잡도가 동일함
"""

# 모든 경우의 분석 예시
def sum(dataset):
    result = 0
    for i in dataset:
        result += i # 기본연산
    return result

dataset = [15, 40, 30, 80, 10, 70, 50, 90, 20, 95]
result = sum(dataset)
# 입력 크기 n: 10
# 리스트 안의 값과 상관없이 기본 연산이 n번 수행되므로 모든 경우 시간 복잡도 T(n) = n