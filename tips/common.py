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