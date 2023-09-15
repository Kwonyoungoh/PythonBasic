# 출력을 하는데 있어서 칸을 15칸을 채우는데 나머지는 공백으로
# 문자열에대한 포멧을 설정할때 많이쓴다.
print("Python is [{:15}]".format('good'))
print("Python is [{:^15}]".format('good'))
print("Python is [{:>15}]".format('good'))