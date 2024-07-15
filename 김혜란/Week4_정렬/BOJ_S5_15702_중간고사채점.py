'''
@ No        : 15702
@ Title     : 중간고사 채점
@ Subject   : 그리디, 정렬

@ 입력값
    - n : 문제 수
    - m : 응시한 사람 수
    - score_list : 문제별 점수
    - applicant_info_dict : 시험 응시자별 문제별 정답 여부
@ 출력값
    -
'''

# 1. 입력값
n, m = map(int, input().split())
# n, m = 4, 4

score_list = list(map(int, input().split()))
# score_list = [10, 20, 30, 40] # 총 문제 수 n개에 따라 크기가 달리짐을 유의

applicant_info_dict = {}
for i in range(m):
    temp_list = list(input().split())
    applicant_info_dict[int(temp_list[0])] = [1 if j == 'O' else 0 for j in temp_list[1:]]

# 정답 O: 1, 오답: X: 0
# applicant_info_dict = {1: [1, 0, 0, 0],
#                        2: [0, 1, 0, 0],
#                        3: [0, 0, 1, 0],
#                        4: [0, 0, 0, 1]
#                        }



# 2. 각 응시자별 점수 계산
total_score_list= []
for key, value in applicant_info_dict.items():
    total_score = 0

    for i in range(len(value)):

        if value[i] == 1:
            total_score += score_list[i]

    # print('학생: {} 총 점수: {}'.format(key, total_score))

    total_score_list.append([key, total_score])


# 3. 정렬
# 1순위: 점수 내림차순 > 2순위: 학생 번호 오름차순

result = sorted(total_score_list, key=lambda x : (-x[1], x[0]))

print(result[0][0], result[0][1])