# 값 10개를 받고 이를 42로 나눈 나머지를 구한다.
# 그 다음 서로 다른 값이 몇개 있는지를 출력하라

A = []
for i in range(10):
    x = int(input())
    x = x%42
    A.append(x)

B = set(A)
print(len(B))