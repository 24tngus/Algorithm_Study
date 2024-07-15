'''
@ No        : 26947
@ Title     : 선물 할인
@ Subject   : 그리디, 정렬

@ 입력값
    - n : 선물 개수
    - b : 예산
    - d : 반값 할인을 받을 수 있는 선물개수
    - price_list = n개 선물 가격
@ 출력값
    - 최대 살 수 있는 선물의 수
@ 참고
https://blog.naver.com/rscracker/223392104593
'''

# 1. 입력값
# n, b, d = map(int, input().split())

n, b, d =  6, 26, 2


# price_list = list(map(int, input().split()))
price_list = [4, 6, 2, 10, 8, 12]

# price_list.sort()
# cumsum_list = [0]
# for i in range(1, n+1):
#     cumsum_list.append(sum(price_list[0:i]))
#
# for j in range(1, n+1):
#     if ((cumsum_list[i] - cumsum_list[i-min(i,d)])/2 + cumsum_list[i-min(i,d)]) <= b:
#         if i == n:
#             print(i)
#         continue
#     else:
#         print(i-1)
#         break
