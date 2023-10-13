from sys import stdin
# 1541
# 간단하다 걍 최대한 많이 더한거 빼주면된다.
# -로 나누고 다 더해서
# 첫수에서 다 빼주면 끝!
str = stdin.readline().rstrip()
lst1=str.split('-')
ans = []

for i in lst1:
    # 해당 리스트 요소 예시 '11+2+23'
    s_n = map(int,i.split('+'))
    ans.append(sum(s_n))
sum = 0

for i in range(len(ans)):
    if i ==0:
        sum += ans[i]
    else:
        sum -= ans[i]

print(sum)