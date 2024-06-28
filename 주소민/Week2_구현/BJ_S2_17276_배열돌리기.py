from copy import deepcopy
# import sys
# input = sys.stdin.readline

# 사용자 입력 값
max_range = int(input())
for _ in range(max_range):
    array = []
    n, d = map(int, input().split())
    for _ in range(n):
        array.append(list(map(int, input().split())))

    if d < 0:
        d = 360 + d

    if d == 360 or d == 0:
        for arr in array:
            print(*arr)
        continue

    rotate_cnt = d // 45
    if rotate_cnt > 4:
        rotate_cnt -= 4
    # 결과 저장할 배열
    result = [[0] * n for _ in range(n)]

    for _ in range(d // 45):
        # 행
        for i in range(n):
            # 열
            for j in range(n):
                # 주 대각선
                if i == j:
                    # 주 대각선 값을 가운데 행으로 변경
                    result[i][j] = array[n // 2][j]
                # 가운데 행
                elif i == n // 2:
                    # 부 대각선 값으로 변경
                    result[i][j] = array[n - j - 1][j]
                # 부 대각선
                elif i + j == n - 1:
                    # 가운데 열 값으로 변경
                    result[i][j] = array[i][n // 2]
                # 가운데 열
                elif j == n // 2:
                    result[i][j] = array[i][i]
                else:
                    result[i][j] = array[i][j]
        array = deepcopy(result)

    for k in result:
        print(*k)
