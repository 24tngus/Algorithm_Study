'''
@ No. 1541
@ 읽어버린 괄호

@ 입력값: 수식 예) 55 - 50 + 40
@ 출력값 : 수식의 값이 최소가 되는 결과값 출력
'''

expresions = '00009-00009'.split('-')

expresions = input().split('-')

value_list = []
for exp in expresions:
    temp_list = exp.split('+')

    temp_val = 0
    for i in temp_list:
        temp_val += int(i)

    value_list.append(temp_val)
rslt = value_list[0]
for j in range(1, len(value_list)):
    rslt -= value_list[j]

print(rslt)