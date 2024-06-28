import sys
blocks = []
H, W = map(int, sys.stdin.readline().split())
blocks = list(map(int, sys.stdin.readline().split()))

ans = 0
for i in range(1, W-1):
    left = max(blocks[ :i])
    right = max(blocks[i+1: ])
    wall = min(left, right)
    if blocks[i] < wall:
        ans += wall - blocks[i]
print(ans)