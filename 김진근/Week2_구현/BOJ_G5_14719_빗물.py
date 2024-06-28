import sys
input = sys.stdin.readline # 빠른 입력
print = sys.stdout.write # 빠른 출력, 출력은 반드시 문자열로

h, w = map(int,input().split())     #세로H 가로W
block = list(map(int,input().split()))
answer = 0

# 좌우는 고정이니 1부터 끝 -1부터 돌기
for i in range(1, w-1):
    # 기준을 두고 왼쪽 오른쪽의 min 찾고
    left = max(block[ :i])
    right = max(block[i+1: ])
    m = min(left, right)
    if m > block[i]:    # 높이 차이만큼 더해줘야한다
        answer += m - block[i]

print(str(answer))