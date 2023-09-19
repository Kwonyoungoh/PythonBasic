# 1003
# 재귀함수로 풀시 시간초과
# 결국 dp로 풀어야함
# DP 란 Dynamic Programming
# 재귀접근시 중복계산을 피하자@

def fibo(n , lst):

    if n == 1:
        lst[1]+=1
        return 1
    elif n == 0:
        lst[0]+=1
        return 0

    return fibo(n-1,lst)+fibo(n-2,lst)


nums = int(input())

for _ in range(nums):
    lst1 = [0, 0]
    n = int(input())
    fibo(n,lst1)
    print(lst1[0], lst1[1])