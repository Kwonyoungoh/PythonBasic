import re

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

pat = re.compile('https://.*" target')
res= pat.search(c)
print(res.group())

pat = re.compile('[a-z:/.]*')
res = pat.search(res.group())
print(res.group())