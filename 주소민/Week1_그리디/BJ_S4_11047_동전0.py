# 사용자 입력 값
n, k = map(int, input().split())

# P_NOTE: [입력] 사용자의 여러 입력값을 반복문으로 받을 수 있음.
coins = list()
for _ in range(n):
    x = int(input())
    if x <= k:
        coins.append(x)

# P_NOTE: [정렬] 내림차순 정렬
coins.sort(reverse=True)

answer = 0
for coin in coins:
    answer += k // coin
    k %= coin
print(answer)
