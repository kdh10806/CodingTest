# 정수 N개로 이루어진 수열A와 정수X가 주어진다.
# 이때, A에서 X보다 작은 수를 모두 출력하라

n, x = map(int, input().split())

A = list(map(int, input().split()))

for i in range(len(A)):
    if A[i]<x :
        print(A[i])
