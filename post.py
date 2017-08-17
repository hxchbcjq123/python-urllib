#! /usr/python urllib/python3
import urllib.parse
import urllib.request
values={'username':"123456",'password':'******'}
data=urllib.parse.urlencode(values).encode(encoding='UTF8')
url='http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
Request=urllib.request.Request(url,data)
response=urllib.request.urlopen(Request)
final=response.read()
print(final)
