class Node:
    def __init__(self, key, data, link):
        """
        단순 연결 리스트를 구성하는 단위 노드 생성
        :param key: 키 필드
        :param data: 데이터 필드
        :param link: 링크 필드
        """
        self.key = key                                      # 데이터의 키 값을 저장하는 키 필드
        self.data = data                                    # 데이터 값을 저장하기 위한 데이터 필드
        self.next = link                                    # 다음 순서 노드의 참조를 저장하기 위한 링크 필드

class Chaining:
    def __init__(self, size):
        """
        빈 해시 테이블 생성
        :param size: 해시 테이블 사이즈
        """
        self.m = size                                       # 해시 테이블 사이즈, 즉 나눗셈 해시 함수의 제수 size를 입력받아 멤버 변수 m에 할당
        self.table = [None for x in range(size + 1)]        # m 사이즈의 해시 테이블을 초기화 (Note: Python 리스트로 구현된 해시 테이블 ht의 각 항목 table[i]는 해시 값 i를 가지는 데이터들을 저장하는 노드들의 연결리스트의 첫 노드를 가리키는 혹은 참조하는 head 역할을 함)

    def hash(self, key):
        """
        해시 함수 (키 값을 해시 값으로 변환)
        :param key: 키 값
        :return: 해시 값
        """
        return key % self.m                                 # 나눗셈 해시 함수로 데이터의 키 값을 m으로 나눈 뒤, 그 나머지를 해시 값으로 변환

    def insert(self, key, data):
        """
        삽입 연산
        :param key: 키 값
        :param data: 데이터 값
        :return:
        """
        i = self.hash(key)                                  # hash(key)를 이용하여 삽입을 위한 슬롯 위치(인덱스)를 지역변수 i에 할당
        p = self.table[i]                                   # 연결리스트의 선형 조사 시 각 노드를 가리키기 위한 지역변수 p 선언 후 연결리스트의 첫 노드를 가리키도록 초기화
        while p != None:                                    # 탈출 조건을 만족할 때까지 while 루프 실행 (탈출 조건은 특정 슬롯의 연결리스트의 마지막 노드까지 선형 조사)
            if key == p.key:                                # 만약 삽입하고자 하는 데이터가 이미해시 테이블에 존재한다면
                p.data = data                               # 데이터 값 p.data만 갱신 후
                return None                                 # while 루프 탈출 및 삽입 연산 종료
            p = p.next                                      # p에 N 다음 노드 할당
        self.table[i] = Node(key, data, self.table[i])      # 만약 삽입하고자 하는 데이터가 해시 테이블에 존재하지 않는다면 해당 데이터를 저장하기 위한 노드 생성 후 연결리스트 앞에 삽입
                                                            # 왜 맨 앞에 삽입할까? -> 그래야지 상수 시간만에 삽입할 수 있기 때문임.
        #16:34
    def search(self, key):
        """
        검색 연산
        :param key: 키 값
        :return: 있으면 데이터 값, 없으면 None
        """
        i = self.hash(key)                                  # hash(key)를 이용하여 삽입을 위한 슬롯 위치(인덱스)를 지역 변수 i에 할당하고
        p = self.table[i]                                   # 연결리스트의 선형 탐사 시 각 노드를 가리키기 위한 지역 변수 p 선언 후 연결리스트의 첫 노드를 가리키도록 초기화
        while p != None:                                    # 탈출 조건을 만족할 때까지 while 루프 실행
            if key == p.key:                                # 만약 현재 노드 N에 저장된 데이터 키 값 p.key가 찾고자 하는 데이터의 키 값 key와 같다면 검색 성공이므로
                return p.data                               # 해당 데이터의 데이터 값 p.data를 반환 후 while 루프 탈출
            p = p.next                                      # p에 N 다음 노드를 할당
        return None                                         # while 루프의 탈출 조건을 만족하여 탈출하였으므로, 즉 연결리스트의 모든 노드를 확인하였지만 찾고자 하는 데이터를 찾지 못하였으므로, 검색 실패

    def delete(self, key):
        """
        삭제 연산
        :param key: 키 값
        :return: None
        """
        i = self.hash(key)                                  # hash(key)를 이용하여 삽입을 위한 슬롯 위치를 지역 변수 i에 할당하고
        p = self.table[i]                                   # 연결리스트의 선형 탐사 시 각 노드를 가리키기 위한 지역 변수 p 선언 후 연결리스트의 첫 노드를 가리키도록 초기화
        previous = None                                     # 연결리스트의 노드 N의 삭제 시 반드시 필요한 N 이전 노드를 할당하기 위한 previous 지역 변수 생성 및 초기화
        while p != None:                                    # 탈출 조건을 만족할 때까지 while 루프 실행
            if key == p.key:                                # 만약 현재 노드 N에 저장된 데이터 키 값 p.key가 삭제하고자 하는 데이터의 키 값 key와 같다면
                if previous == None:                        # 만약 N이 연결리스트의 맨 첫번째 노드라면
                    self.table[i] = p.next                  # head 역할을 하는 table[i]가 N 다음 노드를 가리키게 함으로써 N 삭제
                else:                                       # 만약 N이 연결리스트의 맨 첫번째 노드가 아니라면
                    previous.next = p.next                  # N 이전 노드가 N 다음 노드를 가리키게 함으로써 N 삭제
                return None                                 # 삭제를 완료하였으므로 while문 탈출 및 삭제 연산 종료
            previous = p                                    # p가 가리키는 현재 노드 N을 prexious가 가리키게 하고
            p = p.next                                      # p는 N 다음 노드를 가리키게 함


if __name__ == "__main__":
    ht = Chaining(13)
    ht.insert(45, 'A')
    ht.insert(27, 'B')
    ht.insert(88, 'C')
    ht.insert(9, 'D')
    ht.insert(71, 'E')
    ht.insert(60, 'F')
    ht.insert(46, 'G')
    ht.insert(38, 'H')
    ht.insert(24, 'I')