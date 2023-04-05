# 자주 사용되는 내장함수

# 평균
result= sum([1,2,3,4,5])


# 최대값 최소값
min_result= min(7,1,2,5)
max_result= max(7,1,2,5)


# string 식을 수 형태로 풀어줌
result= eval("(3+5)*7")

# 정렬
result= sorted([9,1,8,5,4], reverse=True)
array = [('홍길동', 35), ('이순신', 40), ('김선경', 32)]
# 정렬 조건
result = sorted(array, key=lambda x: x[1], reverse=False)

# 순열과 조합(경우의 수)
# 순열구하기
from itertools import permutations
data = ['A', 'B', 'C']
result= list(permutations(data, 3))
# 조합구하기
from itertools import combinations
result= list(combinations(data, 2))

# 중복 순열
from itertools import product
result= list(product(data, repeat= 2))   # 2개를 뽑는 모든 순열

# 중복 조합
from itertools import combinations_with_replacement
result= list(combinations_with_replacement(data, 2))

# 등장횟수 세기
from collections import Counter
counter= Counter(['red', 'blue', 'red','green'])
# 딕셔너리로 각각 횟수 센 항목 반환
dictionary= dict(counter)

# 최대공약수, 최소공배수
import math
# 최대공약수 계산
max_gcd= math.gcd(21, 14)
# 최소공배수 계산 (최대공약수로 두 수의 곱을 나눈 몫)
min_lcm= (21*14) // max_gcd

# 재귀함수로 구현한 팩토리얼 예제

def recusive_function(n):
    if n <= 1:
        return 1
    return n * recusive_function(n-1)

print(min_lcm)

## 소수란? 1보다 큰 자연수중에서 1과 자기 자신을 제외한 자연수로 나누어 떨어지지 않는 자연수
## 2부터 반복하면서 나누어지는 값이 있는지 모두 확인해줌
def is_prime_number(x):
    for i in range(2, x):
        if x % i ==0:
            return False
        return True
## 약수의 성질을 사용: 약수의 가운데 값을 기준으로 양 옆이 대칭을 이룬다는 것을 이용하여 간단하게 바꿀수 있음
## 해당 값 제곱근까지만 확인하면 됨

import math

def is_prime_number2(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
        return True


## 다수의 소수판별
## 특정 수의 범위 안에 존재하는 모든 소수를 찾아야할때 -> 에라토스테네스 체 알고리즘 사용
## 2~ N까지 자연수 나열, 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾음
## 남은 수 중에서 i의 배수를 모두 제거 (i는 제거하지 않음)
## 더이상 반복할 수 없을때까지 2,3번을 반복해줌

n= 1000
array= [True for i in range(n+1)]
def how_many_prime_number(n):
    for i in range(2, int(math.sqrt(n))+1):
        if array[i] == True:
            j =2
            while i * j <=n:
                array[i*j] = False
                j += 1

    for i in range(2, n+1):
        if array[i]:
            print(i, end=' ')

how_many_prime_number(n)


## 투 포인터 알고리즘: 리스트를 순차적으로 접근해야 할때 두개의 점의 위치를 기록하면서 처리하는 알고리즘
## 예시 1. 특정한 합을 가지는 부분 연속 수열 찾기(합이 m이 되도록 하는 경우의 수를 구하는 문제)

n= 5
m= 5
data=[1,2,3,2,5]

count=0
interval_sum=0
end=0

for start in range(n):
    while interval_sum< m and end<n:
        interval_sum += data[end]
        end += 1
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]
