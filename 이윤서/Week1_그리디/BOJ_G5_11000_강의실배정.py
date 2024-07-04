"""
$ 최소의 강의실
$ 모든 수업

@ 어떻게 정렬할 것인가?
    1. 가장 빨리 시작하는 강의
        - 구현: 시작 시간을 기준으로 오름차순 정렬


"""

n = int(input())
timeline = [list(map(int, input().split())) for _ in range(n)]

timeline.sort(key=lambda x: (x[0], x[1])) # O(NlogN)

