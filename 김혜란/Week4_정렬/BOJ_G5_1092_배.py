'''
@ No        : 1092
@ Title     : 배
@ Subject   : 그리디, 정렬

@ 입력값
    - n : 크레인 대수
    - crain_weights : 크레인 별 무게 제한
    - m : 박수 개수
    - box_weights : 박스 별 무게
@ 출력값
    - 박스를 옮기는데 소요된 시간
    - 박스 하나라도 옮길 수 없는 경우 -1 출력
'''

# n = 3
# crain_weights = [6, 8, 9]
#
# m = 5
# box_weights = [2, 5, 2, 4, 7]

n = int(input())
crain_weights = list(map(int, input().split()))

m = int(input())
box_weights = list(map(int, input().split()))



crain_weights.sort(reverse=True)
box_weights.sort(reverse=True)


time = 0
if crain_weights[0] < box_weights[0]:
    time = -1
else:
    while box_weights:
        for crain in crain_weights:
            # 아직 옮기지 않은 박스 존재 + 최대 무게 박스가 크레인 최대 무게보다 큰 경우에는 continue
            if box_weights and crain < box_weights[-1]:
                continue
            else:
                # 박스 중에서 크레인 하중 이하인 박스는 옮긴다.
                for box in box_weights:
                    if box <= crain:
                        box_weights.remove(box)
                        break
        # 크레인 전체로 훑을 때 마다 +1
        time += 1


print(time)



# 1. 입력값
crain_weights = [9, 8, 6]
box_weights = [2, 5, 2, 4, 7]

# 2. 정렬 (내림차순)

crain_weights = [9, 8, 6]
box_weights = []

time += 1

print(time)







