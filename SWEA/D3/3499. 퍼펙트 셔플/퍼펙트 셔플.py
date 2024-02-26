T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(input().split())
    a = 0
    if N % 2 == 0:
        b = N // 2
        t = N // 2
    else:
        b = N // 2 + 1
        t = N // 2 + 1
    print(f"#{tc}", end = " ")
    for _ in range(t):
        if a < N:
            print(arr[a], end = " ")
            a += 1
        if b < N:
            print(arr[b], end = " ")
            b += 1
    print()
        
