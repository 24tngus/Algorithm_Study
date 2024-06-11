'''
@ no. 11000 - 강의실 배정
@ key point: heap 자료구조 사용해야함.
'''

import sys, heapq

n = int(sys.stdin.readline())
time_tables = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(n)])


room = []
heapq.heappush(room, time_tables[0][1])  # 첫 강의 끝나는 시간

for i in range(1, n):
    if time_tables[i][0] < room[0]:  # 강의의 시작 시간이 현재 강의 끝나는 시간 보다 짧으면
        heapq.heappush(room, time_tables[i][1])  # 새로운 강의실을 넣자
    else:  # 아니면
        heapq.heappop(room)  # 기존 강의를 빼내고
        heapq.heappush(room, time_tables[i][1])  # 해당 강의를 넣자

print(len(room))


