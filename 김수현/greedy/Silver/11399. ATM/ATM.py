n = int(input())
arr = list(map(int, input().split()))

arr.sort()
result = 0

for i in range(len(arr)):
    result += arr[i] * (n - i)

print(result)