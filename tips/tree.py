# 최소 신장 트리: 최소한의 비용으로 구성도는 신장 트리를 찾아야할때
## 크루스칼 알고리즘: 대표적인 최소신장트리 알고리즘
## 1. 간선 데이터를 비용에 따라 오름 차순으로 정렬
## 2. 간선을 하나씩 확인하며 현재 간선이 사이클을 발생시키는지 확인함 -> 사이클이 발생할 경우 포함x

def find_parent(parent, x):
    # 루트 노드가 아니라면 루트 노드를 찾을때까지 재귀적으로 호출
    if parent[x] != x:
         parent[x]=find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a= find_parent(parent, a)
    b= find_parent(parent, b)
    if a< b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선의 개수입력받기
v, e= map(int, input().split())
# 부모 테이블
parent = [0] * (v+1)

# 모든 간선을 담을 리스트, 최종값 변수
edges= []
result= 0

# 자기 자신으로 부모 초기화
for i in parent(1, v+1):
    parent[i]= i

for _ in range(e):
    a, b, cost= map(int, input().split())
    edges.append((cost, a, b))

# 비용순으로 정렬
edges.sort()

for edge in edges:
    cost, a, b= edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost