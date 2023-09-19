def sum1(*nums):
    total = 0
    print(nums)
    for n in nums:
        total += n
    print(total)


nums = [i for i in range(1, 11)]
print(nums)
# 가변길이 파라미터
sum1(1, 2, 3, 4, 5, 6)

# 언패킹 방식
def sum2(a, b, c):
    print(a + b + c)

x1=[10,20,30]

sum2(*x1)
