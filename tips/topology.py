## 위상 정렬 알고리즘
## 사이클이 없는 방향그래프의 모든 노드를 방향성에 거슬리지 않도록 순서대로 나열(큐를 이용)
## 1. 진입차수가 0인 모든 노드를 큐에 넣는다.
## 2. 큐가 빌때까지 다음의 과정을 반복한다.
## 2-1) 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거함 2-2) 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
## -> 각 노드가 큐에 들어온 순서가 정렬을 수행한것과 같은 결과

## 한 단계에서 큐에 새롭게 들어가는 원소가 2개 이상인 경우가 있다면 여러가지 답이 존재함
## 만약 모든 원소를 방문하기 전에 큐가 빈부분이 있다면 사이클이 존재하는 것

from collections import deque

# 노드의 개수와 간선의 개수
v, e= map(int, input().split())

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree= [0] * (v+1)

# 각 노드에 연결된 간선정보를 담기 위한 연결 리스트
graph= [[] for i in range(v+1)]

# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a, b= map(int, input().split())
    graph[a].append(b) # a-> b로 이동가능
    # 진입차수 추가
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result=[]
    ## 큐 리스트 초기화 해둠
    q=deque()

    for i in range(1, v+1):
        ## 맨 처음 진입차수가 0인 것을 넣어줌
        if indegree[i] ==0:
            q.append(i)
        ## 큐가 빌때까지 반복
    while q:
        ## 현재 보고있는 노드를 꺼내서
        now= q.popleft()
        ## 결과값에 먼저 넣어주고
        result.append(now)
          ## 현재 노드와 연결된 노드를 찾아서
        for i in graph[now]:
              ## 간선 삭제
            indegree[i] -= 1
             ## 만약 삭제해준 후에 간선이 0이라면
            if indegree[i] == 0:
                q.append(i)
    for i in result:
        print(i, end=' ')

topology_sort()