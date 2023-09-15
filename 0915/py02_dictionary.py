dic1 = {'name': 'dickHead', 'phone': '22222', 'addr': 'heaven'}

# 딕셔너리는 키-값 형태로 set처럼 선언 해주면 된다.
print(dic1)
print(dic1['name'])

# 데이터 초기화는 list와 그 방법이 같다
dic1['name'] = 'dep'
print(dic1)
dic1['addr'] = 'hood'
print(dic1)

list1 = [1,2,3,4]
dic3 = dict(list1=list1)
print(dic3)

# 중복키 선언이 가능하나
# 맨 마지막에 초기화한 값으로 정해진다.
dic4 = {'aaa':'가가가','bbb':'nanana','aaa':'dadadad'}
print(dic4)