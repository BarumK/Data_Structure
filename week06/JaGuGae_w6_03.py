# 단순 연결 리스트로 구현한 스택
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

    def get_item(self):
        return self.item

    def get_next(self):
        return self.next

    def set_item(self, new_item):
        self.item = new_item

    def set_next(self, new_next):
        self.next = new_next

class Stack:
    def __init__(self):
        self.head = None # stack top

    def is_empty(self):
        return self.head == None

    def push(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def pop(self):
        if self.is_empty():
            return None
        else:
            popped_item = self.head.get_item()
            self.head = self.head.get_next()
            return popped_item

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.get_item()

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count