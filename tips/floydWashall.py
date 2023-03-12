## 모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산할때 사용함
## 단계별로 거처가는 노드를 기준으로 알고리즘을 수행
## 플로이드 워셜은 2차원 테이블에 최단경로정보를 저장해줌 - 다이나믹 알고리즘에 속함.

## 각 단계마다 특정한 노드 K를 거쳐가는 경우를 확인하여 a-b로 가는것보다 a-k-b의 거리가 더 짧은지 검사해줌

INF=int(1e9)  # 무한 표기

## 노드의 개수 및 간선의 개수를 입력받기
n= int(input())
m= int(input())

## 2차원 리스트를 무한으로 표기해서 저장해줌
graph= [[INF] * (n-1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b]= 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화 해줌
for _ in range(m):
    a, b, c= map(int, input().split())
    # a에서 b로 가는 비용은 c라고 설정
    # 거쳐서 가지 않고 바로 접근할 수 있는 노드들의 정보만을 입력해줌
    graph[a][b]=c

# 거쳐서 가는 경우를 3중 for문을 이용하여 수행해줌
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            ## 거리를 갱신해줌 = 현재값보다 a->k(현재확인노드)를 거쳐 K->b로 가는 것이 더 짧은지 아닌지 확인해줌
            graph[a][b]= min(graph[a][b], graph[a][k]+ graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print('INFINITY', end=' ')
        else:
            print(graph[a][b], end=' ')
    print()