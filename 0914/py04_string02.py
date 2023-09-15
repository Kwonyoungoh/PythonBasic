str7 = '반갑습네다 내래 평안북도에 삽네다'

# 그거아냐? 공백도 문자열이야 임마
# 아스키코드 0x00

print(str7[2])
print(str7[-2])

# 이건 슬라이싱
# 여러개 뽑는 방법
print(str7[:11])

print(str7[-5:])

# 문제 : "Life is bad"
# bad를 good으로 바꾸자
# 문제 : "My time is gold"
bad = 'Life is bad'
good = 'good'

print(bad[:-4], good)

gold = 'My time is gold'
body = 'body'

print(gold[:2], body, gold[8:])

# -1을 던지는 find()
idx = gold.find('time')
# 예외를 던지는 index()
try:
    idx2 = gold.index('hey')
except Exception as err:
    print('index()는 예외를 던진다.', err)
    idx2 = 'none'

# 그리고 replace()는 문자열 교체 가능
# 그러나 파이썬에서 문자열은 immutable 객체
# 그러므로 직접 변경이 불가능 재할당해야 원본에 반영됨
gold = gold.replace('gold','body')

print(gold)
print(idx)
print(idx2)

# 스킵 & 리버스
s4 = 'w e l c o m e'
# 짝수(지금은 2의 배수)에 해당하는 애들만 출력한다.
print(s4[::2])

s5= '오사삼이일'
print(s5[::-1])
