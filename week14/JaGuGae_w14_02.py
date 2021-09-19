# DFS를 위한 함수 dfs 정의
adj_list = [[2, 1], [3, 0], [3, 0], [9, 8, 2, 1], [5], [7, 6, 4], [7, 5], [6, 5], [3], [3]] # 인접 리스트로 그래프 표현
N = len(adj_list)               # 지역 변수 N 선언 후 인접 리스트의 정점 수 할당
visited = [False] * N           # 각 노드 v의 방문 여부 판단을 위한 N 사이즈를 가진 python 리스트 생성

def dfs(v):
    visited[v] = True           # v의 방문 여부를 True로 설정
    print(v, ' ', end='')       # v를 출력(방문)
    for i in adj_list[v]:       # 아직 방문하지 않은 v의 모든 이웃 정점에 대해
        if not visited[i]:
            dfs(i)              # dfs 호출

print('DFS 방문 순서:')
for i in range(N):
    if not visited[i]:
        dfs(i)