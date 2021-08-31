class LinearProbing:
    def __init__(self, size):
        """
        빈 해시 테이블 생성(생성자)
        :param size: 해시 테이블의 사이즈
        """
        self.m = size                                   # 해시 테이블 사이즈(즉, 나눗셈 해시 함수의 제수) size를 입력 받아 멤버 변수 m에 할당
        self.k = [None for _ in range(size + 1)]        # 해시 테이블의 키 값을 저장하는 m사이즈의 키 리스트 k를 초기화
        self.d = [None for _ in range(size + 1)]        # 해시 테이블의 데이터 값을 저장하는 m사이즈의 데이터 리스트 d를 초기화

    def hash(self, key):
        """
        해시 함수 (키 값을 해시 값으로 변환)
        :param key: 키 값
        :return: 해시 값
        """
        return key % self.m                             # 나눗셈 해시 함수로 데이터의 키 값을 m으로 나눈 뒤, 그 나머지를 해시 값으로 반환

    def insert(self, key, data):
        """
        삽입 연산
        :param key: 키 값
        :param data: 데이터
        :return:
        """
        initial_position = self.hash(key)               # hash(key)를 이용하여 삽입을 위한 초기 슬롯 위치(인덱스)를 지역변수 initial_position에 할당
        i = initial_position                            # 선형 조사를 위한 지역 변수 i, j 선언 및 각각 초기 슬롯 위치와 0을 할당
        j = 0                                           # 여기서 i는 비어있는지 아닌지를 확인할 슬롯 위치 할당을 위해 사용하고, j는 순회를 위해 사용
        while True:                                     # 탈출 조건을 만족할 때까지 while 루프 실행
            if self.k[i] == None or self.k[i] == '$':   # 만약 빈 슬롯을 발견했다면(None는 한번도 사용하지 않은 값, $는 사용되었다가 데이터가 삭제되어 비어있는 슬롯)
                self.k[i] = key                         # 해당 슬롯에 키 값과
                self.d[i] = data                        # 데이터 값을 저장하고
                return None                             # while 루프 탈출
            if self.k[i] == key:                        # 만약 삽입하고자 하는 데이터가 이미 해시 테이블에 존재한다면 (특정 데이터의 키 값은 해당 데이터를 유일하게 식별할 수 있는 값으로 이 줄의 조건을 만족한다면 그 데이터가 이미 해시 테이블 ht의 슬롯 ht[i]에 존재한다는 의미)
                self.d[i] = data                        # 데이터 값만 갱신 후
                return None                             # while 루프 탈출
            j += 1                                      # 다음 while 루프에서 방문할 슬롯의 위치 결정
            i = (initial_position + j) % self.m         # (선형 조사이므로 현재 슬롯 다음 위치에 존재하는 슬롯)
            if i == initial_position:                   # 만약 초기 슬롯 위치로 되돌아 왔다면
                break                                   # while 루프 탈출 (빈 슬롯이 없다는 의미이므로 삽입 실패)

    def search(self, key):
        """
        검색 연산
        :param key: 키 값
        :return: 있으면 데이터 값, 없으면 None
        """
        initial_position = self.hash(key)               # hash(key)를 이용하여 삽입을 위한 초기 슬롯 위치(인덱스)를 지역변수 initial_position에 할당하고,
        i = initial_position                            # 선형 조사를 위한 지역 변수 i, j 선언
        j = 0                                           # 및 각각 초기 슬롯 위치와 0을 할당
        while self.k[i] != None:                        # 한 번도 사용하지 않은 빈 슬롯을 만날 때까지 while 루프 실행
            if self.k[i] == key:                        # 만약 해시 테이블 ht[i]의 k[i]값이 찾고자 하는 데이터의 키 값과 같다면
                return self.d[i]                        # 해당 데이터의 값을 반환 후 while 루프 탈출 (검색 성공)
            j += 1                                      # 다음 while 루프에서 방문할 슬롯의 위치 결정
            i = (initial_position + j) % self.m         # (선형 조사이므로 현재 슬롯 다음 위치에 존재하는 슬롯)
            if i == initial_position:                   # 만약 초기 슬롯 위치로 되돌아왔다면
                break                                   # while 루프 탈출 후
        return None                                     # 종료 (검색 실패)

    def delete(self, key):
        """
        삭제 연산
        :param key: 키 값
        :return: None
        """
        initial_position = self.hash(key)               # hash(key)를 이용하여 삭제를 위한 초기 슬롯 위치(인덱스)를 지역변수 initial_position에 할당하고,
        i = initial_position                            # 선형 조사를 위한 지역 변수 i, j 선언 및
        j = 0                                           # 각각 초기 슬롯 위치와 0을 할당
        while self.k[i] != None:                        # 한 번도 사용하지 않은 빈 슬롯을 만날 때까지 while 루프 실행
            if self.k[i] == key:                        # 만약 해시 테이블 ht[i]의 k[i]값이 찾고자 하는 데이터의 키 값과 같다면 삭제할 데이터를 찾았으므로
                self.k[i] = '$'                         # ht[i]는 사용되었다가 데이터가 삭제된 빈 슬롯임을 표시하기 위해 k[i]에 '$' 할당
                self.d[i] = None                        # ht[i]의 d[i]에 None를 할당하고
                return None                             # while 루프 탈출 (삭제 성공)
            j += 1                                      # 다음 while 루프에서 방문할 슬롯의 위치 결정
            i = (initial_position + j) % self.m         # (선형 조사이므로 현재 슬롯 다음 위치에 존재하는 슬롯)
            if i == initial_position:                   # 만약 초기 슬롯 위치로 되돌아왔다면
                break                                   # while 루프 탈출 후
        return None                                     # 종료 (삭제 실패)