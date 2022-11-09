# d(n)은 n과 n의 각 자리수를 더하는 함수
# ex) d(75) = 75+7+5 = 87

# n은 d(n)의 생성자

# def selfNumber():
#     All = [x for x in range(1, 10001)]
#     dn = []
#     result = []
    
#     for i in All:
#         a = i//10000
#         b = (i - (a*1000))//100
#         c = (i - a*1000 - b*100)//10
#         d = i - a*1000 - b*100 - c*10
#         dn.append(i+a+b+c+d)
        
#     for j in All:
#         if j not in dn:
#             result.append(j)
            
#     for k in result:
#         print(k)
        
# selfNumber()

def selfNumber():
    dn = []
    allNum = []

    for i in range(10000):
        allNum.append(i)
        x = i+sum(map(int,str(i)))
        dn.append(x)
    
    result = list(set(allNum) - set(dn))
    result.sort()
    
    for k in result:
        print(k)
        
selfNumber()