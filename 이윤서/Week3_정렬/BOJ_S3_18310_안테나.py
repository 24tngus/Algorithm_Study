"""
안테나로부터 모든 집까지의 거리의 합의 최솟값
= (모든 안테나 경우의 수) * (다른 집 탐색) = O(N^2)

수식에서 얻은 인사이트로 단순화
locs = [a, b, c, d, e], distances = [x1, x2, x3, x4]
a = 4x1 + 3x2 + 2x3 + x4
b = x1 + 3x2 + 2x3 + x4
c = x1 + 2x2 + 2x3 + x4
d = x1 + 2x2 + 3x3 + x4
e = x1 + 2x2 + 3x3 + 4x4
= 가운데 값일 때 최솟값값
"""

import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

print(arr[(N-1) // 2])