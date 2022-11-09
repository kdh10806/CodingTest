# 양의 정수 X의 각 자리가 등차수열을 이루면 그 수를 한수라고 한다.
# N이 주어졌을 때(1<= x <= N) 갯수를 구하라



def Han():
    N = int(input())
    hansu = 0
    
    for i in range(1, N+1):
        if i <= 99:
            hansu+=1

        else:
            num = list(map(int, str(i)))
            if num[0]-num[1] == num[1] - num[2] :
                hansu+=1
    print(hansu)            

Han()