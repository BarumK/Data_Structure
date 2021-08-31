"""
-이친 트리를 구성하는 단위: 노드
일반적인 이진 트리의 노드는 키(항목값), 왼쪽 자식 노드의 참조를 저장하기 위한 left 링크 필드, 오른쪽 자식 노드의 참조를 저장하기 위한 right 링크 필드값으로 구성됨

-순회
전위, 중위, 후위 순회는 모두 루트로부터 동일한 순서(깊이 우선)로 이진 트리의 노드를 따라 지나가는데,
특정 노드 N에 도착했을 때 N을 방문(즉, N에 대한 작업을 수행)하는지, 일단 지나치고 나중에 방문하는지에 따라 구분됨
    전위 순회는 (1) N에 도착하면 N을 먼저 방문, 그 후
              (2) N의 왼쪽 자식 노드를 루트로 하는 서브트리 T1의 모든 노드를 방문(T1을 순회함으로써), 마지막으로
              (3) N의 오른쪽 자식 노드를 루트로 하는 서브 트리 T2의 모든 노드를 방문(T2를 순회함으로써)
              -> NLR
    중위 순회는 N에 도착하면 N의 방문을 보류하고
              (1) N의 왼쪽 자식 노드를 루트로 하는 서브 트리의 모든 노드를 방문, 그 후
              (2) N을 방문, 마지막으로
              (3) N의 오른쪽 자식 노드를 루트로 하는 서브 트리의 모든 노드를 방문
              -> LNR
    후위 순회는 N에 도착하면 N의 방문을 보류하고
              (1) N 왼쪽 자식 노드를 루트로 하는 서브 트리의 모든 노드를 방문, 그 후
              (2) N의 오른쪽 자식 노드를 루트로 하는 서브 트리의 모든 노드를 방문, 마지막으로
              (3) N을 방문
              -> LRN
레벨 순회는 루트 노드가 있는 최상위 레벨부터 시작하여 각 레벨마다 좌에서 우로(너비 우선) 노드를 방문
"""
# 이진 트리의 구현
# 이진 트리 객체를 위한 클래스 정의
from btnode import Node
from clqueue import Queue

class BinaryTree:
    def __init__(self):                                 # 빈 이진 트리를 생성, 시간복잡도: O(1)
        self.root = None                                # 빈 이진 트리이므로 트리의 루트 노드의 참조를 저장하는 변수인 root를 None으로 설정

    def preorder(self, node):                           # 이진 트리를 전위 순회, 시간복잡도: O(n)
        print(str(node.get_key()), ' ', end = '')       # N을 방문(N에 대한 작업을 수행, 즉 N의 key값을 출력)
        if node.get_left():                             # N의 왼쪽 자식 노드가 None이 아니라면
            self.preorder(node.get_left())              # 그 노드를 루트로 하는 서브 트리를 전위 순회(재귀 호출)
        if node.get_right():                            # N의 오른쪽 자식 노드가 None이 아니라면
            self.preorder(node.get_right())             # 그 노드를 루트로 하는 서브 트리를 전위 순회(재귀 호출)

    def inorder(self, node):                            # 이진 트리를 중위 순회,  시간 복잡도: O(n)
        if node.get_left():                             # N의 왼쪽 자식 노드가 None이 아니라면
            self.inorder(node.get_left())               # 그 노드를 루트로 하는 서브 트리를 중위 순회(재귀 호출)
        print(str(node.get_key()), ' ', end='')         # N을 방문(N에 대한 작업을 수행, 즉 N의 key값을 출력)
        if node.get_right():                            # N의 오른쪽 자식 노드가 None이 아니라면
            self.inorder(node.get_right())              # 그 노드를 루트로 하는 서브 트리를 중위 순회(재귀 호출)

    def postorder(self, node):                          # 이진 트리를 후위 순회,  시간 복잡도: O(n)
        if node.get_left():                             # N의 왼쪽 자식 노드가 None이 아니라면
            self.postorder(node.get_left())             # 그 노드를 루트로 하는 서브 트리를 후위 순회(재귀 호출)
        if node.get_right():                            # N의 오른쪽 자식 노드가 None이 아니라면
            self.postorder(node.get_right())            # 그 노드를 루트로 하는 서브 트리를 후위 순회(재귀 호출)
        print(str(node.get_key()), ' ', end='')         # N을 방문(N에 대한 작업을 수행, 즉 N의 key값을 출력)

    def levelorder(self, root):                         # 이진 트리를 레벨 순회, 시간 복잡도: O(n)
        q = Queue()                                     # empty 큐를 생성 후
        q.enqueue(root)                                 # T의 루트 노드를 enqueue
        while not q.is_empty():                         # 큐가 empty가 될 때까지 while 루프를 실행
            node = q.dequeue()                          # 큐에서 노드 N을 dequeue 후
            print(str(node.get_key()), ' ', end='')     # N을 출력
            if node.get_left():                         # N의 왼쪽 자식 노드 Nleft 가 None이 아니라면
                q.enqueue(node.get_left())              # 큐에 Nleft를 enqueue
            if node.get_right():                        # N의 오른쪽 자식 노드 Nright가 None이 아니라면
                q.enqueue(node.get_right())             # 큐에 Nright를 enqueue


if __name__ == "__main__":
    t = BinaryTree()
    n1 = Node(100)
    n2 = Node(200)
    n3 = Node(300)
    n4 = Node(400)
    n5 = Node(500)
    n6 = Node(600)
    n7 = Node(700)
    n8 = Node(800)
    n1.set_left(n2)
    n1.set_right(n3)
    n2.set_left(n4)
    n2.set_right(n5)
    n3.set_left(n6)
    n3.set_right(n7)
    n4.set_left(n8)
    t.root = n1
    print("전위 순회:\t", end = '')
    t.preorder(t.root)
    print("\n중위 순회:\t", end='')
    t.inorder(t.root)
    print("\n후위 순회:\t", end='')
    t.postorder(t.root)
    print("\n레벨 순회:\t", end='')
    t.levelorder(t.root)