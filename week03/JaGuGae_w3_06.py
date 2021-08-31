from JaGuGae_w3_04 import Student

# 사용자 정의 데이터 타입인 Stack을 사용하여 삽입되는 순서대로 나열
class Stack:
    def __init__(self):
        self.items = []
    '''def is_empty(self):
        return self.items == []'''
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items) - 1]
    '''def size(self):
        return len(self.items)'''

assistant = Stack()
num_assistant = int(input("Input the number of assistant: "))

for i in range(num_assistant):
    if i == 0:
        new_name = input("Please enter a name: ")
        new_id = int(input("Please enter an id: "))
    else:
        new_name = input("Please enter another name: ")
        new_id = int(input("Please enter another id: "))
    assistant.push(Student(new_name, new_id))

print("{}, {}".format(assistant.peek().name, assistant.peek().id))
assistant.pop()
print("{}, {}".format(assistant.peek().name, assistant.peek().id))
assistant.pop()
print("{}, {}".format(assistant.peek().name, assistant.peek().id))