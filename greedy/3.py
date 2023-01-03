# 1이 될때까지 주어진 n을 다음 두가지 과정중 하나 선택하여 반복적으로 수행한다.
# 1. N-1 2. N%K
# N과 K를 받아 몇번의 연산이 최소가 되는지 구하라 ( N > K)


# 먼저 풀기
import math

n, k = map(int, input().split())
result=0

while True:
    if n== 1:
        break
    gcd= math.gcd(n, k)
    if gcd != k:
        n = n-1
        result += 1
    elif gcd == k:
        n = int(n / k)
        result += 1


print(result)


