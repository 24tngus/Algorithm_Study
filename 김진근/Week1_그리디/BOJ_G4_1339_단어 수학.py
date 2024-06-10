# AAA + AAA = 100A+10A+1A    + 100A + 10A + 1A = 로 222A A가 제일크니까 9라고생각하고
# GCF + ACDEB = 100G+10C+1F + 10000A+1000C+100D+10E+1B = 10000A + 1B + 1010C + 100D +10E +1F + 100G
# => 10000 * 9 + 1010 * 8 + 100* 7 + 100 * 6 + 10*5 + 1*4 + 1*3 =

import sys
input = sys.stdin.readline #빠른 입력
print = sys.stdout.write #빠른 출력 출력은 반드시 문자열로

n = int(input())
ans = 0
word_dict = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
# 단어 먼저 딕셔너리 형태로 만들어 놓기
word_list = []

for i in range(n):
    word_list.append(input().strip())

for word in word_list:
    for i in range(len(word)): # 10^0 , 10^1  -> 3이라면 10**2 10**1 10**0 앞에서부터
        val = 10 ** (len(word)-i-1)
        word_dict[word[i]] += val


filtered_word_dict = {key: value for key, value in word_dict.items() if value != 0} #0인 값들은 제외

#반환값 배열
sorted_dict = sorted(filtered_word_dict.items(), key=lambda x: x[1], reverse=True) # 값을 기준으로 내림차순 정렬

for i in range (len(sorted_dict)):
    ans += sorted_dict[i][1] * (9-i)

print(str(ans))
