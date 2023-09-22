# 파이썬에서 csv 파일 형식을 읽을 때 사용하는 모듈
import csv

# 파일 읽기
f = open('movies.csv','r', encoding='utf-8')
# csv 파일 형식을 파이썬에서 사용할 수있는 형태로 변환
data = csv.reader(f)
# 이렇게 읽으면됨
print(next(data))

# 영화의 장르 데이터 컬럼 출력
next(data)
res = []

_= [res.extend(i[2].split('|')) for i in data]
print(len(res))

gen = list(set(res))
print(len(gen))
print(gen)

# 현재 각 장르의 영화의 갯수를 구하세요
cnt = {}
for i in res:
    if cnt.get(i):
        cnt[i] +=1
    else:
        cnt[i] =1
print(cnt)

# 장르가 가장 다양한 영화는?

# 연도별 가장 많이 개봉된 영화의 장르는?