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

# 노드의 갯수와 간선의 개수를 입력받음
n, m= map(int, input().split())

# 시작노드 번호
start= int(input())

# 2중 리스트로 노드의 정보를 받을 리스트를 만듬
graph=[[] for i in range(n+1)]

# 방문 여부를 저장해줄 리스트
visited=[False] * (n+1)

# 최단 거리를 저장해줄 리스트, 모두 무한으로 초기화하여 만들어 둠
distance= [INF] * (n+1)

# 간선 정보를 입력해줌
for _ in range(m):
    a, b, c = map(int, input().split())
    ## a번 노드에서 b로 가는 거리가 c라는 의미
    graph[a].append((b, c))

## 방문하지 않은 노드 중에서 가장 가까운 거리에 있는 노드를 찾아서 반환해줌
def get_smallest_node():
    min_value=INF
    # 인덱스를 반환해줄 것임
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

    ## graph 에 저장해둔 거리 정보로 distance 리스트에 저장해준다
    for j in graph[start]:
        distance[j[0]]= j[1]

    ## 모든 노드를 확인해줄것, 시작 노드만 제외하고
    for i in range(n-1):
        # 시작노드부터 가장 가까운 인덱스(노드)를 찾아서 처리해줄 것임
        now = get_smallest_node()
        # 가장 가까운 노드 방문
        visited[now] = True
        for j in graph[now]:
            ## 처리중인 노드 now가 가지는 거리 + now에서 방문 가능한 노드를 방문하는데에 거리를 더해주는 값이
            cost= distance[now]+ j[1]
            ## 기존에 존재하는 now에서 방문가능한 노드의 비용보다 작다면 (더 가깝다면)
            if cost < distance[j[0]]:
                ## 해당 cost 값으로 distance 를 업데이트 해준다.
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('INFINITY')
    else: print(distance[i])

## 이 과정은 전체 노드가 5천개 이하일때 문제를 해결할 수있으나 개수가 만개를 넘어갈때는 시작복잡도가 높아지므로
## 우선순위 큐 자료구조로 해결할 수 있다.
## 어떨때 ? 여러개의 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건 데이터부터 꺼내서 확인해야할 때 ** (가장 우선순위가 높은 데이터부터 추출됨)

## 개선방법: 딘계마다 방문하지 않은 노드중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 힙 자료구조를 사용함