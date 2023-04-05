
## 특정 구간의 합을 구하는 문제가 여러 번에 걸쳐서 수행될 필요성이 있을때
## 접두사합 - prefix sum 이용: 배열의 맨 앞부터 특정 위치까지의 합을 미리 구해놓는것
## left와 right의 위치의 합을 구하려고할때 프리픽스 배열을 구해 놓고
## p[right] - p[left-1] 의 값이 정답이 됨

n= 5
data= [10,20,30,40,50]

## frefix sum array
sum_value=0
prefix_sum= []
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

left= 3
right= 4
print(prefix_sum[right]- prefix_sum[left])