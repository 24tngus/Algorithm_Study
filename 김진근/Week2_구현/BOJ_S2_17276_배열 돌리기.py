import sys
input = sys.stdin.readline # 빠른 입력
print = sys.stdout.write # 빠른 출력, 출력은 반드시 문자열로

cnt = int(input().strip())

def right_turn(arr, n):
    num = n//2
    for i in range(n):
        arr[i][i], arr[i][num] = arr[i][num], arr[i][i]
        arr[i][i], arr[i][n-1-i]=arr[i][n-1-i], arr[i][i]
        arr[i][i], arr[num][i] = arr[num][i], arr[i][i]

    for i in range(num):
        arr[num][i], arr[num][n-1-i] = arr[num][n-1-i], arr[num][i]

    return arr

def left_turn(arr, n):
    num = n//2
    for i in range(n):
        arr[i][n-1-i], arr[i][num] = arr[i][num], arr[i][n-1-i]
        arr[i][n-1-i], arr[i][i] = arr[i][i], arr[i][n-1-i]
        arr[i][n-1-i], arr[num][i] = arr[num][i], arr[i][n-1-i]

    for i in range(num):
        arr[n-1-i][i], arr[i][n-1-i] = arr[i][n-1-i], arr[n-1-i][i]
    return arr

for _ in range(cnt):
    a, b = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(a)]
    if b >= 0:
        p_d = b // 45
        for _ in range(p_d):
            array = right_turn(array, a)
    else:
        p_d = abs(b) // 45
        for _ in range(p_d):
            array = left_turn(array, a)

    for i in range(a):
        for j in range(a):
            print(str(array[i][j]) + ' ')
        print("\n")
