std1 = ['dean','head','ami','june']
# 이런식의 응용또한 가능하다.
std1_comp={st:0 for st in std1}
print(std1_comp)

std1 = {'dean': 50, 'head': 30, 'ami': 60, 'june': 70}
dic1 ={n:s for n, s in std1.items() if n !='june'}
print(dic1)

is_pass ={n:'PASS'if val >=50 else 'FAIL' for n,val in std1.items()}
print(is_pass)