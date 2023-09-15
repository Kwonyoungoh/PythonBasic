print('안녕'
      '안녕2')

# 코드가 너무 길어지는 걸 방지 하려고
a: int = 1 + 2 + 3 + \
         4 + 5 + 6

b: int = (1 + 2 + 3 +
          4 + 5 + 6)

# 문자열 사이사이에 무언갈 추가할때 sep
# 문자열 끝에 무언갈 붙일때 end
print('aaaa', 'bbbb', sep='*', end='@\n')

a = 1

if a == 1:
    print('this is one')

num: int = int(input('숫자 입력해라: '))
# f-string 파이썬 3.6+ 부터 사용가능
print(f'입력 숫자 : {num}')
# str.format()
print('{}은 {}이다'.format(num, num))
# %연산자
print('내 나이 %d살'%(num))