a, b, c = map(int, input().split())
E = S = M = year = 0
while True:
    year += 1
    E += 1
    S += 1
    M += 1
    if E > 15:
        E -= 15
    if S > 28:
        S -= 28
    if M > 19:
        M -= 19
    if E == a and S == b and M == c:
        print(year)
        break