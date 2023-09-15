# 1
x = 'Hello, World!'
y = x[-6: -1]
# print(y)
print('{} {}'.format(y,y),end=' ')
print('{}'.format(y))

# 2
x= 'Hello, Python!'
y = x[-7:]
print('{} {}'.format(y,y),end=' ')
print('{}'.format(y))

# 3
x = 'Learning Python is fun!'
y = x
print('{} is a part of {}'.format(x[9:15],x))

# 연습문제 2
x = 'Programing is life'
y =x[::-1]
z = x[::2]
print('{}\n{}\n{}'.format(y, z, y+z))

# 연습문제 3
# banana

fruits =['apple','banana','cherry']
fruits = fruits+['orange']
print(fruits)



