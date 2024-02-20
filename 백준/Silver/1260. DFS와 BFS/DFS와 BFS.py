import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(idx):
    visited[idx] = True
    print(idx, end = " ")
    for i in graph[idx]:
        if not visited[i]:
            dfs(i)

def bfs():
    visited[V] = True
    q = [V]
    while q:
        v = q.pop(0)
        print(v, end = " ")
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i] = sorted(graph[i])

dfs(V)
print()
visited = [False] * (N + 1)
bfs()