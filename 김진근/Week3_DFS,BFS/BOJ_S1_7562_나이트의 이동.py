import sys
from collections import deque

input = sys.stdin.readline  # 빠른 입력
print = sys.stdout.write  # 빠른 출력, 출력은 반드시 문자열로

# 나이트가 움직일수 있는 좌표 (x,y) 오른쪽 위부터!
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


def bfs(start_x, start_y, target_x, target_y):
    queue = deque()
    queue.append((start_x, start_y))
    graph[start_x][start_y] = 1  # 현재 좌표 방문처리

    while queue:  # 목표를 갈때까지 무한 반복
        now_x, now_y = queue.popleft()
        if now_x == target_x and now_y == target_y:  # 갈려고 하는 곳
            return graph[now_x][now_y]-1

        for i in range(8):
            next_x, next_y = now_x + dx[i], now_y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < n and graph[next_x][next_y] == 0:  # 체스판 안에있고, 아직 방문하지 않은곳
                queue.append((next_x, next_y))
                graph[next_x][next_y] = graph[now_x][now_y] + 1


tc = int(input())  # 테스트 케이스

for _ in range(tc):
    n = int(input())  # 체스판의 크기
    graph = [[0] * n for _ in range(n)]  # 체스판
    start_x, start_y = map(int, input().split())  # 현재 나이트의 위치
    target_x, target_y = map(int, input().split())  # 목표 나이트의 위치

    # 현재 위치랑 목표위치랑 동일하면 종료
    if start_x == target_x and start_y == target_y:
        print('0\n')
        continue

    rlt = bfs(start_x, start_y, target_x, target_y)
    print(str(rlt) + '\n')
