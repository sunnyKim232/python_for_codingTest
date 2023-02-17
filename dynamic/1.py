# 1로 만들기
# 주어진 정수 x가 다음 3가지 연산을 통해 1을 만들려고 한다.
# 1. x가 5로 나누어 떨어지면 5로 나눈다. 2. x가 3으로 나누어 떨어지면 3으로 나눈다. 3. x가 2로 나누어 떨어지면 2로 나눈다. 4. x에서 1을 뺀다.
# 연산의 최소값을 구하시오


## 먼저풀기
# x= int(input())
#
# d= [0] * 100
#
# d[0] = x
#
#
# for i in range(1, x):
#     if d[i]== 1:
#         break
#     if d[i] % 5 !=0 or d[i] % 3 !=0 or d[i] % 2 !=0:
#         d[i] = d[i-1] -1
#         break
#     else:
#         if d[i] % 5 ==0:
#             d[i] = d[i - 1] // 5
#         elif d[i] % 3 ==0:
#             d[i] = d[i - 1] // 3
#         elif d[i] % 2 ==0:
#             d[i] = d[i - 1] // 2
#
# print(d)


## 정답
x= int(input())
d= [0] * 50

for i in range(2, x+1):
    d[i]= d[i-1] +1
    if i % 2 ==0:
        d[i] = min(d[i], d[ i//2] +1)
    if i % 3==0:
        d[i] = min(d[i], d[ i//3] +1)
    if i % 5==0:
        d[i] = min(d[i], d[ i//5] +1)


print(d[x])