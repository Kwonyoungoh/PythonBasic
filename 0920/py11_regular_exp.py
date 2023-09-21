import re
str1 = 'asdfasf 010-1234-5678 fdafasdf'

# [숫자범위]{길이범위}
pat01 = re.compile('[0-9가-힣a-zA-Z]{2,3}-[0-9]{4}-[0-9]{4}')
res = pat01.findall(str1)
print(res)

# 마침표 .
pat02 = re.compile('a.c')
res2 = pat02.findall('abc adf aec azd')
print(res2)

# 캐럿 ^
pat03 = re.compile('^abc')
res03 = pat03.findall('abcdd abcadff adg adbd')
print(res03)
print(res03)

# 진짜 외우기 싫다면 이거라도 외워라
# [검색할 글자의 종류]{반복할 최소 횟수, 반복할 최대 횟수}

