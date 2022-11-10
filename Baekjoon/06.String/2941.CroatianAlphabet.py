croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

S = input()

for i in croatian:
    S = S.replace(i, '1')
    print(S)
    
print(len(S))