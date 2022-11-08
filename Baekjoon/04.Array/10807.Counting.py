# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하라.

# 정수의 갯수
n = int(input())

# 정수 입력, 배열에 삽입
A = list(map(int, input().split()))

# 찾을 v 입력
v = int(input())

print(A.count(v))

