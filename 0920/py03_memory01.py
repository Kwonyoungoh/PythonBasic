a = 1
b = 2
print(id(a))
def func1(a):
    print(id(a))
    a = a+1

def func2(a):
    global b
    b = b+a

func1(2)
func2(2)

print(a)
print(b)