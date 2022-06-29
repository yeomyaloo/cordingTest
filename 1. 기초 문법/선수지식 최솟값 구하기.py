#최솟값 구하기 알고리즘

arr = [5,3,7,9,2,5,6]
arrMin = float('inf')
for i in range(len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i]
print(arrMin)

#같은 방식의 다른 모양의 풀
for x in arr:
    if x < arrMin:
        arrMin = x

print(arrMin)
