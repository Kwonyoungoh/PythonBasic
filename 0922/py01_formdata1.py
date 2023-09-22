c = """
        <div class="select_div">
            <span data-i18n="footer.relationSites">연관사이트</span>
            <ul>


            </ul>
        </div>
        <ul class="list_sns">
            <li><a href="https://www.facebook.com/ekoreatech" target="_blank"><img src="/res/lms/img/common/btn_footer_sns1.png" alt="페이스북"></a></li>
            <li><a href="https://blog.naver.com/e-koreatech" target="_blank"><img src="/res/lms/img/common/btn_footer_sns2.png" alt="블로그"></a></li>
            <li><a href="https://www.youtube.com/user/koreatecholei" target="_blank"><img src="/res/lms/img/common/btn_footer_sns3.png" alt="유트브"></a></li>
        </ul>
    """

# find()함수
print(c.find('list_sns'))

# 키워드를 이용한 스키핑
c = c[169:]
print(c)

# 데이터 소거 시 자주 쓰는 방법
# <li> 태그를 기준으로 쪼개기
c = c.split('<li>')
print(c)
print('-'*40)
# c[0] 출력
# print(c[1])

# 각 태그에서 url태그만 출력
url = c[1].split('" target')[0]
# print(url)

# 각 태그에서 url 만 출력 2
url = url.split('href=')

name = c[1].split('alt="')[1]
print(name)
name = name[:name.find('"')]
print(name)

print(url[1].find('페이스북'))

print(url[1][110:114])

# 지금까지의 내용 종합
for i in range(len(c)-1):
    url= c[i].split('" target')[0]
    url = url.split('href="')[1]
    print(url)
    name  = c[i].split('alt="')[1]
    name = name[:name.find('"')]
    print(name)