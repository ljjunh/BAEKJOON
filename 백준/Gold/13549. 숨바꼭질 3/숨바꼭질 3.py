from collections import deque

def bfs(x):
    global K
    limit = 100001
    visited = [0] * limit
    cnt = [0] * limit
    visited[x] = 1
    q = deque()
    q.append(x)
    while q:
        v = q.popleft()
        if v == K:
            return cnt[v]
        if 0<= v*2 < limit and not visited[v*2]:
            q.appendleft(v*2)
            cnt[v*2] = cnt[v]
            visited[v*2] = 1
        if 0 <= v-1 < limit and not visited[v-1]:
            q.append(v-1)
            cnt[v-1] = cnt[v]+1
            visited[v-1] = 1
        if 0 <= v+1 < limit and not visited[v+1]:
            q.append(v+1)
            q.append(v+1)
            cnt[v+1] = cnt[v]+1
            visited[v+1] = 1
N, K = map(int, input().split())
print(bfs(N))

