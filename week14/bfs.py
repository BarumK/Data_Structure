from clqueue import Queue
adj_list = [[2, 1], [3, 0], [3, 0], [9, 8, 2, 1], [5], [7, 6, 4], [7, 5], [6, 5], [3], [3]]
N = len(adj_list)
visited = [False] * N

def bfs(v):
    queue = Queue()
    visited[v] = True
    queue.enqueue(v)
    while not queue.is_empty():
        v = queue.dequeue()
        print(v, ' ', end='')
        for i in adj_list[v]:
            if not visited[i]:
                visited[i] = True
                queue.enqueue(i)

print('BFS 방문 순서:')
for i in range(N):
    if not visited[i]:
        bfs(i)