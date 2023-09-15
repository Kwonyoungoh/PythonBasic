# 파일 생성 후 쓰기 옵션을 지정
file1 = open('file1.txt', "w")

# 파일로 출력
print('Hello Python!', file=file1)

# 파일 세션 닫기
file1.close()
