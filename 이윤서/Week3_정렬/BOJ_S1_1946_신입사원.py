"""
두 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는다.
= 두 성적 모두 자신보다 나은 지원자가 없다.
= 한 성적을 기준으로 정렬했을 때, 뒤에 다른 성적이 높은 지원자가 없다면 뽑힌다.
"""
import sys

T = int(input())

for _ in range(T):
  ans = 1
  N = int(input())
  scores = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
  # 서류심사 성적 기준으로 정렬하고,
  scores.sort()
  
  prev = scores[0][1]
  # 서류심사 성적이 낮은 사람부터 순회할 때
  for i in range(1, N):
    # 면접 성적이 높은 지원자가 아니라면
    if scores[i][1] < prev:
      # 뽑힌다.
      ans += 1
      prev = scores[i][1]
  print(ans)