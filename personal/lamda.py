# 1
# 각 튜플은 학생의 이름, 점수, 키를 나타냅니다.
# 리스트를 점수가 높은 순서로 정렬하되,
# 점수가 같을 경우 키가 낮은 순서로 정렬하세요.
students = [("cohn", 990, 170), ("aane", 88885, 180), ("aoe", 9999992, 175), ("abddoe", 92, 175)]

res= sorted(students, key = lambda x: (len(x[0]),x[0] ,x[1],x[2]) )
print(res)

# 2
# 리스트를 단어의 길이가 짧은 순서로 정렬하되,
# 길이가 같을 경우에는 알파벳 역순으로 정렬하세요.
words = ["apple", "banana", "cherry", "date", "fig", "grapes", "kiwi"]

# 3
#주어진 리스트에 대해 홀수와 짝수를 분류하여 홀수는 오름차순, 짝수는 내림차순으로 정렬하세요.

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

nums = sorted( numbers , key = lambda x : (x%2==1,-x if x%2==1 else x ))
print(nums)


# 4
# 다음과 같은 사람의 나이와 이름 정보가 들어있는
# 리스트를 나이 오름차순으로 정렬하되,
# 나이가 같으면 이름의 알파벳 순서로 정렬하세요.

people = [("Alice", 32), ("Bob", 25), ("Charlie", 32), ("Daisy", 25)]
