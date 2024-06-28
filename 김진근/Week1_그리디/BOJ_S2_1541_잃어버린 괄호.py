import sys
input = sys.stdin.readline # 빠른 입력
print = sys.stdout.write # 빠른 출력, 출력은 반드시 문자열로

inValue = input().split('-') # - 기준으로 먼저 나누기
ans =0

for i in inValue[0].split('+'): # -기준으로 나눈부분을 +가 있을때 다시 쪼개서 값을 더하라
    ans += int(i)

for i in inValue[1:]:   # - 기준으로 쪼갠 부분 부분들
    for j in i.split('+'):  # 뒤에꺼 하나씩 빼주기
        ans -= int(j)

print(str(ans))
