# 이진 탐색 트리 객체를 위한 클래스 정의 25:53
from btnode import Node
class BST:
    def __init__(self):
        """
        빈 이진 탐색 트리를 생성
        시간 복잡도: O(1)
        """
        self.root = None                                    # 빈 이진 탐색 트리이므로 트리의 루트 노드의 참조를 저장하는 변수인 root를 None로 설정

    def search(self, k):
        """
        이진 탐색 트리 탐색 연산
        1. 검색 키 값이 k라면, 루트 노드의 키 값과 k를 비교하는 것으로 탐색을 시작
        2. (i) k가 루트 노드의 키 값보다 작으면, 루트 노드의 왼쪽 서브 트리에서 k와 같은 키 값을 가지는 노드를 생성
           (ii) 크면 루트 노드의 오른쪽 서브 트리에서 k와 같은 키 값을 가지는 노드를 찾으며,
           (iii) 같으면 탐색 성공
        3. 왼쪽, 오른쪽 서브 트리에서의 탐색은 재귀적으로 반복

        검색 키 값인 k와 같은 키 값을 가지는 노드가 존재하면 True 반환
        시간 복잡도: O(h), 여기서 h는 트리의 높이
            -> 일반적으로 O(logN), 편향된 이진 탐색 트리의 경우 O(n)
        :param k: 검색 키 값
        :return: 탐색 결과
        """
        return self._search(self.root, k)                   # 함수 호출 결과를 반환, 시작은 루트 노드로부터

    def _search(self, n, k):
        """
        :param n: 노드
        :param k: 키 값
        :return: 탐색 결과
        """
        if n == None or n.get_key() == k:                   # if 루트 노드가 None이면 False를 반환하고
            return n != None                                # 루트 노드의 키 값이 k와 같다면 True를 반환
        elif n.get_key() > k:                               # elif 루트 노드의 키 값이 k보다 크다면
            return self._search(n.get_left(), k)            # 왼쪽 자식을 루트 노드로 하는 서브 트리에서 탐색 수행
        else:                                               # else (루트 노드의 키 값이 k보다 작다면)
            return self._search(n.get_right(), k)           # 오른쪽 자식을 루트 노드로 하는 서브 트리에서 탐색 수행

    def insert(self, key):
        """
        이진 탐색 트리 삽입 연산
        삽입 연산은 탐색 연산과 거의 동일
        1. 탐색 연산을 수행
        2. 탐색 중 루트 노드 N == None인 서브 트리를 만나면 새 노드를 생성하여 N의 부모 노드와 연결(삽입)
            단, 이미 동일한 키 값을 가지는 노드가 존재하는 경우 삽입하지 않음.
            왜? -> 이진 탐색 트리에서 모든 노드의 키는 서로 다른 유일한 값을 가지므로

        키 값 key를 가지는 노드 삽입
        시간 복잡도: O(h), 여기서 h는 트리의 높이
            -> 일반적으로 O(logN), 편향된 이진 탐색 트리의 경우 O(n)
        :param key: 삽입하고자 하는 키 값
        :return:
        """
        self.root = self._insert(self.root, key)            # protected 멤버함수 _insert() 호출, 인자는 루트노드와 키 값 key

    def _insert(self, n, key):
        """
        :param n: 노드
        :param key: 키 값
        :return:
        """
        if n == None:                                       # if 루트 노드 n이 None이면 (조건 1)
            return Node(key)                                # key를 키 값으로 가지는 새로운 Nnew를 생성 후 반환
        if n.get_key() > key:                               # if 루트 노드 n의 키 값이 key보다 크다면 (조건 2)
            n.set_left(self._insert(n.get_left(), key))     # 왼쪽 자식을 루트 노드로 하는 서브 트리에서 삽입 수행
        elif n.get_key() < key:                             # elif 루트 노드의 n의 키 값이 key보다 작다면 (조건 3)
            n.set_right(self._insert(n.get_right(), key))   # 오른쪽 자식을 루트 노드로 하는 서브 트리에서 작업 수행
        return n                                            # 부모 노드와 연결하기 위해 (현재 서브 트리의) 루트 노드 n 반환

    def find_min(self):
        """
        이진 탐색 트리에서 키 값이 최소인 노드 탐색 및 키 값이 최소인 노드 삭제
        1. 이진 탐색 트리에서 키 값이 최소인 노드 탐색
            루트 노드로부터 왼쪽 자식 노드를 루트로 하는 서브 트리를 재귀적으로 반복 탐색하여 왼쪽 자식 노드가 존재하지 않는 노드
            Nmin을 반환 (즉, 루트 노드로부터 왼쪽 자식 노드를 따라 내려가며, None을 만났을 때 None의 부모 노드를 반환)
        2. 이진 탐색 트리에서 키 값이 최소인 노드 삭제
            Nmin을 탐색 후, Nmin의 부모 노드 Np와 Nmin의 자식 노드 Nc를 연결시킴(Note: Nmin의 왼쪽 자식 노드는 존재할 수 없음)

        키 값이 최소인 노드 검색
        시간 복잡도: O(h), 여기서 h는 트리의 높이
            -> 일반적으로 O(logN), 편향된 이진 탐색 트리의 경우 O(n)
        :return:
        """
        if self.root == None:                               # if 루트 노드가 None이면 (즉 빈 이진 탐색 트리라면)
            return None                                     # None 반환
        return self._find_min(self.root)                    # protected 멤버함수 호출 (인자는 루트노드)

    def _find_min(self, n):
        """
        :param n: 노드
        :return:
        """
        if n.get_left() == None:                            # if 루트 노드 n의 왼쪽 자식 노드가 None이라면
            return n                                        # n의 키 값이 최소이므로 n을 반환
        return self._find_min(n.get_left())                 # 루트 노드 n의 왼쪽 자식 노드가 None이 아니라면, 왼쪽 자식을 루트 노드로 하는 서브 트리에서 탐색 수행

    def delete_min(self):
        """
        키 값이 최소인 노드 삭제
        시간 복잡도: O(h), 여기서 h는 트리의 높이
            -> 일반적으로 O(logN), 편향된 이진 탐색 트리의 경우 O(n)
        :return:
        """
        if self.root == None:                               # if 루트 노드가 None이면 (즉 빈 이진 탐색 트리라면)
            print("Tree is empty")                          # 비었다는 메시지 출력
        self.root = self._delete_min(self.root)             # protected 멤버함수 호출 (인자는 루트노드)

    def _delete_min(self, n):
        """
        :param n: 노드
        :return:
        """
        if n.get_left() == None:                            # if 루트 노드 n의 왼쪽 자식 노드가 None이라면
            return n.get_right()                            # n의 오른쪽 자식 노드를 반환 (None: 오른쪽 자식 노드가 없다면 None를 반환함)
        n.set_left(self._delete_min(n.get_left()))          # 루트 노드 n의 왼쪽 자식 노드가 None이 아니라면, 왼쪽 자식을 루트 노드로 하는 서브 트리에서 최솟값 삭제 연산 수행
        return n                                            # 부모 노드와 연결하기 위해 (현재 서브 트리의) 루트 노드 n 반환

    def delete(self, key):
        """
        이진 탐색 트리에서 특정 키 값 key를 가지는 노드 삭제
        1. 삭제하고자 하는 노드 N을 찾고 삭제 후, 이진 탐색 트리의 조건을 만족하도록 N의 부모 노드 Np와 N의 자식 노드(들) Nc를 연결
        2. N이 자식 노드가 없는 경우 (case 0), 자식 노드가 하나인 경우(case 1), 자식 노드가 둘인 경우 (case 2)로 나누어 삭제 연산을 수행
            case 0: Np의 (left 혹은 right) 링크 필드에서 N의 참조를 None으로 설정
            case 1: Np와 Nc를 연결
            case 2: Np는 하나인데 Nc는 둘이므로 case1의 방법을 사용할 수 없음. 따라서 N의 위치에 트리를 중위 순회하면서
                    N을 방문하기 직전 노드(중위 선행자: N의 왼쪽 서브 트리에서 가장 큰 키 값을 가지는 자손 노드) 또는
                    직후에 방문되는 노드(중위 후속자: N의 오른쪽 서브 트리에서 가장 작은 키 값을 가지는 자손 노드)로 대체

        키 값 key를 가지는 노드 삭제
        시간 복잡도: O(h), 여기서 h는 트리의 높이
            -> 일반적으로 O(logN), 편향된 이진 탐색 트리의 경우 O(n)
        :param key:
        :return:
        """
        self.root = self._delete(self.root, key)            # protected 멤버함수 호출 (인자는 루트노드와 키 값 key)

    def _delete(self, n, key):
        """
        :param n: 노드
        :param key: 삭제하고자 하는 키 값
        :return:
        """
        if n == None:                                           # if 루트 노드 n이 None이면
            return None                                         # None 반환 (삭제할 노드가 없는 경우)
        if n.get_key() > key:                                   # if 루트 노드 n의 키 값이 key보다 크면
            n.set_left(self._delete(n.get_left(), key))         # n의 왼쪽 자식 노드를 루트로 하는 서브 트리에서 삭제할 노드 탐색
        elif n.get_key() < key:                                 # elif 루트 노드 n의 키 값이 key보다 작으면
            n.set_right(self._delete(n.get_right(), key))       # n의 오른쪽 자식 노드를 루트로 하는 서브 트리에서 삭제할 노드 탐색
        else:                                                   # else (키 값 key를 가지는 노드를 찾았다면)
            if n.get_left() == None and n.get_right() == None:  # case 0인 경우
                return None                                     # None을 반환
            if n.get_left() == None or n.get_right() == None:   # case 1인 경우
                if n.get_left() == None:                        # 왼쪽 자식 노드가 None이면
                    return n.get_right()                        # 오른쪽 자식 노드를 n의 부모와 연결하고
                else:                                           # 오른쪽 자식 노드가 None이면
                    return n.get_left()                         # 왼쪽 자식 노드를 n의 부모와 연결
            target = n                                          # case 2인 경우 지역 변수를 생성하여 n을 참조하게 하고
            n = self._find_min(target.get_right())              # n의 중위 후속자를 찾아서 n으로 대체시키고
            n.set_right(self._delete_min(target.get_right()))   # target 변수가 참조하고 있는 nold의 오른쪽 자식 cright를 루트로 하는 서브 트리에서 중위 후속자를 삭제 후 cright를 nnew의 오른쪽 자식으로 연결시키고
            n.set_left(target.get_left())                       # nold의 왼쪽 자식 cleft를 nnew의 왼쪽 자식으로 연결시킴
        return n                                                # 부모 노드와 연결하기 위해 (현재 서브 트리의) 루트 노드 n 반환