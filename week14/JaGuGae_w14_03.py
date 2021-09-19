from clqueue import Queue
adj_list = [[2, 1], [3, 0], [3, 0], [9, 8, 2, 1], [5], [7, 6, 4], [7, 5], [6, 5], [3], [3]]     # 인접 리스트로 그래프 표현
N = len(adj_list)                       # 지역 변수 N 선언 후 인접 리스트의 정점 수 할당
visited = [False] * N                   # 각 노드 v의 방문 여부 판단을 위한 N 사이즈를 가진 python 리스트 생성

def bfs(v):
    queue = Queue()                     # empty 큐 queue 생성
    visited[v] = True                   # queue에 enqueue하기 전에 미리 v의 방문 여부를 True로 설정
    queue.enqueue(v)                    # v를 queue에 enqueue
    while not queue.is_empty():         # queue가 empty일 때까지 while-루프 수행
        v = queue.dequeue()             # 가장 먼저 enqueue된 정점 v를 dequeue 후 출력(방문)
        print(v, ' ', end='')
        for i in adj_list[v]:           # 아직 방문하지 않은 v의 모든 이웃 정점에 대해
            if not visited[i]:
                visited[i] = True       # 방문 여부를 미리 True로 설정 후
                queue.enqueue(i)        # queue에 enqueue

print('BFS 방문 순서:')
for i in range(N):
    if not visited[i]:
        bfs(i)