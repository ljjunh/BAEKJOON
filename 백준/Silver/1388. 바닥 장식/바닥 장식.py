import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(x, y):
    global graph, answer
    temp = graph[x][y]
    graph[x][y] = ""
    if temp == "-" and graph[x][y + 1] == "-":
        dfs(x, y + 1)
    elif temp == "|" and graph[x + 1][y] == "|":
        dfs(x + 1, y)

MAX = 50 + 10
N, M = map(int, input().split())
graph = [[""] * MAX for _ in range(MAX)]
answer = 0
for i in range(1, N + 1):
    s = input()
    for j in range(1, M + 1):
        graph[i][j] = s[j - 1]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if graph[i][j] != "":
            dfs(i, j)
            answer += 1

print(answer)