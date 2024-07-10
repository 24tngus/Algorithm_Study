import sys
input = sys.stdin.readline # 빠른 입력
print = sys.stdout.write # 빠른 출력, 출력은 반드시 문자열로

N = int(input()) # 집의수
home = list(map(int, input().split())) #집의 좌표

home.sort() # 짝수면 중간 앞에꺼 4 -> 4/2 = 2-1 홀수명 5/2 ->2

if(N%2 == 0):
    print(str(home[N//2 -1]))
else:
    print(str(home[N//2]))
