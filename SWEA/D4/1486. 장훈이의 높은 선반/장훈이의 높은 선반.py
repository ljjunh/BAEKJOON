def recur(n, sm):
    global ans
    if sm - B >= ans:
        return
    
    if n == N:
        if sm >= B:
            ans = min(ans, sm-B)
        return
    
    recur(n+1, sm+arr[n])
    recur(n+1, sm)
T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 2147000000
    recur(0, 0)
    print(f"#{tc} {ans}")