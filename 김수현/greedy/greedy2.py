n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    minn = 10001

    for j in data:
        minn = min(minn, j)

    result = max(result, minn)

print(result)