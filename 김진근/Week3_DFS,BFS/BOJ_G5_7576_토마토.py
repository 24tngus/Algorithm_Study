import sys
from collections import deque

input = sys.stdin.readline  # 빠른 입력
print = sys.stdout.write  # 빠른 출력, 출력은 반드시 문자열로
# 1->익은 토마토, 0->익지 않은 토마토, -1-> 토마토가 들어가있지 않은 칸

#상하좌우
dx = [0,0,-1,1]
dy = [1,-1,0,0]
def bfs():
    # [1] q생성, v[] 방문 배열 생성
    q = deque()
    v = [[0]*M for _ in range(N)]

    # 초기 데이터 q에 데이터 넣기
    cnt = 0 #안익은 토마토 수
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1: #익은 토마토일때
                q.append((i,j))
                v[i][j] = 1 #익은토마토 방문처리
            elif arr[i][j] == 0: #안익은 토마토
                cnt += 1

    # bfs
    while q:
        now_i,now_j = q.popleft()

        # 상하좌우, 범위내, 미방문, 안익은 토마토
        for d in range(4):
            next_i,next_j = now_i+dx[d],now_j+dy[d]
            if 0<=next_i<N and 0<=next_j<M and v[next_i][next_j] == 0 and arr[next_i][next_j] == 0:
                q.append((next_i,next_j))
                v[next_i][next_j] = v[now_i][now_j] + 1  #하루씩 늘어남
                cnt -= 1 #안익은 토마토 넣기

    if cnt == 0: #다익었을때
        return v[now_i][now_j] -1 #마지막 좌표에 저장된 값, -1 시작을 1로 했으니까
    else:
        return -1


M,N =map(int,input().split()) #M(가로) * N(세로)
arr = [list(map(int,input().split())) for _ in range(N)] #토마토 입력
ans = bfs()
print(str(ans))