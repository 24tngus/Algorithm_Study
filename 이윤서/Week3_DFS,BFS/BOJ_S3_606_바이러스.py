from collections import deque

N = int(input())
K = int(input())

board = [[0 for j in range(N+1)] for i in range(N+1)]
visited = [False]*(N+1)

for _ in range(K):
  x, y = map(int, input().split())
  if not visited[x]:
    visited[x] = True
    board[x][y] = y
    board[y][x] = x
    
ans = 0    
visited2 = [False]*(N+1)
queue = deque([1])
while queue:
  node = queue.popleft()
  for n in board[node]:
    if n != 0 and not visited2[n]:
      visited2[n] = True
      queue.append(n)
      ans += 1
    
print(ans)