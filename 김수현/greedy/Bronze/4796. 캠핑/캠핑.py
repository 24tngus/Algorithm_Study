i = 0

while True:
    L, P, V = map(int, input().split())
    if (L == 0 and P == 0 and V == 0):
        break

    i += 1
    if L < (V % P):
        result = (V // P) * L + L
    else:
        result = (V // P) * L + V % P
    print("Case %d: %d" %(i, result))