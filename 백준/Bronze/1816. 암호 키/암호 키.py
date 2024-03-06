T = int(input())
for _ in range(T):
    n = int(input())
    for i in range(2, 1000001):
        if n % i == 0:
            print("NO")
            break
    else:
        print("YES")