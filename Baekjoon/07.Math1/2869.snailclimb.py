#V < Ax-Bx
#V/x < A-B

# x = (V-B)/(A-B) 혹은 x= (V-B)/(A-B) +1 (분수일은 없기때문)

A, B, V = map(int, input().split())

x = (V-B)/(A-B)
print(int(x) if x == int(x) else int(x) +1)

if x == int(x):
    print(int(x))
else:
    print(int(x)+1)