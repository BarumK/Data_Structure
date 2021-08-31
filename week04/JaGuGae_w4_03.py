# 단순 연결 리스트 객체를 위한 클래스 정의
from JaGuGae_w4_02 import Node
class SList:
    def __init__(self):                     # 빈 연결 리스트를 생성, 시간복잡도: O(1)
        self.head = None

    def is_empty(self):                     # 연결 리스트가 비어있으면 True 반환, 시간복잡도: O(1)
        return self.head == None

    def add(self, item):                    # 연결 리스트의 처음 위치에 item을 저장하는 새로운 노드 삽입, 시간복잡도: O(1)
        temp = Node(item)                   # 인자로 받은 item을 저장하는 새로운 노드를 생성하여 지역변수에 할당
        temp.set_next(self.head)            # temp에 할당된 노드가 연결리스트 head가 현재 참조하고 있는 기존 노드를 참조하게 함
        self.head = temp                    # 연결 리스트 head가 temp에 할당된 노드를 참조하게 함
                                            # 연결 리스트의 마지막 위치에 item을 저장하는 새로운 노드를 삽입하는 append() 구현?
                                            # -> 입력 크기에 비례함, O(n) = n

    def size(self):                         # 연결 리스트의 사이즈(항목의 수) 반환, 시간복잡도: O(n)
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):                 # 연결 리스트에 찾고자 하는 item을 저장하고 있는 노드가 존재하면 True를 반환
        current = self.head                 # 순회를 위한 지역 변수 current에 head가 참조하고 있는 노드 할당
        found = False                       # 결과 반환을 위한 지역 변수 found를 선언하고 False를 할당
        while current != None and not found:# current가 마지막 노드를 참조하거나(and) item을 찾을 때까지 while루프 실행
            if current.get_item() == item:  # if current가 참조하고 있는 노드 N이 저장하는 item이 찾고자 하는 item이라면,
                found = True                # found에 True를 할당
            else:                           # else(찾고자 하는 item이 아니라면), current에 N의 다음 노드를 할당
                current = current.get_next()
        return found                        # 결과 반환 -> 선형구조에서 하나씩 살펴보는 순회는 시간복잡도가 O(n)임!!

    def delete(self, item):                 # 연결 리스트에서 item을 저장하고 있는 기존 노드 삭제, 시간복잡도: O(n)
        current = self.head                 # 삭제할 item을 저장하고 있는 노드 N을 찾는 순회를 위한 지역 변수 current에 head가 참조하고 있는 노드 할당
        previous = None                     # N 삭제 시 필요한 N 이전 노드를 할당하기 위한 previous 지역 변수 생성 및 초기회
        found = False                       # N 탐색 성공 여부 확인을 위한 found 지역 변수 선언 및 False 할당
        while not found:                    # N을 찾을 때까지 while루프 실행(중요: 삭제 연산 시 반드시 N이 존재한다고 가정)
            if current.get_item() == item:  # if current가 참조하고 있는 노드 N이 저장하는 item이 삭제하고자 하는 item이라면
                found = True                # found에 True를 할당
            else:                           # else(삭제하고자 하는 item이 아니라면)
                previous = current          # previous에 N을 할당하고 current에 N의 다음 노드 할당
                current = current.get_next()
        if previous == None:                # if previous에 None이 할당되어 있다면(즉, current is head)
            self.head = current.get_next()  # 현재 current가 참조하고 있는 노드 다음 노드를 head에 할당
        else:                               # else, current가 참조하고 있는 노드 다음 노드를 head에 할당
            previous.set_next(current.get_next())

    def append(self, item):                 # 시간복잡도: O(n)
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(new_node)

    def pop_first(self):                    # 연결 리스트의 처음 노드를 삭제하는 pop_first() 구현 -> 시간복잡도: O(1)
        self.head = self.head.get_next()

    def pop_last(self):                     # 연결 리스트의 마지막 노드를 삭제하는 pop_last() 구현 -> 시간복잡도: O(n)
        current = self.head
        previous = None
        while current.get_next() != None:
            previous = current
            current = current.get_next()
        previous.set_next(None)

if __name__ == "__main__":
    s = SList()
    s.add(95)
    s.add(30)
    s.add(45)
    s.add(15)
    current = s.head
    while current:
        if current.get_next() != None:
            print(current.get_item(), '->', end = ' ')
        else:
            print(current.get_item())
        current = current.get_next()