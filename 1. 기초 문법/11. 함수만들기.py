#함수 만들
def add(a,b):
    c = a+b
    d = a - b
    return c,d

print(add(3,2))


#약수만들기 - 반복문을 돌다가 나눠지는 값은 약수가 있기에 소수가 아님 return False를 돌려주고 함수 종료
def isPrime(x):
    #True and False return
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
    
a = [12,13,7,9,19]


for x in a:
    #x가 소수이면 print
    if isPrime(x):
        print(x, end=' ')
    
