# @Author  dongwukun
# @date  2023/7/4 16:37
# @version  1.0
import base64
import hashlib

def get_md5_data(pwd: str, salt=""):
    md5 = hashlib.md5()   #获取md5对象
    pwd = pwd+salt    #加盐 拼接
    md5.update(pwd.encode('utf-8'))  #将密码转为字节串
    return md5.hexdigest()  #md5的16进制返回

if __name__ == '__main__':
    res = get_md5_data('123456')
    res2 = get_md5_data('123456', 'mm')
    print(res)
    print(res2)


#E10ADC3949BA59ABBE56E057F20F883E


'''
Rsa加密和解密
'''

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher

class RsaEncrypt:
    def __init__(self, filepath='../data/'):
        self.filepath = filepath


    def Encrypt(self, data):
        with open(self.filepath+'public.pem', 'rb') as op:
            public_content = op.read()
            publickey = RSA.importKey(public_content)
            cipher = PKCS1_cipher.new(publickey)
            cipher_text = cipher.encrypt(data.encode('utf-8'))
            return base64.b64encode(cipher_text).decode()

    def Dncrypt(self, num):
        with open(self.filepath + 'publicgg.pem', 'rb') as ss:
            res = ss.read()
            cipher = PKCS1_cipher.new(RSA.importKey(res))
            retval = cipher.decrypt(base64.b64decode(num), 'ERROR').decode('utf-8')
            return retval


if __name__ == '__main__':
    res = RsaEncrypt().Encrypt('1234567')
    print(res)
    print('-------------')
    res1 = RsaEncrypt().Dncrypt(res)
    print(res1)


print('-------------')


class RsaEncrypt1:
    def __init__(self, filepath='../data/'):
        self.filepath = filepath


    def Encrypt1(self,data):
        with open(self.filepath+'publicbb.pem', 'rb') as op:
            public_content1 = op.read()
            publickey1 = RSA.importKey(public_content1)
            cipher1 = PKCS1_cipher.new(publickey1)
            cipher_text1 = cipher1.encrypt(data.encode('utf-8'))


            return base64.b64encode(cipher_text1).decode()



if __name__ == '__main__':
    res = RsaEncrypt1().Encrypt1('123456')
    print(res)

















