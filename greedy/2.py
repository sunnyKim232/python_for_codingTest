# 숫자 카드 게임
# n * m의 수를 받아서 n행 m열의 카드를 나열한다
# 각 행마다 작은 수를 뽑아 그 중 가장 큰 수를 뽑아주는 알고리즘문제

# 먼저 풀기
n, m = map(int, input().split())
#
# array= []
# minArr= []
#
# for i in range(n):
#     item = list(map(int, input().split()))
#     array.append(item)
#     array[i].sort()
#     min = array[i][0]
#     minArr.append(min)
#
# result= minArr[n-1];
#
#
# print(result)


## 정답
# min, max 함수 이용하기

result= 0
for i in range(n):
    item = list(map(int, input().split()))
    minValue = min(item)
    result = max(result, minValue)

print(result)
