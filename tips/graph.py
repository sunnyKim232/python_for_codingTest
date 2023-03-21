## 서로소 집합: 공통 원소가 없는 두 집합
# 서로소 집합 자료구조: 서로소 집합들로 이루어진 원소들을 처리하기 위한 자료구조(트리구조)
# 합집합(하나의 집합으로 합치는 연산), 찾기(특정한 원소가 속한 집합이 어떤 집합인지 알려줌) 연산을 지원
# 루트를 재귀적으로 부모를 거슬러 올라가는 연산을 통해 집합이 어떻게 나뉘어있는지 확인할 수 있음

def find_parent(parent, x):
    ## 루트노드가 값과 같다 => 즉 자신이 루트노드인 것
    ## 루트노드가 나올때까지 반복해줌
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두원소가 속한 집합을 합치기
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

# 자기 자신으로 부모 초기화
for i in parent(1, v+1):
    parent[i]= i

## union 연산 수행
for i in range(e):
    a, b= map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합', end=' ')
for i in range(i, v+1):
    print(find_parent(parent, i), end=' ')

print()

print('부모 테이블: ', end=' ')
for i in range(1, v+1):
    print(parent[i], end=' ')


#find_parent 함수는 최악의경우 모든 노드를 다 확인해야하는 경우가 생길 수도 있음 -> 비효율적
## 경로압축기법: 찾기함수를 최적화, 부모함수를 재귀적으로 호출하되 부모 테이블 값을 바로 갱신함
def find_parent2(parent, x):
    # 루트 노드가 아니라면 루트 노드를 찾을때까지 재귀적으로 호출
    if parent[x] != x:
         parent[x]=find_parent2(parent, parent[x])
    return parent[x]

# 무방향 사이클 판별 알고리즘: 무방향 그래프 내에서의 사이클을 판별할때 사용
## 각 간선을 하나씩 확인하면서 두 노드의 루트 노드를 확인 -> 같다면 사이클 발생, 다르다면 합집합 연산수행


# 신장트리: 그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프를 의미
## 모든 노드가 포함되어 연결되면서 사이클이 존재하지않는다 = 트리의 조건

