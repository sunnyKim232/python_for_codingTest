# 성적과 이름의 정보가 순서대로 제공될때 성적이 낮은순으로 정렬하시오

n= int(input())

arr1=[]
for i in range(n):
    data=input().split()
    arr1.append((data[0], int(data[1])))


arr2= sorted(arr1, key=lambda students: students[1])

print(arr2)