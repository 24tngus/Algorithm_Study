import sys

N = int(input())

students = []
for _ in range(N*N):
    students.append(list(map(int, sys.stdin.readline().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

board = [[0 for _ in range(N)] for _ in range(N)]
for student in students:
    possibilities = []
    for i in range(N):
        for j in range(N):
            like = 0
            vacant = 0

            if board[i][j] == 0: # 비어있는 칸 중에서
                for k in range(4): # 각각 인접한 칸의 경우에,
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx < 0 or ny < 0 or nx >= N or ny >= N:
                        continue
                    if board[nx][ny] in student[1:]:
                        like += 1
                    if board[nx][ny] == 0:
                        vacant += 1
                possibilities.append([like, vacant, i, j])
    # 좋아하는 학생이 인접한 칸에 가장 많은 칸으로
    # 여러 개이면, 비어있는 칸이 가장 많은 칸으로
    # 여러 개이면, 행의 번호가 가장 작은 칸으로
    # 여러 개이면, 열의 번호가 가장 작은 칸으로
    possibilities.sort(key=lambda x:(-x[0], -x[1], x[2], x[3]))
    board[possibilities[0][2]][possibilities[0][3]] = student[0]

ans = 0
students.sort()
for i in range(N):
    for j in range(N):
        cnt = 0
        # 인접한 칸에 앉은,
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            # 좋아하는 학생의 수
            if board[nx][ny] in students[board[i][j]-1][1:]:
                cnt += 1
        if cnt != 0:
            ans += 10 ** (cnt - 1)
print(ans)