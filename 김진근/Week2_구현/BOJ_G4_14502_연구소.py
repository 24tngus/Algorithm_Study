import sys
input = sys.stdin.readline # 빠른 입력
print = sys.stdout.write # 빠른 출력, 출력은 반드시 문자열로
from collections import deque

def bfs(tlist):
    # [1] 빈공간 막기 (3개 선택해서 좌표 1로 저장)
    for i,j in tlist:
        arr[i][j] =1

    count = CNT-3 #3개 막았으니까, -3 한게 최대 갯수 count->MAX인걸 찾으면 된다.

    #임시 덱
    # [2] 변수 + 큐 초기화
    q = deque()
    v2 = [[0]*M for _ in range(N)]

    #바이러스 좌표 넣기
    for ti,tj in virus:
        q.append((ti,tj))
        v2[ti][tj] = 1 #방문 표시하기

    # [3] 큐에 데이터 있을대 한개씩 처리
    while q:
        ci,cj = q.popleft() #현재 좌표
        # 조건 = 네방향, 범위내, 미방문, 조건(==0)
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):   #상하좌우 네방향
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and v2[ni][nj] == 0 and arr[ni][nj] == 0:
                v2[ni][nj] = 1 #방문
                q.append((ni,nj))
                count -=1 #확산 되었을때 한개씩 빼주기

    # [0] 벽 초기화
    for i,j in tlist:
        arr[i][j] =0
    return count    #남은 0수

def dfs(n,tlist):
    global ans
    # BFS 종료조건 -> 빈공간 벽 3개 선택
    if n==3:
        ans = max(ans,bfs(tlist))
        return

    for j in range(CNT):
        if v[j] == 0:
            v[j] = 1  #방문
            dfs(n+1, tlist+[lst[j]])
            v[j] = 0    #초기화


N, M = map(int, input().split()) #세로N 가로M
arr = [list(map(int, input().split())) for _ in range(N)] #지도

# 빈칸 list
# 바이러스 좌표 virus
lst = []
virus = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0: #빈좌표
            lst.append((i,j))
        elif arr[i][j] == 2: #바이러스
            virus.append((i,j))

CNT = len(lst) #BFS
v = [0]*CNT #방문부 chk
ans = 0

dfs(0,[])
print(str(ans))