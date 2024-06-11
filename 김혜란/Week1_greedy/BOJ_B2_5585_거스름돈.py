'''
@ no. 5585 - 거스름돈
'''


cash_unit = [500, 100, 50, 10, 5, 1]

# 입력값: 제품 가격
# product_value = 380
input_cash = 1000 # 손님이 낸 돈
product_value = int(input())

out_cash = input_cash - product_value
cnt = 0
for cash in cash_unit:

    if out_cash / cash >= 1:
        cash_cnt = out_cash // cash
        out_cash -= cash * cash_cnt
        cnt += cash_cnt

print(cnt)



