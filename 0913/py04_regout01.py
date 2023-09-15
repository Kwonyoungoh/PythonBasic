# 타입 힌트
# 사실상 필요하냐 하면 잘 모르겠다.
name: str  = '둘리'
age: int = 3

print(f'난 {name}, {age} 살이지')
print('my name is {} and {} years old' .format(name, age))
print('my name is {1} and {0} years old' .format('돌리', '8'))
print('내 이름은 말야 %s야 %04d 살이지 '% (name,age))

# 3.0 zero string
print('{}'.format(age).zfill(4))