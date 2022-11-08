# 9개의 서로 다른 자연수가 주어질때 이들 중 최댓값을 찾고 그 최댓값이 몇번째 수인지 구하라

A = []

for i in range(9):
    x = int(input())
    A.append(x)
    
max1 = max(A)
index1 = A.index(max1)
print(max1)
print(index1+1)