class Node:
    def __init__(self, key, data, link):
        self.key = key
        self.data = data
        self.next = link

class Chaining:
    def __init__(self, size):
        self.m = size
        self.table = [None for x in range(size + 1)]

    def hash(self, key):
        return key % self.m

    def insert(self, key, data):
        i = self.hash(key)
        p = self.table[i]
        while p != None:
            if key == p.key:
                p.data = data
                return None
            p = p.next
        self.table[i] = Node(key, data, self.table[i])

    def search(self, key):
        i = self.hash(key)
        p = self.table[i]
        while p != None:
            if key == p.key:
                return p.data
            p = p.next
        return None

    def delete(self, key):
        i = self.hash(key)
        p = self.table[i]
        previous = None
        while p != None:
            if key == p.key:
                if previous == None:
                    self.table[i] = p.next
                else:
                    previous.next = p.next
                return None
            previous = p
            p = p.next