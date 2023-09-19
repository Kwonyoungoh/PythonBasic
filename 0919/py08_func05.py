def func1(a,b,c, **kwargs):
    print(a)
    print(b)
    print(c)
    print(kwargs)

dic1={'a1':1,'b1':2,'c1':3}

# key 값의 중복은 피해야한다.
func1(1,2,3,**dic1)
# func1(1,2,3,a1=23,b1=233,c1=1232)

def func2(*args, **kwargs):
    print(*args)
    print(kwargs)

func2(1,2,3, **dic1)

def func3 (a, *args):
    print(a)
    print(args)

func3(1)
func3(1,2,3)
# 리스트 언패킹 해준다면?
func3(*[10,20,30])

lst = [1,2,3]
print(lst[-3])