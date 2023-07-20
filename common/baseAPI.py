# @Author  dongwukun
# @date  2023/7/6 8:51
# @version  1.0

import requests
import inspect

from utils.handle_loguru import log
from utils.handle_yaml import get_yaml_data
from conflgs.config import HOST

class BaseApi:
    def __init__(self, in_token=None):
        if in_token:
            self.headers = {'Authorization': in_token}
        else:
            self.headers = None
        self.payloaddata = get_yaml_data()[self.__class__.__name__] #类名

    def send_method(self, poyload=None, params=None, files=None, id=''):
        # try:
        apidata = self.payloaddata[inspect.stack()[1][3]] # 函数名
        res = requests.request(method=apidata['method'],
                         url=f'{HOST}{apidata["url"]}{id}',
                         data=poyload,
                         params=params,
                         headers=self.headers,
                         files=files
        )
        log_msg = f'''模块名:{self.__class__.__name__},接口名:{inspect.stack()[1][3]}
        请求的url:{res.request.url}
        请求方法:{res.request.method}
        请求体:{res.request.body}
        响应体:{res.json()}'''
        log.info(log_msg)
    #
        # except:
        #     pass
        # else:
        return res.json()

    def query(self, data):  #查询(列出商铺)
        return self.send_method(params=data)

    def add(self, data):   #增加
        return self.send_method(params=data)

    def update(self, data):  #修改
        return self.send_method(params=data)

    def delete(self, id):   #删除
        return self.send_method(id=id)

    '''文件上传格式： 文件路径：'''


    def file_upload(self,file_path:str):
        #1-获取文件名
        file_name = file_path.split('/')[-1]
        #2-文件类型
        file_type = file_path.split('.')[-1]
        file = {'file': (file_name, open(file_path, 'rb'), file_type)}
        #发送请求
        resp = self.send_method(files=file)
        return resp


if __name__ == '__main__':
        pass