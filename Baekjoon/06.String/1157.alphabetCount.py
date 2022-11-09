word = input().upper()
result = []

comp = list(set(word))

for i in comp:
    result.append(word.count(i))

if result.count(max(result)) > 1:
    print("?")
else:
    print(comp[result.index(max(result))])