# OX 퀴즈, 맞힌 O가 연속될수록 점수 +1

N = int(input())

for i in range(N):
    score = 0
    bonus = 0
    case = list(input())
    
    for i in case:
        if i == 'O':
            bonus+=1
            score+=bonus
        else:
            bonus=0
    print(score)