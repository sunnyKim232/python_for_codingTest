# 최단경로 알고리즘
## 한 지점에서 다른 지점까지의 최단 경로를 구하거나 한 지점에서 다른지점으로, 모든 지점에서 다른 모든지점으로까지의 최단경로를 구할때 쓰임

# 다익스트라 알고리즘
# 특정한 노드에서 출발하여 다른 모든 노드로가는 최단 경로를 계산함
# 그리디 알고리즘으로 분류됨 / 매 상황에서 가장 비용이 적은 노드를 선택해 임의의 과정을 반복함

## 동작 과정
## 1. 출발 노드를 선택함
## 2. 최단 거리 테이블을 초기화 함
## 3. 방문하지 않은 노드중에서 최단 거리가 가장 짧은 노드를 선택함
## 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신함
## 5. 위 3-4번의 과정을 반복함

## 테이블에 각 노드의 최단거리를 3-4번을 반복하여 갱신해주는 방법으로 구현 가능
## 매 단계마다 1차원 테이블의 모든 원소를 확인해주는 방법으로 구현

import sys
input = sys.stdin.readline
INF= int(1e9) # 무한을 의미하는 값으로 10억 설정

n, m= map(int, input().split())

start= int(input())

graph=[[] for i in range(n+1)]

visited=[False] * (n+1)

distance= [INF] * (n+1)


for _ in range(m):
    a, b, c = map(int, input().split())
    ## a번 노드에서 b로 가는 거리가 c라는 의미
    graph[a].append((b, c))

def get_smallest_node():
    min_value=INF;
    # 가장 최단거리가 짧은 노드(인덱스)
    index=0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
        return index

def dijkstra(start):
    # 시작노드 초기화
    distance[start]=0
    # 방문처리
    visited[start]= True

    for j in graph[start]:
        distance[j[0]]= j[1]
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost= distance[now]+ j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('INFINITY')
    else: print(distance[i])

