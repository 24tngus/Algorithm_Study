import sys
import itertools

N, M = map(int, sys.stdin.readline().split())

board = []
for _ in range(N):
    for _ in range(N):
        board.append([int(x) for x in sys.stdin.readline().strip().split()])

homes = []
chickens = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            homes.append((i, j))
        elif board[i][j] == 2:
            chickens.append((i, j))

def calc_distance(obj1, obj2):
    o1_x, o1_y = obj1
    o2_x, o2_y = obj2
    return abs(o1_x - o2_x) + abs(o1_y - o2_y)

combinations = list(itertools.combinations(chickens, M))
new_chickens_set = [list(combo) for combo in combinations]

candidates = []
for chickens in new_chickens_set:
    sum = 0
    for home in homes:
        min_distance = 2*N
        for chicken in chickens:
            curr_distance = calc_distance(home, chicken)
            if curr_distance < min_distance:
                min_distance = curr_distance
        sum += min_distance
    candidates.append(sum)

candidiates = sorted(candidates)
print(candidiates[0])