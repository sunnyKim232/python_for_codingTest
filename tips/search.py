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
        if(left >= right):
            array[right], array[pivot]= array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


quick_sort(array, 0, len(array) -1)
print(array)


