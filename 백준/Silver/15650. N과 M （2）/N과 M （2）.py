import sys
input = sys.stdin.readline
def dfs(n, s, lst):
    if n == M:
        print(*lst)
        return
    for i in range(s, N+1):
        dfs(n+1, i+1, lst+[i])
N, M = map(int, input().split())
dfs(0, 1, [])