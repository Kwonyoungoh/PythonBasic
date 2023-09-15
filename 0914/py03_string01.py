str1 = '안녕'
str2 = "Hello"

print(str1)
print(str2)

str3 = """안녕!"""
print(str3)

# 안녕
# 내이름
# 돌리

# 이스케이프 문자 ( 개행 문자 )
str4 = " 안녕 \n 내이름 \n 돌리 \n"
print(str4)

# ex) 기사를 원문형태로 받을때
# 어떤 식으로 처리해줄거냐
# 트리플 쿼드
# 여러줄에 걸치 문자열 출력시 사용

str5 = '''
헬로
마이 넴
돌뤼
'''
print(str5)

# 주석으로 사용이 가능하지만 여러개의 문자열을 출력하기 위함

print('저는 "수원시"에 삽니다.')
# 옛날 방식
# 이스케이프 문자 '\'역슬레쉬 : 출력이 되지 않는 특수 문자를 문자열에 출력하기 위해서
# 사용하는 기호
print("Im living in \"Suwon\"")

# 문자열 변수 30번 연속 출력하려면 어떻게 해야지?
# for문 안쓰고 어떻게 할거냐?
str6 = '으아!!'
# 파이썬은 반복 출력에 대해 굉장히 잘 되어있다.
print(str6 * 30)