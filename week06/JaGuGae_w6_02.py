"""
-스택(Stack)
한 쪽 끝 위치(Top)에서만 새로운 항목을 삽입(Push)하거나 기존 항목을 삭제 및 반환(Pop)하는 논리적 선형 구조
시간 순으로 먼저 삽입된 항목이 나중에 삭제되는 Last In, First Out(후입선출) 구조
Top에서만 삽입, 삭제가 이루어지는(적용 가능한 연산이 제한된) 특수한 리스트(List) -> 리스트보다 구현하기 쉽다

-스택의 (물리적) 구현
Python 리스트(동적 배열)에 의한 구현 -> push, pop 연산의 시간복잡도 O(1)
단순 연결 리스트(Singly Linked List)에 의한 구현 -> push, pop 연산의 시간복잡도 O(1)

-Python 리스트로 구현한 스택
append(item)와 pop() 메소드로 push(item)와 pop() 구현 가능
하지만 Python 리스트를 그대로 사용하되
한쪽 끝에서만 item을 삽입, 삭제하기로 약속하는 것보다 item 삽입,삭제 위치를 스택 Top으로 제한하는 것이 더 바람직하므로 Stack 클래스를 정의

-단순 연결 리스트로 구현한 스택
단순 연결 리스트의 add(item)와 (항목 반환을 위해) 수정된 pop_first() 메소드로 push(item)와 pop() 구현 가능
위에서 언급한 대로, 단순 연결 리스트를 수정하여 사용하되 한쪽 끝(head)에서만 item을 삽입, 삭제하기로 약속하는 것보다,
item 삽입, 삭제 위치를 스택 Top으로 제한하는 것이 더 바람직하므로 Stack 클래스를 정의
"""
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    # 리스트로 구현한 스택
    stack = []
    stack.append(1)
    print(stack)
    stack.append(2)
    print(stack)
    stack.append(3)
    print(stack)
    stack.pop()
    print(stack)
    stack.pop()
    print(stack)

    # Stack 클래스 정의 및 일련의 스택 연산과 출력
    s = Stack()
    print(s.is_empty())
    s.push(4)
    s.push("dog")
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.is_empty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())
