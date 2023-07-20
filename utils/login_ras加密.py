# @Author  dongwukun
# @date  2023/7/5 16:47
# @version  1.0
import requests
from utils.handle_date import get_md5_data, RsaEncrypt1


'''
高级加密登录
'''

def lgoin(data):
    url = 'http://42.192.62.8:8082/account/loginRsa'
    #给password进行md5加密
    pwd_md5_text = get_md5_data(data['password'])
    #将加密后的密码(password)使用rsa加密
    data['password'] = RsaEncrypt1().Encrypt1(pwd_md5_text)
    #使用用户名和密码进行签名
    sign = get_md5_data(data['username'] + data['password'])
    #将签名放到data中
    data.update({'sign': sign})
    payload = data
    #发送请求
    res = requests.post(url, data=payload)
    return res

if __name__ == '__main__':
    test_data = {
        'username': 'ct0958',
        'password': '14443'
    }
    res = lgoin(test_data)
    print(res.text)

# def login(data):
#     url = 'http://42.192.62.8:8082/account/loginRsa'
#     pwd_md5_text = get_md5_data(data['password'])
#     data['password'] = RsaEncrypt1().Encrypt1((pwd_md5_text))
#     sign = get_md5_data(data['username'] + data['password'])
#     data.update({'sign': sign})
#     payload = data
#     res = requests.post(url, data=payload)
#     return res
#
# if __name__ == '__main__':
#     test_data = {
#         'username': 'ct0958',
#         'password': '14443'
#     }
#     res = login(test_data)
#     print(res.json())
