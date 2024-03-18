import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == "L":
            visited = [[0 for _ in range(M)] for _ in range(N)]
            dist = [[0 for _ in range(M)] for _ in range(N)]

            q = deque()
            q.append((i, j))
            visited[i][j] = 1
            while q:
                x, y = q.popleft()
                for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == "L" and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        dist[nx][ny] = max(dist[x][y] + 1, dist[nx][ny])
                        if ans < dist[nx][ny]:
                            ans = dist[nx][ny]
                        q.append((nx, ny))
print(ans)