'''
@ No        : 15686
@ Title     : 치킨 배달
@ Subject   : 구현

@ 입력값
    - n             : 도시 가로, 세로 길이 값 (정사각형)
    - m             :  폐업시키지 않을 치킨집을 최대 m개
    - n*n           : 도시의 정보(0은 빈 곳, 1은 집, 2는 치킨 가게)
@ 출력값
    - min_distance : 치킨가게외 집과의 최소 거리
'''

'''
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2
'''

from itertools import combinations


# 1. 입력값
n, m = map(int, input().split(' '))
# n, m = 5, 2

locations_list = []
for _ in range(n):
    locations_list.append(list(map(int, input().split(' '))))
#
# locations_list = [[0, 2, 0, 1, 0],
#                  [1, 0, 1, 0, 0],
#                  [0, 0, 0, 0, 0],
#                  [2, 0, 0, 1, 1],
#                  [2, 2, 0, 1, 2]]

# 2. 치킨 집 위치 정보
chicken_home_list = []
for i in range(n):
    for j in range(n):

        if locations_list[i][j] == 2:
            chicken_home_list.append([i,j])

chicken_combi = combinations(chicken_home_list, m)


city_distance = []
for combi in chicken_combi:
    #([0, 1], [3, 0])
    # 여기 위치에 해당하는 치킨집들과만 치킨 거리 구하기

    chicken_distance = []

    for i in range(n):
        for j in range(n):
            if locations_list[i][j] == 1:

                # 치킨 거리 구하기 즉, 집과 치킨 집들과의 거리 구하기
                temp_distance = []
                for c in combi:
                    temp_distance.append(abs(c[0] - i) + abs(c[1] - j))
                # A 집과 1, 2 치킨 집과의 거리 중 가장 작은 값을 치킨 거리로 저장
                chicken_distance.append(min(temp_distance))

    city_distance.append(sum(chicken_distance))

result = min(city_distance)

print(result)







