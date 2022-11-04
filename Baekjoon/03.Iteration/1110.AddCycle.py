num = int(input())

a = num//10
b = num%10
c = (a+b)%10
num1 = 10*b+c
count = 1

while(num!=num1):
    a = num1//10
    b = num1%10
    c = (a+b)%10
    num1 = 10*b+c
    count+=1
print(count)