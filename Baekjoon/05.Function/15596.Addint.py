# 정수 n개가 주어졌을때 n개의 합을 구하라
# solve라는 함수를 만들고 a라는 list를 인자로 받는다.

def solve(a):
    result = 0
    for i in a:
        result+=i
    return result

a = [1,2,3,4,5]

solve(a)