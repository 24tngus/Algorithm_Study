'''
@ No        : 1920
@ Title     : 수 찾기
@ Subject   : 이진탐색


@ 입력값
    - n : n의 개수
    - num_list : n개 개수 만큼 입력된 숫자 리스트
    - m : 확인할 숫자의 개수
    - chk_list : num_list에 있는지 없는지 확인할 숫자 종류
@ 출력값
    - num_list에 존재하는 수는 1, 아니면 0으로 출력
'''


# 1. 입력값
n = int(input())
num_list = set(map(int, input().split())) # 중복을 없애는 것이 중요

m = int(input())
chk_list = list(map(int, input().split()))

# n = 5
# num_list = [4, 1, 5, 2, 3]
# m = 5
# chk_list = [1, 3, 7, 9, 5]

# 존재여부 확인
# 존재하면 1 , 아니면 0 출력

[print(1) if i in num_list else print(0) for i in chk_list]


