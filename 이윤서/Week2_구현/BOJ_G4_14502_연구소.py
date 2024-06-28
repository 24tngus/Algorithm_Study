import sys
import copy
from collections import deque
from itertools import combinations

def spread(temp_map):
    # 바이러스 퍼지는 경우,
    queue = deque([(j, i) for i in range(n) for j in range(m) if lab_map[i][j] == 2])

    while queue:
        x, y = queue.popleft()
        for nx, ny in zip([x+1, x-1, x, x], [y, y, y+1, y-1]):
            if 0 <= nx < m and 0 <= ny < n and not temp_map[ny][nx]:
                temp_map[ny][nx] = 2
                queue.append((nx, ny))

    # 안전 영역 크기 계산
    global ans
    cnt = sum([i.count(0) for i in temp_map])
    ans = max(ans, cnt)


n, m = map(int, sys.stdin.readline().split())
lab_map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ans = 0

xys = [(x, y) for x in range(m) for y in range(n) if not lab_map[y][x]]
for combo in combinations(xys, 3):
    temp_map = copy.deepcopy(lab_map)
    for x, y in combo:
        temp_map[y][x] = 1
    spread(temp_map)

print(ans)