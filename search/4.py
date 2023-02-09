# 부품찾기
# N개의 부품 배열이 주어지는데, 그중 손님이 M개 배열을 주문하였을때 해당 부품이 있는지 없는지 확인하시오

from bisect import bisect_left, bisect_right

n= int(input())
products= list(map(int, input().split()))


m= int(input())
order= list(map(int, input().split()))


sorted(products)
sorted(order)


# for i in order:
#     left= bisect_left(products, i)
#     right= bisect_right(products, i)
#     if (right - left) == 0:
#         print(i, 'yes')
#     else: print(i, 'no')


## 정답

def binary_search(array, target, start, end):
    while start <= end:
        mid= (start + end) //2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid +1
    return None

for i in order:
    result= binary_search(products, i, 0, n-1)
    if result != None:
        print('yes', end='')
    else:
        print('no', end='')


## 더 간단하게

for i in order:
    if i in products:
        print('yes', end=' ')
    else:
        print('no', end=' ')