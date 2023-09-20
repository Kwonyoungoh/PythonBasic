# 명시적 접근 제어가 불가능하기때문
def outer_func1():
    hello = 'hello outter'

    def closer():
        print(hello)
        return hello

    return closer()


outer_func1()

# lambda와 함께 이런식의 사용도 가능하다
def outer_func2(a):
    hello = a
    return lambda x : hello+':'+x

inner_func2 = outer_func2('hello')
print(inner_func2('world'))