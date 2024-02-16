import sys
input = sys.stdin.readline

def dfs(v):
    global cnt
    visited[v] = 1
    for i in graph[v]:
        if visited[i] != 1:
            dfs(i)
            cnt += 1


n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n + 1)
cnt = 0
for i in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
dfs(1)
print(cnt)