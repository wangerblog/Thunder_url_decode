import base64, re

def url_decode(url_user):
    url_encode = url_user.lstrip('thunder://').encode()
    link = base64.b64decode(url_encode).decode('gbk')
    link = link.strip('AZ')
    return link

def url_chenk(url_user):
    while True:
        if re.match('thunder://',url_user):
            break
        else:
            print('你输入的不是需要破解的迅雷链接。\n')
        url_user = input('请重新输入迅雷下载地址：\n')
    return url_user

url_user = url_chenk(input('请输入需要破解的迅雷下载地址：\n'))

input('复制原始链接：\n%s'%url_decode(url_user))