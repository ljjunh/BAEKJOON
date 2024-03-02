N = int(input())
arr = [[0] * 1003 for _ in range(1003)]
for i in range(1, N + 1):
    x, y, w, h = map(int, input().split())
    for j in range(x, x+w):
        for k in range(y, y+h):
            arr[j][k] = i
res = [0] * (N + 1)
for i in range(1003):
    for j in range(1003):
        if arr[i][j] != 0:
            res[arr[i][j]] += 1
for i in range(1, N + 1):
    print(res[i])
