# 세자리수 곱셈
# 첫째 줄에 세자리 자연수 둘째 줄에 세자리 자연수가 주어진다
# 3번에 첫 세자리 자연수 X 두번째 세자리 자연수의 1의 자리
# 4번에 첫 세자리 자연수 X 두번째 세자리 자연수의 10의 자리
# 5번에 첫 세자리 자연수 X 두번째 세자리 자연수의 100의 자리
# 6번에 곱셈 결과

a = int(input())
b = int(input())

print(a*(b%10))
print(a*((b//10)%10))
print(a*(b//100))
print(a*b)

# a=int(input())
# b=input()

# print(a*int(b[2]))
# print(a*int(b[1]))
# print(a*int(b[0]))
# print(a*int(b))