"""
정렬된 단순 연결 리스트
-데이터: (1) 순차(sequential) 방식으로만 접근할 수 있는 정렬된 노드들의 집합과
        (2) 단순 연결 리스트의 시작을 가리키는(첫 번째 노드의 참조를 저장하는) 변수인 head
-적용 가능한 연산은 강의 자료 참고 -> 단순 연결 리스트와 동일, add와 search만 다르다.
웬만해서는 잘 사용하지 않는다고 한다.
왜 사용하지 않을까. 그 답에 대한 설명은 이진 탐색을 보면 알 수 있다.
중간을 기준으로 search space를 좁혀가야 하는데(따라서 이진 탐색은 시간복잡도가 O(logN)),
정렬된 단순 연결 리스트는 그만큼의 시간을 투자해도 원하는 항목을 찾지 못함.
"""
from node import Node
class OList:
    def __init__(self):                     # 빈 연결 리스트를 생성, 시간복잡도: O(1)
        self.head = None

    def is_empty(self):                     # 연결 리스트가 비어있으면 True 반환, 시간복잡도: O(1)
        return self.head == None

    def add(self, item):                    # 연결 리스트의 (오름차순)정렬된 순서에 맞는 위치에 item을 저장하는 새로운 노드 삽입, 시간복잡도: O(n)
        current = self.head                 # 삽입할 위치에 있는 기존 노드를 찾는 순회를 위한 변수 current에 head가 참조하고 있는 노드 할당
        previous = None                     # 새로운 노드를 삽입 시 필요한 이전 노드를 할당하기 위한 previous 지역 변수 생성 및 초기화
        stop = False                        # 삽입할 위치(즉, 기존 노드) 탐색 여부 확인을 위한 stop 지역 변수 선언 및 False 할당
        while current != None and not stop: # 삽입할 위치를 찾을 때까지 while 루프 실행
            if current.get_item() > item:   # if current가 참조하고 있는 노드 N이 저장하는 item의 값이 삽입하고자 하는 item의 값보다 크면
                stop = True                 # stop에 True 할당
            else:                           # else, previous에 N을 할당하고 current에 N의 다음 노드를 할당
                previous = current
                current = current.get_next()
        temp = Node(item)                   # 삽입하고자 하는 item을 저장하는 새로운 노드 생성 후 지역 변수 temp에 할당
        if previous == None:                # if previous에 None이 할당되어 있다면, current가 참조하고 있는 노드는 head가 참조하고 있는 노드이므로
            temp.set_next(self.head)        # temp에 할당된 노드가 기존 노드를 참조하게 하고
            self.head = temp                # head는 새로운 노드를 참조하게 함(순서 중요!!)
        else:                               # 연결 리스트의 (오름차순) 정렬된 순서에 맞는 위치에 item을 저장하는 새로운 노드 삽입
            temp.set_next(current)          # temp에 할당된 새 노드가 기존 노드를 참조하게 하고
            previous.set_next(temp)         # previous에 할당된 노드는 새 노드를 참조하게 함

    def size(self):                         # 연결 리스트의 사이즈(항목의 수) 반환, 시간복잡도: O(n)
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):                 # 연결 리스트에 찾고자 하는 item을 저장하고 있는 노드가 존재하면 True를 반환, 시간복잡도: O(n)
        current = self.head                 # 단순 연결 리스트 search의 동일부분 라인과 같음
        found = False
        stop = False                        # 찾고자 하는 item을 저장하고 있는 노드가 존재하지 않을 때 순회를 종료하기 위해 사용할 지역 변수 stop를 선언하고 False를 할당
        while current != None and not stop and not found:
                                            # (1) current가 마지막 노드를 참조하거나
                                            # (2) 찾고자 하는 item이 존재하지 않는다는 사실을 알게 되거나
                                            # (3) item을 찾을 때까지 while루프 실행
            if current.get_item() == item:  # if current가 참조하고 있는 노드N이 저장하는 item이 찾고자 하는 item이라면
                found =True                 # found에 True를 할당
            else:                           # 찾고자 하는 item이 아니라면
                if current.get_item() > item:# N이 저장하는 item이 찾고자 하는 item보다 크다면
                    stop = True             # stop에 True를 할당하여 while루프를 탈출하고
                else:                       # 아니라면 current에 N의 다음 노드 할당
                    current = current.get_next()
        return found                        # 결과 반환
                                            # 처음부터 중간값에 접근할 수 없기 떄문에 순회를 해야 한다

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