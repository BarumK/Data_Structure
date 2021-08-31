class Node:
    def __init__(self, item, left_child = None, right_child = None):
        self.key = item
        self.left = left_child
        self.right = right_child

    def get_key(self):
        return self.key

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_key(self, new_item):
        self.key = new_item

    def set_left(self, new_left_child):
        self.left = new_left_child

    def set_right(self, new_right_child):
        self.right = new_right_child