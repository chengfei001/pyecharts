import re
import logging
import os
import  sys

from requests import get

logging.basicConfig(level=logging.DEBUG)

def addone(match):
    val1 = match.group()
    num = int(val1) + 1
    return str(num)

if __name__ == '__main__':
    str1 = 'Chengfei oo1 abc test 123'

    r = re.compile(r'fei')
    logging.info(type(r))
    pattern1 = r.match(str1)
    logging.info(pattern1)

    # 忽略大小写 在pattern的表达式前加"r"后面的斜杠等就不需要转意了
    pattern2 = re.match(r'cheNg', str1, re.IGNORECASE)

    if pattern2 is not None:
        logging.info(pattern2.group())
        logging.info(pattern2.groups())
        logging.info(pattern2.groupdict())

    # 忽略大小写，并以组的形式返回

    pattern3 = re.match(r'(chenG)', str1, re.IGNORECASE)
    if pattern3 is not None:
        logging.info("groups")
        logging.info(pattern3.group())
        logging.info(pattern3.groups())
        logging.info(pattern3.groupdict())

    # 匹配任意a-z
    pattern4 = re.match(r'[abcdef]+', 'abadfafdsf',re.IGNORECASE)
    logging.info("pattern4")
    if pattern4 is not None:
        logging.info(pattern4.group())

    # 匹配任意A-Z
    pattern5 = re.match(r'[A-Z]', 'X')
    logging.info('pattern5')
    if pattern5 is not None:
        logging.info(pattern5.group())
    # 匹配0—9
    pattern6 = re.match(r'\d', '0')
    logging.info('pattern6')
    if pattern6 is not None:
        logging.info(pattern6.group())
    # 匹配空格+字母
    pattern7 = re.match(r'\s[\w]', ' b')
    logging.info('pattern7')
    if pattern7 is not None:
        logging.info(pattern7.group())
    # 匹配非数字
    pattern8 = re.match(r'[\D]', '(1!<>DAFE')
    logging.info("pattern8")
    if pattern8 is not None:
        logging.info(pattern8.group())
    # *
    pattern9 = re.match(r'([a-z][0-9]*)','a001x11100')
    logging.info('pattern9')
    if pattern9 is not None:
        logging.info(pattern9.group())

    # ?
    pattern10 = re.match(r'[a-z][0-9]+','a1111')
    logging.info('pattern10')
    if pattern10 is not None:
        logging.info(pattern10.group())

    pattern11 = re.match(r'[a-z][0-9]+', 'aaaa')
    logging.info('pattern11')
    if pattern11 is not None:
        logging.info(pattern10.group())
    # {m}/{m,n}
    pattern12 = re.match(r'[a-z]{1,100}[0-9]{3}@gmail.com', 'chengfei001@gmail.com')
    logging.info('pattern12')
    if pattern12 is not None:
        logging.info(pattern12.group())


    '''以下部分理解的还不透彻'''
    # *?
    pattern13 = re.match(r'[a-z][0-9]*?', 'a111')
    logging.info('pattern13')
    if pattern13 is not None:
        logging.info(pattern13.group())

    # +?
    pattern14 = re.match(r'[a-z][0-9]+?', 'c111')
    logging.info('pattern14')
    if pattern14 is not None:
        logging.info(pattern14.group())

    # ??
    pattern15 = re.match(r'[a-z][0-9]??','a1aa')
    logging.info('pattern15')
    if pattern15 is not None:
        logging.info(pattern15.group())
    '''以上部分理解的还不透彻'''

    # ^ 开头 这个好像对match效果为0
    pattern16 = re.match(r'^[a-z]{1}[0-9]*', 'b99999')
    logging.info('pattern16:' + pattern16.group())
    # $ 结尾
    pattern17 = re.match(r'[\w]*abc$','ddabcdabc')
    logging.info('pattern17:' + pattern17.group())
    # \A 指定字符开头
    pattern18 = re.match(r'\Aimooc[p][\w]*', 'imoocpython')
    logging.info("pattern18: " + pattern18.group())
    # \W 指定字符结尾
    # 分组
    pattern26 = re.match(r'<(?P<mark_hmtl>[\w]+>)[\w]+</(?P=mark_hmtl)', '<html>我是一个html</html>')
    logging.info(pattern26.groups())
    logging.info('pattern16:'+pattern26.group())

    # 练习分组
    pattern266 = re.match(r'<(?P<img>[\w]+>)[\w]+</(?P=img)','<img>正则表达式分组练习</img>')
    logging.info("pattern266:"+pattern266.group())

    # search
    pattern18  = re.search(r'\d+', '1000 299 300 ,55')
    logging.info(pattern18.group())

    # findall
    pattern19 = re.findall(r'http://[\w|.|/]*', 'http://www.cmbchina.com/1.html http:// abc http://baidu.com')
    logging.info(pattern19)

    # sub
    pattern20 =re.sub(r'\d+', addone, '100000 200 333')
    logging.info(pattern20)

    # split
    pattern21 = re.split(r' |,', 'coffee,tea,wather juice')
    logging.info(pattern21)

    line = "Cats are smarter than dogs"
    # .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
    matchObj = re.match(r'(.*) are (.*?) .*', line,  re.I)

    if matchObj:
        logging.info("matchObj.group() : " + matchObj.group())
        logging.info("matchObj.group(0) : " + matchObj.group(0))
        logging.info("matchObj.group(1) : " + matchObj.group(1))
        logging.info("matchObj.group(2) : " + matchObj.group(2))

    else:
        logging.info("No match!!")

    import re

    phone = "2004-959-559 # 这是一个电话号码"

    # 删除注释
    num = re.sub(r'#.*$', "", phone)
    logging.info("电话号码 : " + num)

    # 移除非数字的内容
    num = re.sub(r'\D', "", phone)
    logging.info("电话号码 : "+num)


    # 将匹配的数字乘于 2
    def double(matched):
        logging.info('X'+matched.group('value'))
        value = int(matched.group('value'))
        return str(value * 2)


    s = 'A29G4HFD567'
    logging.info(re.sub('(?P<value>\d+)',double, s))

    # req = get('https://www.imooc.com')
    # content = req.text
    # logging.info(type(req.text))
    # pattern22 = re.compile(r'//img.+.jpg')
    #
    # list_src = re.findall(pattern22,content)
    # logging.info(list_src)
    # for src in list_src:
    #     jpg = get('https:'+src).content
    #     with open(os.path.basename(src), 'wb') as f:
    #         f.write(jpg)
    logging.info(re.search('com', 'www.runoob.com').span())

    it = re.finditer(r"\d+", "12a32bc43jf3w11asdf,1234")
    for match in it:
        logging.info(match.group())

    it = re.finditer(r"\w+", "12a32bc43jf3w11asdf,1234")
    for match in it:
        logging.info(match.group())

    s = '北京2017-11-27到达'
    # 11/27/2017
    logging.info(re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', s))
    logging.info(re.findall('(\d{4})-(\d{2})-(\d{2})', s))

    ip = '0.1.1'
    trueIp = re.search(r'(([01]{0,1})\.)', ip)
    # trueIp = re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])', ip)
    logging.info(trueIp.group())

    html = '<H1>Chapter 1 - 介绍正则表达式</H1>'

    logging.info(re.search(r'<.*>', html).group())

    logging.info(re.search(r'<.*?>', html).group())
    logging.info(re.search(r'<\w+?>', html).group())

    url = 'http://www.baidu.com:81/book/item.html'
    match_list = re.match(r'(\w*)://([^/:]+):([\d]*|./)?([^# ]*)', url)
    logging.info(match_list.group(1))
    logging.info(match_list.group(2))
    logging.info(match_list.group(3))
    logging.info(match_list.group(4))
    for match in match_list.groups():
        logging.info(match)

    s = '(abc)xyzWa'
    pattern30 = re.compile(r'(\(.*\))(.*)')
    logging.info(pattern30.search(s).groups())
    logging.info(pattern30.search(s).groups())

    pattern31 = re.compile(r'^[a-z]+$')
    s_lower ='aebcXWcw'
    s_lower_s = pattern31.search(s_lower)
    if s_lower_s:
        logging.info(s_lower_s.group()+'全是小写')
    else:
        logging.info(s_lower + '：有大写')


    def expand_abbr(sen, abbr):
        lenabbr = len(abbr)
        logging.info(lenabbr)
        ma = ''
        for i in range(0, lenabbr):
            ma += abbr[i] + '[a-z]+' + ' '
            logging.info(abbr[i])
        logging.info('ma:' + ma)
        ma = ma.strip(' ')
        logging.info('ma:' + ma)
        p = re.search(ma, sen)

        if p:
            return p.group()
        else:
            return ''


    logging.info(expand_abbr("chengfei   Cab Air Big Cool DD!", 'ABC'))

    sen = 'asdf1345,1234,123,12341324asdfa'
    p = re.compile(r'\d+,\d')
    while 1:
        mm = p.search(sen)
        if mm:
            mm = mm.group()
            logging.info('mm:' + mm)
            sen = sen.replace(mm, mm.replace(',',''))
            logging.info(sen)
        else:
            break
    # 链接显示内容
    # p = re.compile(r'<a(?:[^>]*)+href=([^>]*)(?:[^>]*)*>')
    p = re.compile(r'<a(?:[^>]*)+href=([^^>]*)(?:[^>]*>)')
    a_mark = '<a href=www.baidu.com>百度</a>'
    a_content = p.search(a_mark)
    if a_content: logging.info(a_content.group())
    pass
