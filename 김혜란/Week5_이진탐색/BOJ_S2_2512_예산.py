'''
@ No        : 2512
@ Title     : 예산
@ Subject   : 이진 탐색


@ 입력값
    - n : 예산 요청 수
    - budget_list : 지방 별 요청한 예산
    - budget : 현재 사용 가능한 총 예산
@ 출력값
    - 각 지방별 예산을 배분 했을 때, 최대 예산 금액은?
'''

# 1. 입력값
# n = 4
# budget_list = [120, 110, 140, 150]
# budget = 485
n = int(input())
budget_list = list(map(int, input().split()))
budget =  int(input())

# 2. 예산 범위
start, end = 1, max(budget_list)

chk = 0
# 3. 예산 배분
while start <= end:
    chk += 1
    mid = (start + end) // 2

    # print('{} : [{} , {}] '.format(chk, start,end))
    # print('mid = {}'.format(mid))
    total = 0

    for i in budget_list:
        if i > mid:
            total += mid # 중간값보다 크면 중간값으로
        else:
            total += i # 중간값보다 작으면 해당 예산으로


    if total <= budget:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)









