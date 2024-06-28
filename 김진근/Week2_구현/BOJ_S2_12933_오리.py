import sys
input = sys.stdin.readline # 빠른 입력
print = sys.stdout.write # 빠른 출력, 출력은 반드시 문자열로

duck = input().rstrip()
word = ['q', 'u', 'a', 'c', 'k']        # 오리울음소리는 quack고정

# 조건1 오리울음소리는 무조건 5개이므로 5의 배수가 아니라면 오리의 울음소리가 아니다.
if len(duck) % 5 != 0:
    print(str(-1) + "\n")
else:
    visited = [False] * len(duck)   #방문 여부-> quack의 방문여부 , 최대 울음 소리만큼
    cnt = 0 #오리의 수

    for a in range(len(duck)):
        if duck[a] == 'q' and not visited[a]: #처음시작
            first = True
            index = 0
            for i in range(len(duck)):
                if word[index] == duck[i] and not visited[i]: #'q' 이면서 방문하지 않았을때
                    visited[i] = True # 방문
                    if duck[i] == 'k':  #끝 조건
                        if first:   #시작 -> 끝
                            cnt += 1    #1마리 찾음
                            first = False
                        index = 0   #다시 0부터
                        continue
                    index += 1 #다음 울음소리찾기

    if cnt == 0 or not all(visited):
        print(str(-1) + "\n")
    else:
        print(str(cnt) + "\n")
