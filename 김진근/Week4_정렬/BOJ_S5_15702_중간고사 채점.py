import sys
input = sys.stdin.readline # 빠른 입력
print = sys.stdout.write # 빠른 출력, 출력은 반드시 문자열로

N,M = map(int,input().split())      #N 문제갯수, M 응시자수
score = list(map(int,input().split()))

max_score = -1
max_student = -1
for i in range(M):
    tmp = list(input().split())
    tmp_score = 0
    for j in range(1,N+1):
        if tmp[j] == 'O': #맞춘문제
            tmp_score += int(score[j-1])

    if max_score < tmp_score:
        max_score = tmp_score
        max_student = tmp[0]
    elif max_score == tmp_score:
        max_student = min(int(max_student), int(tmp[0]))

print(str(max_student) + " " + str(max_score))

