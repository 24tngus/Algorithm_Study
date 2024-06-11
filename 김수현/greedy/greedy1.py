n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
fir = arr[n-1]
sec = arr[n-2]


# 방법1
result = 0

while (1):
    for i in range(k):
        if m == 0:
            break
        result += fir
        m -= 1
    if m == 0:
        break
    result += sec
    m -= 1

# 방법2

count = int((m / (k + 1))) * k
count += m % (k + 1)

result = 0
result += count * fir
result += (m - count) * sec

print(result)