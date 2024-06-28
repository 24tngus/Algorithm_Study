import sys

ans = 0
cows = [-1]*11
n = int(input())

for _ in range(n):
    idx, val = map(int, sys.stdin.readline().split())
    if cows[idx] == -1:
        cows[idx] = val
    elif cows[idx] != val:
        cows[idx] = val
        ans += 1
print(ans)