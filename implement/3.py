# 8*8 체스판에서 말이 1. 수평 2칸 수직 1칸 2.수직 2칸, 수평 1칸로만 이동할 수 있을때
# 주어진 좌표에서 이동할수 있는 모든 경우의 수를 구하시오 (체스판 밖으로는 이동할 수 없음)


## 먼저 풀기
x, y= list(str(input()))
max= 8

if x== "a":
    nx= 1
elif x=="b":
    nx= 2
elif x=="c":
    nx=3
elif x =="d":
    nx=4
elif x =="e":
    nx=5
elif x=="f":
    nx=6
elif x=='g':
    nx=7
elif x=="h":
    nx=8

# 가능한 모든 움직임의 경우
moves=[[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [1, -2], [1, 2], [-1, 2]]


for move in moves:
    fx= nx+ move[0]
    fy =int(y) + move[1]
    if fx < 1 or fy < 1 or fx > 8 or fy > 8:
        max = max -1

print(max)


## 정답
# 아스키 코드를 활용하여 if 문 줄일수 있음
datas= input()
row= int(datas[1])
column= int(ord(datas[0])) - int(ord('a')) + 1

# 그 외에는 같음