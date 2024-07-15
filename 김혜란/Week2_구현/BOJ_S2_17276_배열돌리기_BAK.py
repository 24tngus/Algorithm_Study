'''
@ No        : 17276
@ Title     : 배열 돌리기
@ Subject   : 구현

@ 입력값
    -
@ 출력값
    -
'''

result = [] # 테스트별 결과를 넣을 리스트 변수

n = 5
# 새로운 배열에 입력
# 주 대각선 > 가운데 열 > 부 대각선 > 가운데 행 순서로 값을 입력
d = 45


org_array = [[1,  2,  3,  4, 5],
          [6,  7,  8,  9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25]]


# 값이 0으로 된 템플릿 생성
new_array = [[0 for _ in row] for row in org_array]


# 회전 할 때 위치가 변하는 값들만 출력
# 주 대각선 > 가운데 열 > 부 대각선 > 가운데 행 순서로 값을 출력
move_array = []

move_array.append([org_array[i][i] for i in range(len(org_array))]) # 주 대각선
move_array.append([org_array[i][(n+1)//2 - 1] for i in range(len(org_array))]) # 가운데 열
move_array.append([org_array[i][n - i - 1] for i in range(len(org_array))]) # 부 대각선
move_array.append([org_array[(n+1)//2 - 1][i] for i in range(len(org_array))]) # 가운데 행



# 반시계 방향 회전시 (마이너스 각도일 때)
if d < 0:
    d = 360 + d

start_point = d // 45 # 주 대각선이 입력을 시작하는 대각선 번호


# 이동하는 숫자들 부터 대각선별로 값 넣기
for i in range(4):

    num = (i + start_point) % 8

    if num == 0:
        for j in range(n):
            new_array[j][j] = move_array[i][j]

    elif num == 1:
        for j in range(n):
            new_array[j][n//2] = move_array[i][j]

    elif num == 2:
        for j in range(n):
            new_array[j][n-1-j] = move_array[i][j]

    elif num == 3:
        for j in range(n-1, -1, -1):
            new_array[n//2][n-1-j] = move_array[i][j]

    elif num == 4:
        for j in range(n):
            new_array[n-1-j][n-1-j] = move_array[i][j]
            # new_array[j][j] = move_array[i][j]

    elif num == 5:
        for j in range(n):
            new_array[j][n//2] = move_array[i][n-1-j]

    elif num == 6:
        for j in range(n):
            new_array[j][n-1-j] = move_array[i][j]

    elif num == 7:
        for j in range(n):
            new_array[n//2][j] = move_array[i][j]


# 움직이지 않는 숫자들 넣기
for i in range(n):
    for j in range(n):
        if new_array[i][j] == 0:
            new_array[i][j] = org_array[i][j]

# result 변수에 2차원 리스트가 테스트 한번이 끝날 때 마다 추가된다.
result.append(new_array)

for test in result:
    for row in test:
        print(*row)

11 2 1 4 3
6 12 7 8 10
21 17 13 9 5
16 18 19 14 20
23 22 25 24 15