"""
*환형 연결 리스트
마지막 노드와 첫 노드와 연결된 단순 연결 리스트.(참고로 이중 연결 리스트도 환형 연결 리스트로 변환될 수 있음)
마지막 노드가 첫 노드를 참조하므로 next 필드 값이 None인 노드가 존재하지 않음
환형이므로 연결 리스트 내 어떤 노드도 첫 노드가 될 수 있음
주로 head가 마지막 노드를 참조하게 함으로써 첫 노드와 마지막 노드를 상수시간만에 접근할 수 있도록 함

*환형 연결 리스트 ADT
-데이터: (1) 순차 방식으로만 접근할 수 있으며, 마지막 노드가 첫 노드를 참조하는 노드들의 집합과
        (2) 환형 연결 리스트의 마지막을 가리키는 변수인 head
-적용 가능한 연산: 강의 교안 참조
"""
from node import Node
class CList:
    def __init__(self):                                 # 빈 연결리스트를 생성, 시간복잡도: O(1)
        self.head = None # CList의 마지막 노드            # 빈 연결 리스트이므로 마지막 노드의 참조를 저장하는 함수인 head를 None로 설정

    def is_empty(self):                                 # 연결리스트가 비어있으면 True 반환, 시간복잡도: O(1)
        return self.head == None

    def add(self, item):                                # 연결 리스트의 처음 위치에 item을 저장하는 새로운 노드 삽입, 시간복잡도: O(1)
        temp = Node(item)                               # 인자로 받은 item을 저장하는 새로운 노드 Nnew를 생성하여 지역변수 temp에 할당
        if self.is_empty():                             # if 빈 연결 리스트라면,
            temp.set_next(temp)                         # temp에 할당된 Nnew가 자기 자신을 next필드로 참조하게 한 후
            self.head = temp                            # head가 Nnew를 참조하게 함
        else:                                           # 빈 연결 리스트가 아니라면
            temp.set_next(self.head.get_next())         # temp에 할당된 Nnew가 현재 head가 참조하는 노드(현재 마지막 노드) Nold의 다음 노드(현재 첫 노드)를 참조하도록 하고
            self.head.set_next(temp)                    # Nold가 next 필드로 Nnew를 참조하도록 함

    def append(self, item):                             # 연결 리스트의 마지막 위치에 item을 저장하는 새로운 노드 삽입, 시간복잡도: O(1)
        temp = Node(item)                               # 인자로 받은 item을 저장하는 새로운 노드 Nnew를 생성하여 지역변수 temp에 할당
        if self.is_empty():                             # if 빈 연결리스트라면
            temp.set_next(temp)                         # temp에 할당된 Nnew가 자기 자신을 next 필드로 참조하게 한 후
            self.head = temp                            # head가 Nnew를 참조하게 함 -> 참고: 빈 연결 리스트의 경우 add와 append는 동일
        else:                                           # 빈 연결리스트가 아니라면
            temp.set_next(self.head.get_next())         # temp에 할당된 Nnew가 현재 head를 참조하는 노드(현재 마지막 노드) Nold의 다음 노드(현재 첫 노드)를 참조하도록 하고
            self.head.set_next(temp)                    # Nold가 next 필드로 Nnew를 참조하도록 한 후
            self.head = temp                            # head가 Nnew를 참조하도록 함

    def pop_first(self):                                # 연결 리스트의 첫 노드를 삭제, 시간 복잡도: O(1)
        if self.head == None:                           # if 빈 연결 리스트라면
            print("List is empty.")
        else:                                           # 빈 연결 리스트가 아니라면
            temp = self.head.get_next()                 # 지역 변수 temp를 선언하고 현재 head가 참조하는 노드(현재 마지막 노드)의 다음 노드(현재 첫 노드) N을 할당
            if temp == temp.get_next():                 # if N이 첫 노드이자 마지막 노드라면(즉, 연결 리스트에 N만 존재한다면)
                self.head = None                        # head에 None 할당
            else:
                self.head.set_next(temp.get_next())     # 마지막 노드가 N 다음 노드를 참조하게 함

    def search(self, item):                             # 연결 리스트에 찾고자 하는 item을 저장하고 있는 노드가 존재하면 True를 반환, 시간 복잡도: O(n)
        if self.head == None:                           # if 빈 연결 리스트라면
            print("List is empty.")
        else:                                           # 빈 연결 리스트가 아니라면
            temp = self.head.get_next()                 # 무한 루프 발생을 방지하기 위한 지역 변수 temp에 head가 참조하고 있는 노드의 다음 노드(즉, 첫 노드) N을 할당
            if self.head == temp:                       # if N이 첫 노드이자 마지막 노드라면(즉, 연결 리스트에 N만 존재한다면)
                if self.head.get_item() == item:        # N이 저장하는 item이 찾고자 하는 item일 경우
                    return True                         # True를 반환 및 메소드를 종료하고
                else:                                   # 찾고자 하는 item이 아닐 경우
                    return False                        # False를 반환 및 메소드를 종료
            found = False                               # 결과 반환을 위한 지역 변수 found 선언하고 False를 할당
            current = temp                              # 순회를 위한 지역 변수 current에 temp에 할당된 노드(즉, 첫 노드) 할당
            while True:                                 # current가 한 번의 순회를 마쳤거나 item을 찾을 때까지 while 루프 실행
                if current.get_item() == item:          # if current가 참조하고 있는 노드 N이 저장하는 item이 찾고자 하는 item이라면
                    found = True                        # found에 True를 할당
                else:                                   # 찾고자 하는 item이 아니라면
                    current = current.get_next()        # current에 N의 다음 노드를 할당
                if current != temp and not found:       # while 루프 탈출 조건 검사: if current가 한 번의 리스트 순회를 마치지 않았고 item을 찾지도 못했다면
                    continue
                else:                                   # while 루프 탈출 조건 검사: current가 한 번의 리스트 순회를 마쳤거나 item을 찾았다면
                    break
            return found                                # 결과 반환