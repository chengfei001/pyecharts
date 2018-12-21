import urllib,urllib3
import  requests

Url = 'http://www.chengfei.com/get'

params = urllib.parse.urlencode({'name':'coffee','param2':'daye'})
print('?'.join((Url,'%s')) % params)
