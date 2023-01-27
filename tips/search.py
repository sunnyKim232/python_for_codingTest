# 선형 탐색 알고리즘이란 단방향으로 맨 앞부터 원하는 데이터를 찾아내는 단순한 구조의 탐색. 시간 오래걸림
# sorted 메소드 없이 작은값부터 배열을 정렬하는 문제를 선형적으로 풀어낼수있음

array=[1,5,7,3,9,7,6,4,8,2]

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
