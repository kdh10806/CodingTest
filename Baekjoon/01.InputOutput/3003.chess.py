# 체스는 총 16개 피스
# 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
# 첫 줄에 킹, 퀸, 룩, 비숍, 나이트, 폰의 갯수가 주어진다. (0<= x <=10)
# 몇개의 피스가 더해지거나 빼져야 하는지 출력하라

a,b,c,d,e,f = map(int, input().split())

print(1-a, 1-b, 2-c, 2-d, 2-e, 8-f)