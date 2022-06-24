#조건문

==와 != 

== 같다
!= 다르다


중첩 if(if문 안에 if)
x=12
if x >= 10:
    if x % 2 == 1:
        print("10이상의 홀수")

중첩 없이 if문 하나로(논리 연산자 사용)
x=7
if x>0 and x<10:
    print("10보다 작은 자연수")

파이썬은 and 연산 없이도 가능
if 0<x<10:
    print("10보다 작은 자연수")

if ~ else(분기문)
if문이 참이 아니면 else문 실행

if ~ elif ~else
if가 참이면 if문만 출력 elif는 출력 X
if가 참이 아니면 elif를 돌며 확인한다.
결국 elif까지 참인 경과가 없다면 else문 출력

-> 다중 if는 전부 출력하게 됨

x = 93
if x>90:
    print('A')
elif x> 80:
    print('B')
elif x > 70:
    print('C')
elif x > 60:
    print('D')
else:
    print('F')
