# 교실엔 1번부터 30번까지 학생이 있다.
# 28명이 과제를 제출했는데 제출 안 한 학생 2명의 출석번호를 구하라

# 입력은 총 28줄로 각 학생의 출석번호가 한 불에 하나씩 주어진다.
class1 = []

for i in range(28):
    x = int(input())
    class1.append(x)
    
for j in range(1,31):
    if j not in class1:
        print(j)