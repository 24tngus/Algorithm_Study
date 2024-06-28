# 소는 최대 1~10 총 11마리 들어올수있다
# 각위치 저장해놓고 바뀐 횟수만 세어보자

import sys
input = sys.stdin.readline #빠른 입력
print = sys.stdout.write #빠른 출력 출력은 반드시 문자열로

cow = [-1]*10 # -1 은 가지고 있지 않는 소
ans = 0

n = int(input()) #관찰수 -> 소가 총 몇번 길을 건넜는지
for _ in range (n):
    a,b = map(int,input().split())

    if cow[a-1] == -1: #처음 관찰
        cow[a-1] = b #처음 관찰위치 update

    elif cow[a-1] != b: #처음관찰이 아니고, 이전에 있었던 위치가 아닐때
        cow[a-1] = b    #위치 업데이트
        ans += 1    #건너간횟수 업데이트

print(str(ans))