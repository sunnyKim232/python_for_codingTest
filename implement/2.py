# 정수 n이 입력되면 00시 00분 00초부터 N시 59분 59초까지 시각중에서
# 3이 하나라도 포함되는 모든 경우의 수를 구하시오


n = int(input())
count = 0

for time in range(n+1):
    for min in range(60):
        for sec in range(60):
            total=list(str(time))+list(str(min))+list(str(sec))
            if '3' in total:
              count +=1

print(count)
