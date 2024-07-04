from collections import deque

def min_moves(start, target, n):
  movs = [[1, 2], [2, 1], [-1, 2], [-2, 1], [-2, -1], [2, -1], [-1,-2], [1, -2]]
  queue = deque([(start[0], start[1], 0)])
  visited = set()
  visited.add((start[0], start[1]))
  
  while queue:
    current_x, current_y, moves = queue.popleft()
    
    if (current_x, current_y) == (target[0], target[1]):
      return moves
      
    for mov in movs:
      new_x = current_x + mov[0]
      new_y = current_y + mov[1]
      
      if 0 <= new_x < n and 0 <= new_y < n and (new_x, new_y) not in visited:
        visited.add((new_x, new_y))
        queue.append((new_x, new_y, moves+1))

T = int(input())
ans = []

for _ in range(T):
  n = int(input())
  current_x, current_y = map(int, input().split())
  target_x, target_y = map(int, input().split())
  
  result = min_moves((current_x, current_y), (target_x, target_y), n)
  ans.append(result)
  
for a in ans:
  print(a)