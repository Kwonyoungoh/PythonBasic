from sys import stdin

N = int(1e9)+7

# 수입력
n = int(stdin.readline().rstrip())
# fib의 결과1
# 1 1 2 3 5 8 13 21 34
a = 1
b = 1
ans = n-2
for _ in range(n-2):
    b,a = (a+b)%N,b

print(b,ans)
