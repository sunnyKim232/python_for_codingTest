# 큰 수의 법칙
# 배열의 갯수 N, 총 숫자가 더해지는 M, 같은 인덱스가 연속해서 K번이상 사용될 수 없음
# 배열에서 M 번만큼 더해질 수 있는 경우 중에 가장 큰 수를 구하라

## 풀어보기
n, m, k = map(int, input().split())
arr= list(map(int, input().split()))

arr.sort()
first= arr[n-1]  # 가장 큰수
second= arr[n-2]  # 두번째로 작은수

result= 0  # 결과를 더해줄 최종값
count=0  # m번만큼 돌았는지 확인해줄 임시값

for _ in range(m):
    for _ in range(k):
        if count>= m:
            break
        result += first
        count += 1
    if count < m:
        if count>= m:
            break
        result += second
        count += 1

print(result)


## 정답
# 반복되는 수열의 길이를 구하기
# k+1번이 한 덩이로 반복해서 나타남 예시: k=3일때 (큰수,큰수,큰수,작은수)
# 총 더할 길이가 8번이라면 8번 중 k+1길이의 수열이 반복해서 나타남
# M / (k+1) => 수열의 길이
# 수열의 길이 * k 만큼 가장 큰 수가 들어갈 수 있음
# 만약 딱 떨어지는 길이가 아니라면? 수열 외에 나머지 길이만큼 큰 수가 들어갈 수 있음

howManyBiggest= (m / (k+1)) * k + (m % (k+1))
howManySecond= m - howManyBiggest

result= howManyBiggest*first + howManySecond*second
print(result)
