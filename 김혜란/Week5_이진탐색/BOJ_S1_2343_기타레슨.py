'''
@ No        : 2343
@ Title     : 기타레스
@ Subject   : 이진 탐색


@ 입력값
    - n : 강의 수
    - m : 블루레이 개수
    - lecture_list : 강의 별 녹화 시간
@ 출력값
    - 블루레이 최소 크기
'''


# 1. 입력값
n, m = 9, 3
lecture_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# 2. 블루레이 크기 범위
start, end = sum(lecture_list)// 3, sum(lecture_list)


while start <= end:

    mid = (start + end) // 2
    cnt = 0

    time = 0
    bluray_list = [0] * m

    for i in lecture_list:
        if cnt >= 2:
            break

        if time + i <= mid:
            time += i
            bluray_list[cnt] = time
        else:
            cnt += 1 # 다음 블루레이에 저장
            bluray_list[cnt] = i


    if sum(bluray_list) <= sum(lecture_list):

        start = mid + 1
    else:
        end = mid - 1






