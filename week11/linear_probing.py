class LinearProbing:
    def __init__(self, size):
        self.m = size
        self.k = [None for _ in range(size + 1)]
        self.d = [None for _ in range(size + 1)]

    def hash(self, key):
        return key % self.m

    def insert(self, key, data):
        initial_position = self.hash(key)
        i = initial_position
        j = 0
        while True:
            if self.k[i] == None or self.k[i] == '$':
                self.k[i] = key
                self.d[i] = data
                return None
            if self.k[i] == key:
                self.d[i] = data
                return None
            j += 1
            i = (initial_position + j) % self.m
            if i == initial_position:
                break

    def search(self, key):
        initial_position = self.hash(key)
        i = initial_position
        j = 0
        while self.k[i] != None:
            if self.k[i] == key:
                return self.d[i]
            j += 1
            i = (initial_position + j) % self.m
            if i == initial_position:
                break
        return None

    def delete(self, key):
        initial_position = self.hash(key)
        i = initial_position
        j = 0
        while self.k[i] != None:
            if self.k[i] == key:
                self.k[i] = '$'
                self.d[i] = None
                return None
            j += 1
            i = (initial_position + j) % self.m
            if i == initial_position:
                break
        return None