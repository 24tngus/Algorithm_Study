import sys

def rot(matrix, n, isNeg):
    temp =  [[0]*n for _ in range(n)]
    mid = (int)((n+1)/2) - 1

    for i in range(n):
        for j in range(n):
            if i == j:
                temp[i][j] = matrix[mid][i] if isNeg == 0 else matrix[i][mid]
            elif i == (n - 1) - j:
                temp[i][j] = matrix[i][mid] if isNeg == 0 else matrix[mid][j]
            elif i == mid:
                temp[i][j] = matrix[n-1-j][j] if isNeg == 0 else matrix[j][j]
            elif j == mid:
                temp[i][j] = matrix[i][i] if isNeg == 0 else matrix[i][n-1-i]
            else:
                temp[i][j] = matrix[i][j]
    return temp

def print_matrix(matrix, n):
    for row in matrix:
        print(" ".join(map(str, row)))

T = int(input())
for _ in range(T):
    n, degree = map(int, sys.stdin.readline().split())
    matrix = [[-1] * n for _ in range(n)]
    for i in range(n):
        nums = list(map(int, sys.stdin.readline().split()))
        for j in range(n):
            matrix[i][j] = nums[j]

    trial = abs(int(degree/45))

    if trial%8 == 0: # 360의 배수
        print_matrix(matrix, n)
        continue

    for _ in range(trial):
        matrix = rot(matrix, n, degree < 0)
    print_matrix(matrix, n)