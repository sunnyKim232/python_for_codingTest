# 미로탈출
# [1,1] 위치에서 주어지는 출구의 위치 [n,m] 까지 가는 최소의 움직임을 구하시오

from collections import deque


n, m= map(int, input().split())

# 2차원리스트 형태로 받아줌
graph=[]
for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우로 움직일 수 있도록함
dx= [-1, 1, 0, 0]
dy= [0, 0, -1, 1]

def bfs(x, y):
    queue= deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        # 상하좌우로 돌면서 1이 있는곳을 찾아줌
        for i in range(4):
            nx = x + dx[i]
            ny = y+ dy[i]
            # 범위를 벗어날경우 건너 뛰기
            if nx< 0 or nx>= n or ny < 0 or ny>= m:
                continue
            # 만약 0인경우 건너 뛰기
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]== 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]

print(bfs(0,0))