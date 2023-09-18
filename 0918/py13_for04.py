lst1 = list(range(5))
for i in range(len(lst1)):
    lst1[i] **= 2

list2 = [i ** 2 for i in range(5)]

# 1부터 10까지의 수를 가진 리스트에서 짝수만
list3 = [i for i in range(1, 11) if i % 2]
print(list3)

# 1-10 3의 배수
list5 = [i for i in range(1, 11) if not i % 3]
print(list5)

# 구구단임
for j in range(2,11):
    lst = [i for i in range(1,j*9+1) if not i % j]
    lst2 = [i*j for i in range(1,10)]
    print(lst)
    print(lst2)

# 이중 for문 일시

lst6 = [f'{i} * {j} = {i*j}' for i in range(2,11) for j in range(1,10)]
print(lst6)