"""
최대로 살 수 있는 선물의 수
= 예산에서 살 수 있는 선물 중, 가격이 높은 선물 a개의 반값 할인을 최대화한다.

실제로 구현하려면,
1. 가격이 낮은 순으로 선물을 정렬한다.
2. 예산을 초과할 때까지 선물을 산다.
3. 예산을 초과한 직후의 인덱스부터 시작하여, 반값 할인된 더 높은 가격의 선물을 산다.
4. 예산을 또다시 초과하면, idx는 초과 직전 인덱스이다.
"""

n, b, a = map(int, input().split())
presents = list(map(int, input().split()))
ans = 0

# 1. 가격이 낮은 순으로 선물을 정렬한다.
presents.sort()

# 2. 예산을 초과할 때까지 선물을 산다.
idx = 0
cost = 0
while idx < n and cost + presents[idx] <= b:
  cost += presents[idx]
  idx += 1
  
# 3. 예산을 초과한 직후의 인덱스부터 시작하여, 반값 할인된 더 높은 가격의 선물을 산다.
for j in range(idx, min(idx + a, n)):
    if cost + (presents[j] // 2) <= b:
        cost += (presents[j] // 2)
        idx += 1
    else:
        break

print(idx)