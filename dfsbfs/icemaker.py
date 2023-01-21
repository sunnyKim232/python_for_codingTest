# 세로길이 N * 가로길이 M 이 주어졌을때 구멍이 뚫려있는부분은 0, 아닌부분은 1로 표시되는데
# 구멍이 뚫려있는 부분끼리 상하좌우 모두 연결된것으로 간주하여 총 구해지는 아이스크림의 갯수를 구하라
# 연결요소 찾기 문제라고 볼수있음
# 0인 노드를 찾아서 해당 노드에 상하좌우로 연결된 노드를 방문하면서 0일경우를 찾아서 방문처리를 모두 해주는 dfs 방식으로 재귀적으로 계속 호출해준다.

n, m= map(int, input().split())

# 2차원리스트 형태로 받아줌
graph=[]
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    # 값이 범위를 벗어날경우 false처리해줌
    if x <= -1 or x>=n or y<=-1 or y>=m:
        return False
    ## 방문처리하기 전의 노드
    if graph[x][y]== 0:
        ## 방문처리
        graph[x][y] = 1
        # 해당 노드랑 연결된 상하좌우의 노드들까지 0인지 확인해주러 감
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x +1, y)
        dfs(x, y+1)
        return True
    return False

# n * m 배열을 돌면서 0인 곳을 찾아서 함수에 넣어주기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j)== True:
            result += 1

print(result)