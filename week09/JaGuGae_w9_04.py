# MIN 힙의 구현
class Binaryheap:
    def __init__(self, array = []):
        '''
        빈 힙 생성 혹은 Python 리스트 형태로 입력받은 item들의 배열을 담고 있는 Python 리스트 생성, 시간 복잡도: O(1)
        :param array: 참조할 배열
        '''
        self.items = array

    def size(self):
        '''
        힙의 사이즈 반환, 시간 복잡도: O(1)
        :return: 힙의 사이즈를 반환
        '''
        return len(self.items)

    def swap(self, i, j):
        '''
        힙의 두 노드 위치를 바꿈, 시간 복잡도: O(1)
        :param i: 위치 바꿀 힙의 번호 1
        :param j: 위치 바꿀 힙의 번호 2
        '''
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def insert(self, key):
        '''
        힙 삽입 알고리즘
        1. 완전 이진 트리의 형태를 유지하기 위해 힙의 마지막 위치에 있는 노드의 바로 다음 위치에 새로운 노드 N을 저장
        2. 마지막 노드로부터 루트 노드 방향으로 올라가면서
            (1) 부모 노드와 키 값을 비교하고
            (2) 부모 노드의 키 값이 더 크면 위치를 서로 교환하는 영상을 힙 속성이 만족될 때까지 반복 진행
            -> 단말 노드로부터 위로 올라가므로 Upheap이라고 부름
        "신입사원이 오면 일단 말단 자리에 앉힌 다음, 능력껏 위로 진급시키는 것(Upheap, Promotion)"

        시간 복잡도: O(logN) -> pf) 최악의 경우 힙의 높이 h만큼 upheap(swap)
        :param key: 삽입할 값
        '''
        self.items.append(key)                                                      # 완전 이진 트리의 형태를 유지하기 위해 리스트의 맨 끝에 저장
        self.upheap(self.size() - 1)                                                # 위로 올라가며 힙 속성을 회복하기 위해 upheap 메소드 호출

    def extract_min(self):
        '''
        힙 삭제 및 반환 알고리즘
        1. 완전 이진 트리의 형태를 유지하기 위해 루트 노드 삭제 및 반환 후 힙의 가장 마지막 위치의 노드 N을 루트 노드 위치로 이동시킴
        2. 루트로부터 시작하여 단말 노드 방향으로 내려가면서
            (1) 자식 노드들 중에서 더 작은 키 값을 가진 자식 노드(승자)와 키 값을 비교하고,
            (2) 자식 노드의 키 값이 더 작으면 위치를 서로 교환하는 연산을 힙 속성이 만족될 때까지 반복 진행
            -> 루트 노드로부터 아래로 내려가면서 수행되므로 Downheap라고 부름
        "사장자리가 비면 말단 사원을 그 자리에 앉힌 다음, 바로 아래 부하보다는 능력이 좋다고 판단될 때까지 강등시키는 것(Downheap, Demotion)"

        힙에서 루트 노드 삭제 및 (키 값) 반환
        시간 복잡도: O(logN) -> pf) 최악의 경우 힙의 높이만큼 downheap(swap)
        :return: 빈 힙이면 None, 아닐 경우 가장 높은 우선순위를 가진 값(MIN 힙이기 때문에 여기선 제일 작은 값)
        '''
        if self.size() == 0:                                                        # 힙이 empty이면
            print("Heap is empty.")                                                 # 출력 후
            return None                                                             # None 반환
        minimum = self.items[0]                                                     # 키 값 반환을 위한 지역 변수에 루트 노드의 키 값을 할당
        self.swap(0, -1)                                                            # 루트 노드 R과 힙의 가장 마지막에 있는 노드 N의 위치 교환
        del self.items[-1]                                                          # 후 삭제
        self.downheap(0)                                                            # 아래로 내려가며 힙 속성을 회복하기 위해 downheap 메소드 호출(인자는 N의 인덱스값)
        return minimum                                                              # minimum에 할당한 값을 반환

    def downheap(self, i):
        '''
        extract_min과 build_heap에서 사용함
        위에서 아래로 내려가며 힙 속성을 회복
        :param i: index 값
        '''
        while ((2 * i + 1) <= (self.size() - 1)):                                   # 리스트 items의 인덱스 i번째에 있는 노드의 왼쪽 자식이 힙에 존재할 때까지 반복문 진행
            k = 2 * i + 1                                                           # 왼쪽 자식의 인덱스 값을 지역 변수 k에 할당
            if (k < (self.size() - 1)) and (self.items[k] > self.items[k + 1]):     # 왼쪽과 오른쪽 자식의 승자를 결정한 후, k에 승자의 인덱스 값을 할당
                k += 1
            if self.items[i] < self.items[k]:                                       # 현재 노드가 자식 승자보다 작으면
                break                                                               # 루프를 중단
            self.swap(i, k)                                                         # 현재 노드와 승자인 자식 노드의 위치를 교환
            i = k                                                                   # 인덱스 값 i를 위치 교환이 끝난 현재 노드의 인덱스 값으로 변경(레벨을 증가시킴으로써 아래로 한 단계 올라가서 반복)

    def upheap(self, i):
        '''
        insert에서 사용함
        아래서 위로 올라가며 힙 속성을 회복
        :param i: 새로 들어온 item의 index값
        '''
        while (i > 0) and (self.items[(i - 1) // 2] > self.items[i]):               # 리스트 items의 인덱스 i번째에 있는 노드가 (1)루트 노드가 아니고 (2)자신의 부모 노드 키 값이 자신의 키 값보다 클 때까지만 반복문 수행
            self.swap(i, (i - 1) // 2)                                              # 현재 노드와 부모 노드의 위치를 교환
            i = (i - 1) // 2                                                        # index값 i를 위치 교환이 끝난 현재 노드의 인덱스 값으로 변경(레벨을 감소시킴으로써 위로 한 단계 올라가서 반복)

    def build_heap(self, array):
        '''
        Python 리스트를 힙으로 만들기(Heapify)
        1. 하향식(Top-down) 알고리즘
            -Python 리스트 items의 각 항목을 차례로 빈 힙에 삽입(insert 메소드 사용)
            -Python 리스트 items의 사이즈가 N이라고 했을 때, 각 항목을 하나 삽입할 때의 시간 복잡도가 O(logN)이고 N개의 항목을 삽입해야 하므로 하향식 알고리즘의 시간 복잡도는 O(NlogN)
        2. 상향식(Bottom-up) 알고리즘
            -사이즈가 N인 Python 리스트 items 내의 각 항목이 임의의 순서로 저장되어 있을 때,
                (1) 이를 이진 트리로 간주하고,
                (2) items[N // 2 - 1] 위치의 노드(즉, 비단말 노드)를 시작으로 items[0] 위치의 노드(즉, 루트 노드)까지의 각 노드를 루트 노드로 하는 서브 트리에 대해 downheap() 메소드를 사용하여 힙 속성을 충족시킴(downheap을 수행하는 순서는 오른쪽에서 왼쪽, 아래에서 위 순서)
                -> 시간 복잡도는 O(n)

        Heapify, 시간 복잡도: O(n)
        입력 받은 item들의 array를 힙으로 변환
        :param array: 힙으로 만들 array
        '''
        for i in range(len(array) // 2 - 1, -1, -1):                                # 입력 받은 array(임의의 순서로 항목이 저장되어 있는 Python 리스트)의 마지막 비단말 노드를 시작으로 루트 노드까지의 각 노드를 루트 노드로 하는 서브 트리에 대해 downheap() 메소드를 호출하여 힙 속성을 충족시킴
            self.downheap(i)

    def print_heap(self):
        '''
        힙의 노드 및 사이즈 출력
        :return:
        '''
        for i in range(0, self.size()):
            print(self.items[i], end = ' ')
        print("\nSize of Heap = ", self.size())


if __name__ == "__main__":
    array = [3, 2, 4, 5, 6, 7]
    bheap = Binaryheap(array)
    bheap.build_heap(array)
    bheap.print_heap()
    bheap.insert(1)
    bheap.insert(9)
    bheap.insert(11)
    bheap.insert(19)
    bheap.print_heap()
    print(bheap.extract_min())
    print(bheap.extract_min())
    bheap.print_heap()