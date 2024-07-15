'''
@ No        : 18310
@ Title     : 안테나
@ Subject   : 그리디, 정렬

@ 입력값
    - n : 집의 수
    - addr_list : n개 집 위치
@ 출력값
    - 안테나가 설치될 위치 (단, 여러개 일 경우 작은 위치 값을 출력)
'''


# 1. 입력값
# n = int(input())
n = 6

# addr_list = list(map(int, input().split()))
addr_list = [5, 1, 2, 3, 7, 9]
addr_list.sort()

if len(addr_list) % 2 == 0:
    # 짝수
    idx = len(addr_list) //2
    result = addr_list[idx-1]
else:
    # 홀수
    idx = len(addr_list) // 2
    result = addr_list[idx]
print(result)








