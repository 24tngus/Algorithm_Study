'''
@ No        : 7562
@ Title     : 나이트의 이동
@ Subject   : BFS/DFS

@ 입력값
    - t: 테스트 케이스 개수
    - l: 체스판 한 변의 길이 (전체 크기 = l^2)
    - now = 현재 나이트가 있는 칸
    - move = 나이트가 이동하고자 하는 칸
@ 출력값
    - 바이러스에 감연된 컴퓨터의 수 (1번 컴퓨터를 제외하고)
'''

from collections import deque




dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]


def dfs():

    q = deque()
    q.append((now_knite[0], now_knite[1]))

    while q:
        x, y = q.popleft() # 현재 방문한 위치 큐에서 출력

        if x == dest_knite[0] and y == dest_knite[1]:
            return chess[x][y] - 1

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            # 체스판 안에 있
            if 0 <= nx < l and 0 <= ny < l and chess[nx][ny] == 0:
                chess[nx][ny] = chess[x][y] + 1
                q.append((nx, ny)) # 다음 위치 큐에 저장



t = int(input())
for _ in range(t):
    l = int(input())
    chess = [[0] * l for _ in range(l)]

    now_knite = list(map(int, input().split()))
    chess[now_knite[0]][now_knite[1]] = 1

    dest_knite = list(map(int, input().split()))
    print(dfs())
