"""
$ 회의의 최대 개수

@ 무엇을 우선적으로 선택해야 할까?
    1. 가장 빨리 끝나는 회의 
      - 구현: 끝나는 시간을 기준으로 오름차순 정렬
    2. 가장 짧은 회의
      - 구현: 매번 겹치지 않는 회의를 선택하기 위해 타임라인 전체 순회해야 하므로 비효율적

@ 테스트 케이스
    1. 모든 회의가 겹치는 경우 -> 끝나는 시간이 빠른 순으로 정렬
    2. 끝나는 시간이 같은 회의가 있는 경우 -> 시작 시간이 빠른 순으로 정렬
"""

n = int(input())
timeline = [list(map(int, input().split())) for _ in range(n)]

timeline.sort(key=lambda x: (x[1], x[0])) # O(NlogN)

ans = 1 # 첫번째 회의는 무조건 선택
endPoint = timeline[0][1]
for i in range(1, n): # 전체 타임라인을 순회하면서
    if timeline[i][0] >= endPoint: # 현재 타임라인과 겹치지 않는 회의가 있다면
        endPoint = timeline[i][1] # 해당 회의를 선택하고
        ans += 1 # 회의 개수를 증가시킨다.
print(ans)