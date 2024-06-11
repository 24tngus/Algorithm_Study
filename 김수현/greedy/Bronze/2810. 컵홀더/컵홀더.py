n = int(input())
str = input()

cnt = 0
result = 0

for i in str:
    if (i == 'L'):
        cnt += 1
if (cnt >= 4):
    result = n - (cnt // 2) + 1
else:
    result = n
print(result)