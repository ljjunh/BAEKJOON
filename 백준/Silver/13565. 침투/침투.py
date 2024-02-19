import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global graph, answer
    graph[x][y] = False
    if x == N:
        answer = True
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if graph[nx][ny]:
            dfs(nx, ny)

MAX = 1000 + 10
N, M = map(int, input().split())
graph = [[False] * MAX for _ in range(MAX)]
answer = False

for i in range(1, N + 1):
    s = input()
    for j in range(1, M + 1):
        graph[i][j] = (s[j - 1] == "0")

for i in range(1, M + 1):
    if graph[1][i]:
        dfs(1, i)
if answer:
    print("YES")
else:
    print("NO")