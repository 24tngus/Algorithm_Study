import sys
input = sys.stdin.readline # 빠른 입력
print = sys.stdout.write # 빠른 출력, 출력은 반드시 문자열로

def dfs(now):
    global ans

    ans+=1  #바이러스 퍼져나가는수
    v[now] = 1 #방문여부 체크

    #연결된 노드 확인하기
    for tmp in arr[now]:
        if v[tmp] == 0: #방문 X
            v[tmp] = 1
            dfs(tmp)

n = int(input()) # 컴퓨터수
m = int(input()) # 연결된 컴퓨터의 쌍의 수

arr = [[] for _ in range(n+1)] #연결된 컴퓨터들 넣기 1부터 시작

for _ in range(m):
    s,e = map(int,input().split()) #시작점과 연결된 노드
    arr[s].append(e)
    arr[e].append(s)    #양방향 모두 연결해 주기  1 - 2 | 2- 1

ans = 0;
v = [0] * (n+1) #방문 여부 체크
dfs(1) #1번이 바이러스에걸림

print(str(ans-1))
# 5개 연결되어있으면 4개 전염 -> 1번은 원래 걸림
