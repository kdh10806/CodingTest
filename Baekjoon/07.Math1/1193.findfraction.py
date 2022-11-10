# 45도 돌려서 보면 같은 층 분모와 분자의 합이 같다.

N = int(input())
i = 1

while N-i>0:
    N-=i
    i+=1
    
if i%2==0:
    print(f'{N}/{i-N+1}')
else:
    print(f'{i-N+1}/{N}')