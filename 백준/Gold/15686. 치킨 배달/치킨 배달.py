import sys
input = sys.stdin.readline

def cal(lst):
    sm = 0
    for hx, hy in home:
        tmp = 2147000000
        for cx, cy in lst:
            tmp = min(tmp, abs(hx-cx) + abs(hy-cy))
        sm += tmp
    return sm
            
def recur(n, lst):
    global ans
    if n == len(chicken):
        if len(lst) == M:
            ans = min(ans, cal(lst))
        return
    recur(n+1, lst + [chicken[n]])
    recur(n+1, lst)
    
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
chicken = []
home = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            home.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))
ans = 2147000000
recur(0, [])
print(ans)
