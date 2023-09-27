from sys import stdin
# 파도반 수열
# T
T = int(stdin.readline().rstrip())
ns = [int(stdin.readline().rstrip()) for _ in range(T)]
lst = [0,1,1,1,2,2,3,4,5,7,9]

for n in ns:

    if n < len(lst):
        print(lst[n])
        continue

    for i in range(len(lst)-1,n+1):
        lst.append(lst[i]+lst[i-4])

    print(lst[n])