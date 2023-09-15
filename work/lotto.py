from random import *

nums = []

while True :
    num = randint(1, 37)

    for i in nums :
        if i == num :
            break

    nums.append(num)

    if len(nums) == 7:
        break

print(nums)