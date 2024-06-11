'''
@ no. 11000 - 강의실 배정
@ key point: heap 자료구조 사용해야함.
'''


# n = int(input())
#
# time_tables = []
# for _ in range(n):
#     start, end = map(int, input().split(' '))
#     time_tables.append([start, end])
#
# time_tables = [[1,3], [2, 4], [3, 9], [3,5]]
#
# # 오름차순으로 정렬
# time_tables.sort(key = lambda x:(x[1], x[0]))
#
# lecture_room_dict = {}
# room_cnt = 1
#
# # 첫번째 강의실 부터 우선 지정
# lecture_room_dict[room_cnt] = [time_tables[0]]
#
# for i in range(1,len(time_tables)):
#     for key in lecture_room_dict.keys():
#         # 각 강의실 마지막 수업 종료 시간 <= 현재 강의 시작 시간
#         # 기존 강의실에 추가
#         if lecture_room_dict[key][[-1][-1]][1] <= time_tables[i][0]:
#             lecture_room_dict[key] = lecture_room_dict[key] + [time_tables[2]]
#             break
#         else:
#             # 새로운 강의실 추가
#             room_cnt += 1
#             lecture_room_dict[room_cnt] = [time_tables[i]]
#             break
#
#
# print(max(lecture_room_dict.keys()))


import sys
from collections import deque
import heapq
input = sys.stdin.readline

time_tables = []
n = int(input())
for _ in range(n):
    start, end = map(int, input().split(' '))
    time_tables.append([start, end])

# 강의 시간표 오름차순 정렬
time_tables.sort()

time_deque = deque()
end_time = time_tables[0][1]
time_deque.appendleft(end_time)

for i in range(1, len(time_tables)):

    if time_tables[i][0] in time_deque:
        time_deque.remove(time_tables[i][0])
        time_deque.appendleft(time_tables[i][1])

    else:
        time_deque.appendleft(time_tables[i][1])

print(len(time_deque))

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


