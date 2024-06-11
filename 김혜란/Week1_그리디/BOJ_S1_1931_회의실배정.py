'''
@ no. 1931 - 회의실 배정
'''

n = int(input())
meeting_list = []
for _ in range(n):
    start, end = map(int, input().split(' '))
    meeting_list.append([start, end ])


# 열 기준으로 오름차순
meeting_list.sort(key=lambda x: (x[1], x[0]))

start = meeting_list[0][0]
end = meeting_list[0][1]
cnt = 1

for i in range(1,len(meeting_list)):
    if meeting_list[i][0] >= end:
        # start = meeting_list[i][0]
        end = meeting_list[i][1]
        cnt += 1

print(cnt)





