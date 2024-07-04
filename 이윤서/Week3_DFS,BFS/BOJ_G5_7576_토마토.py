from collections import deque

ans = 0
movs = [[0,1], [0,-1], [1,0], [-1,0]]
queue = deque()

def spread():
  while queue:
    curr_x, curr_y = queue.popleft()
    for mov in movs:
      new_x = curr_x + mov[0]
      new_y = curr_y + mov[1]
      if 0 <= new_x < N and 0 <= new_y < M and box[new_x][new_y] == 0:
        # 처음 시작이 1이므로 뒤에서 -1 처리를 해줘야 합니다.
        box[new_x][new_y] = box[curr_x][curr_y] + 1
        queue.append([new_x, new_y])
        

M, N = map(int, input().split())
# 토마토 값을 2차원 리스트에 저장합니다.
box = []
# 값은 -1, 0, 1을 가질 수 있습니다.
for _ in range(N):
  row = list(map(int, input().split()))
  box.append(row)

# 처음부터 이미 익은 토마토의 위치를 큐에 저장합니다.
for i in range(N):
  for j in range(M):
    if box[i][j] == 1:
      queue.append([i, j])
      
# 토마토를 익힙니다.
spread()

# 최대한 익힌 후,
for row in box:
  for element in row:
    # 다 익히지 못했다면 -1을 출력하고,
    if element == 0:
      print(-1)
      exit(0)
    # 다 익혔다면 최댓값을 출력합니다.
    ans = max(ans, element)
print(ans-1)