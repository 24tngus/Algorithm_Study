'''
@ No        : 2610
@ Title     : 컵홀더
@ Subject   : 그리디 / 복습

@ 입력값
    - n : 좌석 수
    - 좌석 배치
@ 출력값
    - 최대 컵홀더를 사용하는 사람 수
'''


# 1. 입력값 받기
n = 4
# n = int(input())


seats = 'SLLS'
# seats = input()

# 커플석 수만큼 컵홀더가 없다.
cup_holder = seats.count('LL')

if cup_holder <= 1 :
    print(len(seats))
else :
    print(len(seats) - cup_holder + 1)



