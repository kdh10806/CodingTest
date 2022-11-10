N = int(input())
count = 0
new = []

for i in range(N):
    S = input()
    for j in range(len(S)-1):
        if S[j] != S[j+1]:
            new = S[j+1:]
            if S[j] in new:
                count -= 1
                break
    count+=1

print(count)