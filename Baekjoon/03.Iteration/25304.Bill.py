total = int(input())
type = int(input())
sum = 0

for i in range(type):
    price, amount = map(int, input().split())
    sum = sum+(price*amount)
    
if sum==total:
    print("Yes")
else:
    print("No")