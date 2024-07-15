'''
@ No        : 6068
@ Title     : 시간 관리하기
@ Subject   : 그리디, 정렬

@ 입력값
    - n : 해야할 일의 개수
    - 해야할 일에 대한 정보([t, s])
        - t : 작업시간
        - s : 일을 끝내야 하는 시간
@ 출력값
    - 하루가 0부터 시작 할떄, 일을 최대한 늦게 시작할 수 있는 시각
'''

n = int(input())
work_list = [list(map(int, input().split())) for _ in range(n)]

n = 4
work_list = [[17, 63], [32, 95], [38, 129], [11, 104]]
# work_list = [[3, 5],[8, 14],[5, 20],[1, 16]]

# 마감 시간 기준 내림차순 정렬
work_list = sorted(work_list, key = lambda x: (x[1], x[0]), reverse = True)
# [[5, 20], [1, 16], [8, 14], [3, 5]]

# 마감 시간 max 값이 최종 마감 시간
time = work_list[0][1]

for i in range(n):

    if work_list[i][1] <= time:
        # 다음 작업 end_time
        # 마감 시간 - 작업 시간
        time = (work_list[i][1] - work_list[i][0])

    else:
        # 뒷 작업 시작 시간보다 마감 시간이 큰 경우
        # 뒷 작업 시작 시간 - 현재 작업 시간
        time -= work_list[i][0]

if time >= 0:
    print(time)
else:
    print(-1)