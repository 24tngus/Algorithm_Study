taro_change = 1000 - int(input())
change_list = [500, 100, 50, 10, 5, 1]

answer = 0

# P_NOTE: [연산자] 정수 몫(//) 구하기
for change in change_list:
    answer += taro_change//change
    taro_change %= change

print(answer)
