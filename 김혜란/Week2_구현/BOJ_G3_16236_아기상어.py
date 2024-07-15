'''
@ No        : 16236
@ Title     : 아기 상어
@ Subject   : 구현

@ 입력값
    - n : 공간의 크기
    - sea_grid : 공간 속 물고기, 아기상어 위치 정보
@ 출력값
    - max_time : 아기 상어가 엄마 상어에게 도움을 요청하지 않고 먹이는 먹는 최대 시간


'''

import math
n = 4
# n = int(input())

sea_grid = [[4, 3, 2, 1],
            [0, 0, 0, 0],
            [0, 0, 9, 0],
            [1, 2, 3, 4]]

# sea_grid = []
# for _ in range(n):
#     sea_grid.append(list(map(int, input().split())))

visited = [[0]*n for _ in range(n)]

import sys

input = sys.stdin.readline
from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 이동방식에 대해서는 아무렇게나 설정해도 된다.
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def bfs(time, x, y):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    eat_lst = []
    q = deque()
    q.append([time, x, y])
    visited[x][y] = 1

    while q:
        time, x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if graph[nx][ny] == 0 or graph[nx][ny] == size:
                    q.append([time + 1, nx, ny])
                    visited[nx][ny] = 1
                elif 0 < graph[nx][ny] < size:
                    eat_lst.append([time + 1, nx, ny])
                    visited[nx][ny] = 1

    # 리스트가 비었을 때
    if len(eat_lst) == 0:
        return False
    # 아니라면 sorted 정렬을 한다.
    else:
        return sorted(eat_lst)


for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x = i
            y = j


size = 2
eat = 0
time = 0

while 1:
    graph[x][y] = 0
    ans = bfs(0, x, y)
    # 탐색에서 False 를 반환하면, 더이상 먹을게 없으므로 break
    if ans == False:
        print(time)
        break
    eat += 1
    if size == eat:
        size += 1
        eat = 0

    x = ans[0][1]
    y = ans[0][2]
    time += ans[0][0]






