'''
@ no. 1439 - 뒤집기
'''

input_string = list('11101101')
# input_string = list('11001100110011000001')
# input_string = list(input())

# 뒤집는 구간 확인

cnt = 0

for i in range(len(input_string)-1):
    if input_string[i] != input_string[i+1]:
        cnt+=1
    print(input_string)
print((cnt+1)//2)

# ------------------------------ 이전 풀이 ------------------------------- #
# while True:
#     if input_string.count(input_string[0]) == len(input_string):
#         break
#
#     reference_str = input_string[0]
#     start_point = 0
#     end_point = 0
#
#     for i in range(1,len(input_string)):
#         if reference_str != input_string[i]:
#             if end_point - start_point >= 1:
#                 if reference_str == '1':
#                     input_string[start_point:end_point+1] = ['0']*(end_point - start_point + 1)
#                 else:
#                     input_string[start_point:end_point+1] = ['1']*(end_point - start_point + 1)
#
#             start_point = i
#             end_point = i
#             reference_str = input_string[i]
#
#
#         #if reference_str == input_string[i]:
#         else:
#             end_point += 1
#
#
#     cnt += 1
#     # reference_str =
#
#
# print((cnt +1) // 2)
# -------------------------------------------------------------------------------- #