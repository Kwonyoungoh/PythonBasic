import re

# 1
str01 = 'I love python. dddpython is my favorite programming language. python'

pat01 = re.compile('python')
res01 = pat01.findall(str01)
print(res01)

# 2
str01 = 'python is fun. I love python.'

# 마침표 기준으로 정렬
# lookbehind assertion
# (?<=...)
# 문자열이 특정패턴과 일치하는지 확인
# ^ 시작
# | or연산
# \ 문장 끝
# \s 공백
# \S 공백 아님
# [] 대괄호 안 문자와 일치

# 패턴 생성
pat01 = re.compile('^python[^.]*\.')
#
res01 = pat01.findall(str01)

print(res01)

# 3
# (?: ... ): 괄호 안의 내용을 캡쳐하지 않는 비캡쳐 그룹(non-capturing group)입니다. 이 그룹 내의 패턴이 일치하더라도 별도로 저장되지 않아 나중에 참조할 수 없습니다.
# [^.]: 마침표를 제외한 모든 문자에 일치합니다.
# |: 또는 (or)의 의미를 가지는 alternation입니다.
# \A: 문자열의 시작에 일치합니다.
# 따라서, (?:[^.]|\A) 패턴은 "마침표가 아닌 문자" 또는 "문자열의 시작"에 일치합니다.

str01 = 'I love python. python is my favorite programming language. Do you like python.'

# [^.]: 대괄호 내부의 ^ 기호는 "다음 문자를 제외하라"는 뜻
pat01 = re.compile('[^.]*python\.')
res01 = pat01.findall(str01)
print(res01)

# 4
str01 = r'I love python. python is my favorite programming language. Do you like java'
pat01 = re.compile('[^.]*python[^.]*\.')
res01 = pat01.findall(str01)
print(res01)

# 5
str05 = 'abc! def? ghi#'

pat05 = re.compile('\W')
res05 = pat05.findall(str05)
print(res05)

# 6
str05 = 'abc! def? ghi#'

#[]안에서만 ^가 not의 의미를 갖는다..
pat05 = re.compile('[^\w\s]')
res05 = pat05.findall(str05)
print(res05)