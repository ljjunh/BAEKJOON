from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited = [[0] * M for _ in range(N)]
    visited[x][y] = 1
    q = deque()
    q.append((x, y))
    while q:
        tx, ty = q.popleft()
        for k in range(4):
            nx, ny = tx + dx[k], ty + dy[k]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    now[nx][ny] += 1
                else:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                
                
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = 0
while True:
    now = [[0] * M for _ in range(N)]
    bfs(0, 0)
    ans += 1
    for i in range(N):
        for j in range(M):
            if now[i][j] >= 2:
                graph[i][j] = 0
    cheese = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                cheese += 1
    if cheese == 0:
        print(ans)
        break
    
  