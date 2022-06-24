#문자열과 내장함수
msg = "It is Time"
print(msg.upper()) #대문자화
print(msg.lower()) #소문자

find()
count()

slice 기능 [:0번부터 해당 번호 전까지]
[3:5] index 3 ~ 4까지

len() 공백 포함 문자열 길이를 구해준다.

for x in msg:
    if x.isupper():
        print(x, end='')
isupper(): 대문자 여부 확인
islower(): 소문자 여부 확인
isalpha(): 알파벳인지 여부 확인
ord(): 아스키 넘버 A:65 ~ Z: 90
                   a: 97 ~ z: 122
