t,m = map(int, input().split())

m = m-45
if(m<0):
    m = 60+m
    t = t-1
    if(t<0):
        t = 24+t;

print(t, m)