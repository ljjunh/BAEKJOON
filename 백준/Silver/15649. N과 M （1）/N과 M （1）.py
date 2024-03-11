import sys
input = sys.stdin.readline
def dfs(n):
    if n == M:
        print(*path)
        return
    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = 1
        path.append(i)
        dfs(n+1)
        path.pop()
        visited[i] = 0
N, M = map(int, input().split())
path = []
visited = [0] * (N+1)
dfs(0)