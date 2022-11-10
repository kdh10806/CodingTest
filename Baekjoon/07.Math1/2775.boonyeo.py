# a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와야한다.
# 정수 k와 n에 대해  k층에 n호에는 몇명이 살고 있는가?

#아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때,
# 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라.
# 단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.

T = int(input())
for i in range(T):
    floor = int(input())
    room = int(input())
    people = [j for j in range(1, room+1)]
    
    for k in range(floor):
        for v in range(room-1):
            people[v+1] += people[v]
    print(people[-1])
    
# 파스칼의 삼각형 활용
# import math
# i = lambda:int(input())

# exec('k,n=i(), i();print(math.comb(k+n,k+1));'*i())