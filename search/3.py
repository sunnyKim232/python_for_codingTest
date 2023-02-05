## N개의 길이인 배열 A와 B가 주어졌을때  최대 M번까지 배열 A가 가장 최대값이 되도록 B의 원소와 바꾸는 알고리즘을 작성하시오

## 그냥 먼저 풀기
n, m= map(int, input().split())

arr1= list(map(int, input().split()))
arr2= list(map(int, input().split()))


for i in range(m):
    arr1min=min(arr1)
    arr2max=max(arr2)
    if arr1min >=arr2max:
        break
    index1 = arr1.index(arr1min)
    index2=arr2.index(arr2max)
    arr1[index1], arr2[index2]= arr2max, arr1min


print(sum(arr1))

## 정답
## 배열의 순서를 정한후 만약 b배열이 더 크면 바꿔줌
## 이를 m만큼만 반복
arr1.sort()
arr2.sort(reverse=True)

for i in range(m):
    if arr1[i] <arr2[i]:
        arr1[i], arr2[i] = arr2[i], arr1[i]
    else:
        break



