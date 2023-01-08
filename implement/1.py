# n * n 크기의 정사각형 지도가 있을때 여행자가 (1,1)에서 계획서대로 이동할경우 최종 도착지가 어디인지 구하라
# 계획서는 R: 오른쪽으로 이동 L: 왼쪽으로 이동 U: 위로 이동 D: 아래로 이동 의 방향이 주어진다.

n=int(input())
plan= list(map(str, input().split()))

x, y= 1, 1
dx = [0, 0, -1, 1]
dy=[-1, 1, 0, 0]
type=['L', 'R', 'U', 'D']

for i in plan:
    for j in range(len(type)):

        if i == type[j]:
            nx = x+ dx[j]
            ny = y+ dy[j]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y= nx, ny



print(nx, ny)

