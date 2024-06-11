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
