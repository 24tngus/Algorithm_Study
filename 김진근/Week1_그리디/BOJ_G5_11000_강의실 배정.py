
'''import sys
input = sys.stdin.readline #빠른 입력
print = sys.stdout.write #빠른 출력 출력은 반드시 문자열로

n = int(input())
cls = [] #수업들 입력

for i in range(n):
    start, end = map(int,input().split())
    cls.append([start, end])

cls.sort(key=lambda x:(x[0],x[1])) # 시작 시간, 끝나는시간 정렬

end_times = [] #종료시간 넣는 배열

for start, end in cls:
    find = False
    #적합한 회의실이 있을때
    for i in range(len(end_times)):
        if end_times[i] <= start:
            end_times[i] = end #회의실에 수업 넣기
            find = True
            break #해당 수업을 찾았으니까 다른 수업 찾을필요 없음

    #회의실이 없으면 새로운 회의실 만들기
    if not find:
        end_times.append(end)

print(str(len(end_times)))
'''

import sys
import heapq

input = sys.stdin.readline # 빠른 입력
print = sys.stdout.write # 빠른 출력 출력은 반드시 문자열로

n = int(input())
cls = [] # 수업들 입력

for i in range(n):
    start, end = map(int, input().split())
    cls.append((start, end))

cls.sort() # 시작 시간 기준으로 정렬

# 종료 시간을 저장할 최소 힙 (우선순위 큐)
heap = []

# 첫 번째 회의의 종료 시간을 힙에 추가
heapq.heappush(heap, cls[0][1])

for i in range(1, n):
    start, end = cls[i]
    # 가장 빨리 끝나는 회의의 종료 시간보다 현재 회의의 시작 시간이 크거나 같다면 회의실을 재사용
    if heap[0] <= start:
        heapq.heappop(heap) # 회의실 회수
    heapq.heappush(heap, end) # 새로운 종료 시간을 힙에 추가

# 힙의 크기가 필요한 회의실의 수
print(str(len(heap)))


