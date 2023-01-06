# n * n 크기의 정사각형 지도가 있을때 여행자가 (1,1)에서 계획서대로 이동할경우 최종 도착지가 어디인지 구하라
# 계획서는 R: 오른쪽으로 이동 L: 왼쪽으로 이동 U: 위로 이동 D: 아래로 이동 의 방향이 주어진다.
from collections import Counter
n=input()
plan= list(map(str, input().split()))

counter= Counter(plan)
x, y= (1, 1);
nx=0
ny=0

for i in range(len(plan)):
    if plan[i]== 'L':
        nx= x - 1
    elif plan[i] == 'R':
        nx = x +1
    elif plan[i] == 'U':
        ny = y -1
    elif plan[i] == 'D':
        ny = y + 1


print(nx, ny)

