# 선형 탐색 알고리즘이란 단방향으로 맨 앞부터 원하는 데이터를 찾아내는 단순한 구조의 탐색. 시간 오래걸림
# sorted 메소드 없이 작은값부터 배열을 정렬하는 문제를 선형적으로 풀어낼수있음

array=[1,5,7,3,9,6,4,8,2]

for i in range(len(array)):
    first_index= i
    for j in range(i+1, len(array)):
        if array[first_index] > array[j]:
            first_index = j
    array[i], array[first_index] =array[first_index],array[i]


print(array)

# 삽입 정렬 알고리즘
# 처리되지 않은 원소들의 위치를 적절한 위치를 찾아줌

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j], array[j-1]
        else:
            break

print(array)

# 퀵 정렬: 빠름. 기준 데이터를 고른 후 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꿔준다.
# 기본적으로 맨 첫번째 값을 기준 데이터(pivot)으로 설정하여 피벗을 기준으로 작은 값들은 왼쪽 파티션, 큰 값은 오른쪽 파티션으로 나뉘게 된다
# 이 과정을 재귀적으로 계속 현재 리스트의 값이 1개가 될때까지 반복한다.

array=[1,5,7,3,9,6,4,8,2]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot= start
    left= start+ 1
    right= end
    # 교차 되는 순간까지 반복
    while(left<= right):
        # 피벗보다 작은 데이터를 계속 찾음
        while(left<=end and array[left]<=array[pivot]):
            left += 1
        # 피벗보다 큰 데이터를 계속 찾음
        while(right>start and array[right] >= array[pivot]):
            right -= 1
        if(left > right):
            array[right], array[pivot]= array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


quick_sort(array, 0, len(array)-1)
print(array)

## 위의 퀵정렬을 파이썬의 장점을 살려서 리팩토링 (더 직관적인듯)
## array[:::] 문법은 extended slices 를 찾아볼것

array=[1,5,7,3,9,6,4,8,2]

def quick_sort2(array):
    if len(array) <=1 :
        return array
    pivot= array[0]
    tail= array[1:]

    left_side= [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)

print(quick_sort2(array))

# 계수 정렬(counting sort): 특정 조건이 부합할때만 사용할 수 있지만 매우 빠르게 동작함
# 특정 조건: 데이터 크기 범위가 제한되어 정수의 형태로 표현할 수 있을때 사용 가능함
# 배열을 만든 후 해당 데이터가 해당하는지 개수를 세어주는 방식임
# 하나의 값이 여러번 나올때, 길이가 정해져 있을때 효과적인 방식



array=[1,5,7,3,9,6,4,8,2,2,3,4,5,6,1,2,2,6,7,8,0]

def counting_sort(array):
    count= [0] * (max(array) +1)
    for i in range(len(array)):
        count[array[i]] += 1
    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=' ')

print(counting_sort(array))


# 순차 탐색:특정 데이터를 찾기위해 앞에서부터 데이터를 하나씩 확인함)
# 이진탐색(binary search)
# 정렬이 되어있는 리스트에서 탐색범위를 절반씩 좁혀가며 데이터를 탐색함
# 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정함

def binary_search(array, target, start, end):
    if start > end:
        return None
    middle= (start+end) // 2
    if array[middle] > target:
        return binary_search(array, target, start, middle -1)
    else:
        return binary_search(array, target, middle +1, end)


# 이진탐색 라이브러리 활용
# bisect_left(arr, target): arr의 정렬을 유지하면서 target이 들어갈 왼쪽 인덱스 자리를 찾아줌
# bisect_right(arr, target): arr의 정렬을 유지하면서 target이 들어갈 오른쪽 인덱스 자리를 찾아줌
from bisect import bisect_left, bisect_right
a= [1,2,4,4,8]
x= 4

print(bisect_left(a, x))
print(bisect_right(a, x))

# 이진탐색 라이브러리를 활용해 target의 원소가 몇개있는지 추출해낼 수 있음
def count_by_range(arr, left_value, right_value):
    left_idx=bisect_left(arr, left_value)
    right_idx= bisect_right(arr, right_value)
    return right_idx-left_idx

# 파라매트릭 서치: 최적화 문제를 결정의 문제로 바꾸어 해결하는 것 ex)특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제일경우
# --> 다음시간에..
