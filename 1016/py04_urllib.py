import urllib.request

res = urllib.request.urlopen('https://www.google.co.kr')
print(res.status)

if res.status == 200:
    print('success')

