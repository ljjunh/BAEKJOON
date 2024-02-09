N = int(input())
num = list(map(int, input().split()))
pn = 0
for i in num:
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        pn += 1
print(pn)
   
