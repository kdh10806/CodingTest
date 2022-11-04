# TimeOver
# n = int(input())

# for i in range(1, n+1):
#     a, b = map(int, input().split())
#     print(a+b)

import sys

read = lambda: sys.stdin.readline().rstrip()

n = int(read())

for i in range(n):
    a, b = map(int, read().split())
    print(a+b)