import sys
input = sys.stdin.readline
N, K = map(int, input().split())
num = list(map(int, input().split()))
a = sum(num[:K])
answer = a
for i in range(N-K):
    a = a - num[i] + num[K+i]
    if a > answer:
        answer = a
print(answer)