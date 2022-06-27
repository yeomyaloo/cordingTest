#람다함수


#일반적인 함수 사용 방법
def plus_one(x):
    return x+1

print(plus_one(1))

#람다 사용방법
plus_lambda = lambda x: x+2

print(plus_lambda(1))

a = [1,2,3]
print(list(map(plus_one, a)))

#map에 인자로 람다 표현식을 쓴 방법
#람다는 내장함수의 인자로 사용할떄 아주 편리하다
print(list(map(lambda x: x+1, a)))
