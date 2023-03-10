## 개선방법: 딘계마다 방문하지 않은 노드중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 힙 자료구조를 사용함
## 우선순위 큐를 거리, 노드값을 차례대로 저장해주는데 동일하게 차례대로 방문할 수 있는 노드를 방문하면서 거쳐갈때의 값이 더 작다면 갱신되도록함
import heapq
import sys
input = sys.stdin.readline
INF= int(1e9) # 무한을 의미하는 값으로 10억 설정

# 노드의 갯수와 간선의 개수를 입력받음
n, m= map(int, input().split())

# 시작노드 번호
start= int(input())

# 2중 리스트로 노드의 정보를 받을 리스트를 만듬
graph=[[] for i in range(n+1)]


# 최단 거리를 저장해줄 리스트, 모두 무한으로 초기화하여 만들어 둠
distance= [INF] * (n+1)

# 간선 정보를 입력해줌
for _ in range(m):
    a, b, c = map(int, input().split())
    ## a번 노드에서 b로 가는 거리가 c라는 의미
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

## q가 비어있지 않는동안 반복
    while q:
        # 가장 가까운 거리응 뽑아줌
        dist, now = heapq.heappop(q)
        # 민약 거리가 더 길다면 = 처리되기 전의 노드임
        if distance[now] < dist:
            continue
        ## 가장 기까운 거리의 노드의 값을 꺼내서,
        for i in graph[now]:
            ## 거쳐서 갈 경우(기존 dist 값이 존재하는 경우)의 비용을 구해준 후
            cost= dist + i[1]
            ## 만약 그 값이 더 작을 경우에만 힙에 저장되어있는 q의 값을 갱신해줌 (최소값으로 저장됨)
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('INFINITY')
    else: print(distance[i])
