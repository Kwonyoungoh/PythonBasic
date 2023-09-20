def get_personal_info(name,addr,age):
    print(f'name {name}')
    print(f'address {addr}')
    print(f'age {age}')

set1 = {'jena','miami',12}
get_personal_info(*set1)

dic1 ={'name':'jena','age':12,'addr':'miami'}
get_personal_info(*dic1)

get_personal_info(*dic1.values())

# 알아서 들어감 dictionary unpacking
get_personal_info(**dic1)

# 5
# kwargs
def get_p_info2(**kwargs):
    print(kwargs)
    for key, arg in kwargs.items():
        print(f'{key} : {arg}')

get_p_info2(**dic1)
get_p_info2(name = 'je22na', age=12, addr='miami')