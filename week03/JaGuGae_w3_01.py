# Python의 데이터 타입
# 1. 스칼라 데이터타입
print(23, type (23)) # int
print(23.5, type(23.5)) # float
print(None, type(None)) # None
print(True, type(True), False, type(False)) # bool

# 2. 컬렉션 데이터타입
# 다른 객체들의 참조들을 담아 객체들의 모음을 표현하는 데이터타입
# 순서열(문자열, 리스트, 튜플), 매핑(dict), 집합(set) 데이터타입이 있다. 자구개는 리스트 위주.
a = list() # == a = []
a = [1, 1.5, "string"] # 데이터의 참조를 조정한다.
print(a, type(a))
print(a, id(a))
a[0] = 3
print(a, id(a))

a = [None] * 5
b = [40, 10, 70, 60]
print(a)
print(b[0])
print(b[-1])
b.pop()
b.pop(0)
b.append(90)
print(b, len(b))

# 리스트를 스택처럼 사용할 수 있음 -> 한 쪽 끝에서 삽입, 삭제가 이루어지는 선형 구조
stack = []
stack.append(1)
print(stack)
stack.append(2)
print(stack)
stack.append(3)
print(stack)
stack.pop()
print((stack))
stack.pop()
print((stack))

# 리스트를 큐처럼 사용할 수 있음 -> 한 쪽 끝에서 삽입이 이루어지면 다른 한 쪽 끝에선 삭제가 이루어지는 선형 구조
queue = []
queue.append(1)
print(queue)
queue.append(2)
print(queue)
queue.append(3)
print(queue)
queue.pop(0)
print(queue)
queue.pop(0)
print(queue)

# 두 가지 방식의 문제점?
# 아무 데서나 다 뽑아낼 수 있고 리스트에 적용 가능한 연산들을 할 수 있다. 리스트니까.
# 스택의 탑에서만 이루어져야하는게 다른데에서도 이루어질 수도 있어 스택의 기능을 상실할 수 있다.
# 큐 또한 마찬가지.
# 해결법: 사용자 데이터타입의 스택과 큐를 만들어 pop에는 인자를 받지 못하게 제한해야함.