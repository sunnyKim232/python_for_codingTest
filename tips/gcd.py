# 유클리드 호제법
# 두 자연수에 대해 (a>b 일때) a를 b로 나눈 나머지 값과 b값의 최대공약수와 같다는 점을 이용하여 재귀함수로 구현가능함

def gcd(a, b):
    if a % b==0:
        return b
    else :
        return gcd(b, a%b)

print(gcd(192,162))