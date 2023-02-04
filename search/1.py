# 주어진 수 N개를 큰수에서 작은수의 순서로 정렬하시오

n= int(input())
array= []
for i in range(n):
    array.append(int(input()))

arrSorted= sorted(array, reverse=True)
print(arrSorted)