n = int(input())
sum = []

for i in range(n):
    a,b = map(int, input().split())
    sum.append(a+b)
    
for i in range(n):
    print(sum[i])
    
# n=int(input())
# for i in range(1,n+1):
#     a,b=map(int,input().split())
#     print(a+b)
