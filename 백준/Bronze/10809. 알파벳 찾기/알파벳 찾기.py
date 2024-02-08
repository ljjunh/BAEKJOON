res = [-1] * 26
for idx, v in enumerate(input()):
    if res[ord(v)-97] == -1:
        res[ord(v)-97] = idx
print(*res)