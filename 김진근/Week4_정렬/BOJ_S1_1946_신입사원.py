import sys
input = sys.stdin.readline # 빠른 입력
print = sys.stdout.write # 빠른 출력, 출력은 반드시 문자열로

# 일단 서류 기준으로 정렬하고
# 서류 1등은 반드시 뽑히게 되므로, 그다음 사람의 면접 점수비교
"""
1 4 뽑
2 5 4<5 안뽑
3 6 4<6 안뽑
4 2 4<2 뽑
5 7 2<7 안뽑
6 1 2<1 뽑
7 3 1<3 안뽑
"""

T = int(input()) #테스트 케이스
for _ in range(T):
    N = int(input())
    cnt = 1 #1등 한명은 반드시 채용
    member =[]
    for _ in range(N):
        member.append(list(map(int, input().split()))) #입력

    member.sort(key=lambda x:x[0]) #앞에꺼 기준 오름차준 정렬

    best_score = member[0][1] #1등성적

    for i in range(1, N):
        if member[i][1] < best_score:
            cnt += 1
            best_score = member[i][1]

    print(str(cnt) + '\n')


