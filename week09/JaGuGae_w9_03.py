# 정렬된 단순 연결 리스트를 이용한 우선순위 큐의 구현 -> 정렬된 단순 연결 리스트와 매우 유사하다
# 여기에선 작은 값이 우선순위가 높다고 판단한다.
from node import Node
class PriorityQueue:
    def __init__(self):
        '''
        빈 우선순위 큐 생성, 시간 복잡도: O(1)
        '''
        self.head = None

    def enqueue(self, item):
        '''
        연결 리스트의 정렬된 순서에 맞는 위치에 item 삽입, 시간 복잡도: O(n)
        :param item: 삽입할 item
        :return:
        '''
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:         # 탐색: 순회 -> 시간 복잡도: O(n)
            if current.get_item() > item:
                stop =True
            else:
                previous = current
                current = current.get_next()
        temp = Node(item)                           # 찾고 난 이후에는 연결 정보만 바꾸면 되므로 시간 복잡도: O(1)
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)


    def dequeue(self):                              # 이미 정렬되어 있으므로 시간 복잡도: O(1)
        if self.head == None:                       # 정렬할 때 주의: 작은 값이 우선순위라면 오름차순으로 정렬해야.
            return None                             # -> 우선순위가 높은 것을 먼저 나오게끔 배치해야 함.
        else:
            temp = self.head                        # 없어도 되는 내용임. 없앤다면 뒤의 부분을 temp 대신 self.head로 바꾸면 됨
            dequeued_item = temp.get_item()
            self.head = self.head.get_next()
            return dequeued_item

# if 환형 연결 리스트로 우선순위 큐를 구현한다면?