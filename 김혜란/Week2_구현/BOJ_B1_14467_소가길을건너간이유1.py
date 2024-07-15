'''
@ No        : 14467
@ Title     : 소가 길을 건너간 이유1
@ Subject   : 구현

@ 입력값
    - n             : 소의 종류와 소의 위치를 입력받을 횟수
    - cow, location : 소의 종류와 소의 위치
@ 출력값
    - min_cnt : 소들의 최소 이동 횟수
'''

# 1. 입력값
n = int(input())

cows_location_list = []
for _ in range(n):
    cow, location = map(int, input().split(' '))
    cows_location_list.append([cow, location])

cows_location_list = [[3, 1], [3, 0], [6, 0], [2, 1], [4, 1], [3, 0], [4, 0], [3, 1]]

move_cnt = 0

cow_dict = {}
for cow, location in cows_location_list:
    if cow not in cow_dict:
        cow_dict[cow] = [location]
    elif cow in cow_dict and (cow_dict[cow][-1] != location):
        cow_dict[cow] = [location]
        move_cnt += 1

print(move_cnt)





