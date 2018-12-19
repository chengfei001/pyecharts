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

    # 忽略大小写
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
    pattern4 = re.match(r'[abcef]', 'a', re.IGNORECASE)
    logging.info("pattern4")
    if pattern4 is not None:
        logging.info(pattern4.group())

    # 匹配任意A-Z
    pattern5 = re.match(r'[A-Z]', 'X')
    logging.info('pattern5')
    if pattern5 is not None:
        logging.info(pattern5.group())
    # 匹配1—9
    pattern6 = re.match(r'\d', '1')
    logging.info('pattern6')
    if pattern6 is not None:
        logging.info(pattern6.group())
    # 匹配空格
    pattern7 = re.match(r'\s', ' b')
    logging.info('pattern7')
    if pattern7 is not None:
        logging.info(pattern7.group())
    # 匹配非字符
    pattern8 = re.match(r'\D', '(!DAFE')
    logging.info("pattern8")
    if pattern8 is not None:
        logging.info(pattern8.group())
    # *
    pattern9 = re.match(r'[a-z][0-9]*','a001x11100')
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
    pattern16 = re.match(r'<(?P<mark_hmtl>[\w]+>)[\w]+</(?P=mark_hmtl)', '<html>我是一个html</html>')
    logging.info(pattern16.groups())
    logging.info('pattern16:'+pattern16.group())

    # search
    pattern18  = re.search(r'\d+', '1000 299 300 ,55')
    logging.info(pattern18.group())

    # findall
    pattern19 = re.findall(r'http://[\w|.|/]*','http://www.cmbchina.com/1.html http:// abc http://baidu.com')
    logging.info(pattern19)

    # sub
    pattern20 =re.sub(r'\d+', addone, '100000 200 333')
    logging.info(pattern20)

    # split
    pattern21 = re.split(r' |,', 'coffee,tea,wather juice')
    logging.info(pattern21)

    req = get('https://www.imooc.com')
    content = req.text
    logging.info(type(req.text))
    pattern22 = re.compile(r'//img.+.jpg')

    list_src = re.findall(pattern22,content)
    logging.info(list_src)
    for src in list_src:
        jpg = get('https:'+src).content
        with open(os.path.basename(src), 'wb') as f:
            f.write(jpg)


    pass
