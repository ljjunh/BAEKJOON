T = int(input())
for i in range(T):
    arr = list(map(str, input().split()))
    for i in arr:
        print(i[::-1], end = " ")
    print()