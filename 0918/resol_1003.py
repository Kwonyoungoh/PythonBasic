#  만약 n이라는 키가 딕셔너리 mem에 저장되어있다면
#  해당 리스트를 리턴
#  아니라면 재귀로 들어감
def fibo(n, mem):
    if n == 0:
        return [1,0]
    elif n == 1:
        return [0,1]
    if mem[n][0] == 0 and mem[n][1] == 0 :
        mem[n] = [x+y for x,y in zip(fibo(n-1,mem),fibo(n-2,mem))]
    return mem[n]


# lst = [ [0,0] for _ in range(4)]
#
# lst2 = fibo(3,lst)
# print('done')
nums = int(input())

for _ in range(nums):
    mem = []
    n = int(input())
    mem = [[0,0] for _ in range(n+1)]

    lst1 =fibo(n, mem)
    print(lst1[0], lst1[1])
