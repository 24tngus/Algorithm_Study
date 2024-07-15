
'''
@ No        : 2606
@ Title     : 바이러스
@ Subject   : BFS/DFS

@ 입력값
    - 컴퓨터 수
    - 네트워크 상에서 연결된 컴퓨터 쌍의 수
@ 출력값
    - 바이러스에 감연된 컴퓨터의 수 (1번 컴퓨터를 제외하고)
'''


'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''

# n = 7
# p = 6
n = int(input())
p = int(input())

pair_list = [[] for _ in range(n+1)] # [[], [], [], [], [], [], [], []]
visited =  [0 for _ in range(n+1)]


# [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
for _ in range(p):
    num1, num2 = map(int, input().split())
    pair_list[num1].append(num2)
    pair_list[num2].append(num1)

# pair_list = [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]


def dfs(start):
    stack = [start] # 방문할 노드 번호 스택에 입력
    visited[start] = 1 # 방문 처리
    cnt = 0

    while stack:
        node = stack.pop()
        for next in pair_list[node]:
            if visited[next] == 0:
                visited[next] = 1
                stack.append(next)
                cnt += 1
    return cnt

print(dfs(1)) # 1번 노드 부터 시작
