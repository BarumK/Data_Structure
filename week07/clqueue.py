# 환형 연결 리스트로 구현한 큐
from node import Node
class Queue:
    def __init__(self):
        self.head = None # 큐 rear

    def is_empty(self):
        return self.head == None

    def enqueue(self, item):
        temp = Node(item)
        if self.is_empty():
            temp.set_next(temp)
            self.head = temp
        else:
            temp.set_next(self.head.get_next())
            self.head.set_next(temp)
            self.head = temp

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            temp = self.head.get_next()
            dequeued_item = temp.get_item()
            if temp == temp.get_next():
                self.head = None
            else:
                self.head.set_next(temp.get_next())
            return  dequeued_item

    def size(self):
        count = 0
        if self.is_empty():
            return count
        temp = self.head.get_next()
        current = temp
        while True:
            count += 1
            current = current.get_next()
            if current != temp:
                continue
            else:
                break
        return count