N = int(input())
A = input()

a = str(A)
sum = 0

for i in range(N):
    sum += int(a[i])
    
print(sum)