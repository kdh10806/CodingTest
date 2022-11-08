# 점수 중 최대값 M
# 모든 점수를 점수/M*100 했다.

N = int(input())

score = list(map(int, input().split()))
max_score = max(score)

for i in range(N):
    score[i] = score[i]/max_score*100

print(sum(score)/N)
    