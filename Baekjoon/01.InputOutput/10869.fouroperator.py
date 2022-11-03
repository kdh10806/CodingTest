#첫 줄에 두 자연수 A와 B를 입력받음(1<=A, B<=10000)
#A+B, A-B, A*B, A/B(몫), A%B(나머지)를 구하라.

a,b = map(int, input("A와 B를 입력하세요(ex : 1 2) : ").split())

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)