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