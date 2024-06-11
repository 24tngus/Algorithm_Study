'''
@ no. 1339 - 뒤집기
'''

n = int(input())

char_list = []
for _ in range(n):
    char_list.append(input())

# char_list = ['ACDEB', 'GCF']
digit_dict = {}

for char in char_list:
    for i in range(len(char)):
        # 해당 문자의 자릿수가 있다면
        if char[i] in digit_dict.keys():
            digit_dict[char[i]] = digit_dict[char[i]] + (10 ** (len(char) - 1 - i))
        else:
            digit_dict[char[i]] = 10 ** (len(char) - 1 -i)

char_orders_dict = {}
digit_order_dict = sorted(digit_dict.items(), key=lambda x: x[1], reverse=True)

start_number = 9
for digit in digit_order_dict:
    char_orders_dict[digit[0]] = start_number
    start_number -= 1


char_to_num_list = []
for char in char_list:
    char_to_num = ''

    for s in char:
        char_to_num += str(char_orders_dict[s])

    char_to_num_list.append(int(char_to_num))


print(sum(char_to_num_list))

# --------- 딕셔너리 정렬 ------------ #
# 다른 방법 참고
# import operator
# digit_dict = sorted(digit_dict.items(), key=operator.itemgetter(1), reverse=True)



