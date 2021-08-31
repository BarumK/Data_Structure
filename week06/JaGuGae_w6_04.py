"""
-큐(Queue)
한쪽 끝 위치(Rear)에서 새로운 항목을 삽입(Enqueue)하고, 다른 한 쪽 끝 위치(Front)에서 기존 항목을 삭제 및 반환(Dequeue)하는 논리적 선형 구조
시간 순으로 먼저 삽입된 항목이 먼저 삭제되는 선입선출(First in, first out) 구조
Rear(끝)에서만 삽입이 이루어지고 Front(앞)에서만 삭제가 이루어지는 (적용 가능한 연산이 제한된) 특수한 리스트 -> 구현이 쉽다

-큐의 물리적 구현
Python 리스트(동적 배열)에 의한 구현 - enqueue 연산의 시간복잡도 O(1), dequeue 연산의 시간복잡도 O(n)
단순 연결 리스트에 의한 구현 - enqueue 연산의 시간 복잡도 O(n), dequeue 연산의 시간복잡도 O(1)
환형 연결 리스트에 의한 구현 - enqueue, dequeue 연산의 시간 복잡도 O(1)

-Python 리스트로 구현한 큐
append(item)와 pop(0) 메소드로 enqueue(item)와 dequeue() 구현 가능하지만,
Stack 클래스를 정의한 이유와 동일한 이유로 Queue 클래스 정의
"""
class Queue:
    def __init__(self):
        self.items= []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop(0)

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    q = Queue()
    print(q.is_empty())
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    print(q.size())
    print(q.is_empty())
    q.enqueue(8.4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.size())