n = int(input())

for _ in range(n):
    k = int(input())
    a = 0
    b = 0
    c = 0
    d = 0
    
    if (k >= 25):
        a = k // 25
        k %= 25
    if (k >= 10):
        b = k // 10
        k %= 10
    if (k >= 5):
        c = k // 5
        k %= 5
        
    d = k // 1

    print(a, b, c, d)
    