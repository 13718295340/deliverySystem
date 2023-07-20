# @Author  dongwukun
# @date  2023/7/6 8:52
# @version  1.0
import inspect

import requests

from common.baseAPI import BaseApi
from utils.handle_date import get_md5_data
from utils.test import show_time

class Login(BaseApi):
    @show_time
    def login(self, data, get_token=False):
        data['password'] = get_md5_data(data['password'])
        resp = self.send_method(data)
        if get_token:
            return resp['data']['token']
        return resp

if __name__ == '__main__':
    test_data = {
        'username': 'ct0958',
        'password': '14443'
    }

    # res = Login().login(test_data)
    # print(res)
    test = show_time(Login().login)(test_data, get_token=True)









