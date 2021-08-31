# 함수 재귀호출
"""
재귀 호출 함수는 두 부분으로 구성됨
1. 기본 케이스: 충분히 문제 크기가 작아져서 스스로를 더 이상 호출하지 않는 부분
2. 재귀 케이스: 스스로를 호출하는 부분
-> 분할 정복 방식에서 많이 쓰이게 된다.

if (some condition for which answer is known) # base case
    solution statement
else                                          # general case
    recursive function call
"""
def recursion1():
    print("Hello World!")
    recursion1()
# -> 이렇게 되면 실행시 무한루프

def recursion2(count):
    if count <= 0:
        print("Bye")
    else:
        print("Hello World!")
        recursion2(count - 1)

recursion2(5)

# Factorial 계산 재귀함수
# 조건식:
# Factorial(1) = 1
# Factorial(n) = n * Factorial(n - 1), for n >= 2
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4))
# 수행시간 T(n) = O(n)

# 피보나치 수열
# 조건식:
# fibo(0) = 1
# fibo(1) = 1
# fibo(n) = fibo(n - 1) + fibo(n - 2), for n >= 2
def fibo(n):
    if n <= 2:
        return 1
    else:
        return fibo(n - 2) + fibo(n - 1)

print(fibo(4))
# 수행시간 T(n) = O(2^n) -> 지수함수는 굉장히 좋지 않은 시간 복잡도 함수. 사용 안하는게 좋다. 동일 함수를 너무 반복함.

# 이진 탐색
def binary_search(dataset, left, right, target):
    if left > right:
        return "Not found"
    else:
        mid = (left + right) // 2
        if dataset[mid] == target:
            return mid
        elif dataset[mid] > target:
            return binary_search(dataset, left, mid - 1, target)
        else:
            return binary_search(dataset, mid + 1, right, target)

dataset = [1, 3, 5, 6, 7, 9, 11, 20, 30]
target = 5
i = binary_search(dataset, 0, 8, target)
print(i)