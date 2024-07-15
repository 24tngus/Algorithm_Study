'''
@ No        : 10816
@ Title     : 숫자 카드 2
@ Subject   : 이진 탐색


@ 입력값
    - n : n의 개수
    - num_list : n개 개수 만큼 입력된 숫자 리스트
    - m : 확인할 숫자의 개수
    - chk_list : num_list에 있는지 없는지 확인할 숫자 종류
@ 출력값
    - chk_list에 저장된 숫자들이 num_list에 몇 개 있는지 출력
'''


# 1. 입력값
n = int(input())
num_list = list(map(int, input().split()))

m = int(input())
chk_list = list(map(int, input().split()))


# n = 10
# num_list = [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
#
# m = 8
# chk_list = [10, 9, -5, 2, 3, 4, 5, -10]

num_dict = {}
for num in num_list:
    if num in num_dict.keys():
        num_dict[num] = num_dict[num] + 1
    else:
        num_dict[num] = 1

# result = []

for val in chk_list:
    if val in num_dict.keys():
        # result.append(num_dict[val])
        print(num_dict[val], end= ' ')
    else:
        # result.append(0)
        print(0, end=' ')