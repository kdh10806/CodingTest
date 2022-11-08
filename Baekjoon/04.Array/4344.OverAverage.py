# 테스트케이스 수 C
# 테스트 케이스 마다 학생수 N이 첫 수로 주어지고 이어서 N명의 점수가 주어진다.
# 각 케이스마다 한줄씩 평균을 넘는 학생의 비율을 소숫점 셋째 자리까지 출력한다.

C = int(input())

for i in range(C):
    case = list(map(int, input().split()))
    avg = sum(case[1:])/case[0]
    cnt = 0
    
    for i in case[1:]:
        if i > avg:
            cnt+=1
    ratio = cnt/case[0]*100
    
    print(f'{ratio:.3f}%')