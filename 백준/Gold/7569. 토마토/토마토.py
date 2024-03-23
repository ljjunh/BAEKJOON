from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque()
    cnt = 0
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if graph[h][i][j] == 1:
                    q.append((h,i,j))
                    visited[h][i][j] = 1
                elif graph[h][i][j] == 0:
                    cnt += 1
    while q:
        ch, cx, cy = q.popleft()
        for dh, dx, dy in [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0)]:
            nh, nx, ny = ch + dh, cx + dx, cy + dy
            if 0 <= nh < H and 0 <= nx < N and 0 <= ny < M and not visited[nh][nx][ny] and graph[nh][nx][ny] == 0:
                q.append((nh, nx, ny))
                visited[nh][nx][ny] = visited[ch][cx][cy] + 1
                cnt -= 1
    if cnt == 0:
        return visited[ch][cx][cy] - 1
    else:
        return -1
    

M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]
ans = bfs()
print(ans)