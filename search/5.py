# 떡볶이 떡 만들기
# 떡의 갯수 N, 요청한 떡의 길이 M이 주어지는데 이때
# N개의 갯수만큼 떡이 주워지는데 이 떡의 갯수는 일정하지 않아
# H의 길이만큼 잘라내는데 이때 나머지 떡의 길이가 손님이 요청한 떡의 길이 N만큼 나오려면
# H의 길이는 최대 얼마여야하는지 구하는 문제

## 일단 풀기
n, m= list(map(int, input().split()))
arr= list(map(int, input().split()))
# result=[]
# for i in range(1, max(arr)+1):
#     answer=0
#     for item in arr:
#         temp= item-i
#         if temp > 0:
#             answer += item- i
#     if answer >= int(m):
#         result.append(i)
#
# print(max(result))

## 정답
## 적절한 높이를 찾을때까지 h를 반복하며 조정하는 것
## 이진탐색으로 해결
## 시작점을 가장 긴 값의 중간점을 지정하여 얻을 수 있는 떡의 합을 지속적으로 구해주는것

start= 0
end= max(arr)

result= 0
while(start <= end):
    total =0
    mid= (start+ end) //2
    for x in arr:
        if x> mid:
            total += x-mid
    if total < m:
        end= mid -1
    else:
        result = mid
        start = mid+1

print(result)