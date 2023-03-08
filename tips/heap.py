
# 우선순위 큐를 구현할때 사용하는 자료구조 : 최소 힙 / 최대 힙
## logN만큼의 시간복잡도가 소요됨

## 최소 힙 구현
import heapq

def heapsort(iterable):
    h=[]
    result= []
    for value in iterable:
        ## 차례대로 원소가 들어감
        heapq.heappush(h, value)
    for i in range(len(h)):
        ## 차례대로 원소가 나옴
        result.append(heapq.heappop(h))
    return result


result =heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

## 최대 힙 구현
def maxheapsort(iterable):
    h = []
    result = []
    ## 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result =maxheapsort([1,3,5,7,9,2,4,6,8,0])
print(result)