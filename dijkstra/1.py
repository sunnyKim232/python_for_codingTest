## 미래도시
## 1에 있는 사람이 n개의 도시가 주워졌을때, 1번 도시 -> k도시 -> x도시로 이동하는 최단거리를 구해라
## 모든 거리는 m개 이며 모두 1로 도시가 연결 되어 있음

n, m= map(int, input().split())
INF=int(1e9)
graph= [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b]= 0


for _ in range(m):
    a, b= map(int, input().split())
    ## 거리는 무조건 1
    graph[a][b]=1
    graph[b][a]=1

x, k= map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            ## 거리를 갱신해줌 = 현재값보다 a->k(현재확인노드)를 거쳐 K->b로 가는 것이 더 짧은지 아닌지 확인해줌
            graph[a][b]= min(graph[a][b], graph[a][k]+ graph[k][b])

distance= graph[1][k] + graph[k][x]

if distance >= INF:
    print('갈수 없는 거리임')
else: print(distance)