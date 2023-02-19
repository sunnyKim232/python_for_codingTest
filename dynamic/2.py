## 개미전사
# 개미가 메뚜기 마을의 식량창고를 털러갈건데 나란히있는 창고를 털게 되면 들킴
# 들키지 않고 털수있는 가장 최대한의 식량을 구하시고
# n = 식량 창고의 갯수 / list= 각 창고에 저장된 식량 크기들이 주어짐

## 개어렵..

# 현재 위치를 i라고 했을 경우 (i-1)은 털수 없음, (i-2)일 경우에는 털 수 있음 ==> 두개를 비교하여 큰값인 경우를 고르면 됨

n= int(input())

array= list(map(int, input().split()))

d= [0] * 100

d[0] = array[0]
d[1]= max(array[0], array[1])

for i in range(2, n):
    d[i]= max(d[i-1], d[i-2] + array[i])


print(d[n-1])