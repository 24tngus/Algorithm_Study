n, k = map(int, input().split())

data = []
result = 0

for _ in range(n):
    data.append(int(input()))

data.sort(reverse=True)

for i in data:
    if (k >= i):
        result += k // i
        k %= i

print(result)