n = int(input())

data = []
result = 0

for i in range(n):
    a, b = map(int, input().split())
    data.append([a,b])

data.sort(key=lambda x: (x[1], x[0]))

a = 0
b = 0
for x, y in data:
    if (x >= b):
        result += 1
        a = x
        b = y

print(result)
