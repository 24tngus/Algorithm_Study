"""
모든 박스를 배로 옮기는데 드는 시간의 최솟값
= 가벼운 박스를 먼저 옮기면 무거운 박스를 들 수 있는 크레인이 제한되므로, 박스와 크레인을 내림차순으로 정렬한다.

1. 모든 박스를 옮길 때까지 반복한다.
2. 박스가 들어가기에 적합한 크레인을 찾아 박스를 넣는다.
3. 단, 가장 작은 크레인보다 가장 작은 박스가 큰 경우 ans는 -1이다.
"""
N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

if cranes[0] < boxes[0]:
  print(-1)
else:
  ans = 0
  while boxes:
    for crane in cranes:
      for i in range(len(boxes)):
        if crane >= boxes[i]:
          boxes.pop(i)
          break
    ans += 1
  print(ans)
        