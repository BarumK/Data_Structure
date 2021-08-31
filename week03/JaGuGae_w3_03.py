# Python에서의 함수의 정의
# def 키워드를 이용한 정의
"""
def 함수명(매개변수 목록):
    명령문
    ...
    return 결과
"""
def myabs(x):
    if x < 0:
        x = -x
    return x

a = myabs(-2)
print(a)

# 시간복잡도 연습: 입력 크기 n에 대한 각 함수의 연산 수행 시간 복잡도를 Big-Oh 표기법으로 표현하면?
def func1(n): # O(1)
    print("Hi") # 기본연산

def func2(n): # O(n)
    for i in range(n):
        print("Hi") # 기본연산

def func3(n): # O(n^2)
    for i in range(n):
        for j in range(n):
            print("Hi") # 기본연산