# @Author  dongwukun
# @date  2023/7/12 14:35
# @version  1.0

import pytest

from conflgs.config import NAME_PWD
from libs.login import Login
from libs.shop import Shop

'''
session:作用于所有文件执行之前
function:所有函数执行之前
class:所有类执行之前
module:所有模块执行之前
'''
@pytest.fixture(scope='session',autouse=True)
def init_login():
    print('----------------开始登录------------------')


'''------------1.登陆操作----------------_token'''
@pytest.fixture(scope='session')
def login_init():
    print('----1.开始执行的登录操作----')
    token = Login().login(NAME_PWD, get_token=True)    #NAME_PWD是个常量 跟HOST放在一块 你想要token就写Ture 不像就Flase
    yield token
    print('登陆完成,我要退出')

@pytest.fixture(scope='session')
def shop_init(login_init):
    print('------2.创建店铺实例操作-----')
    shop_boject = Shop(login_init)
    yield shop_boject   #返回给测试方法使用

#--------店铺更新初始化操作
@pytest.fixture(scope='class')
def update_shop_init(shop_init):
    shop_id = shop_init.query({'page': 1, 'limit': 20})['data']['records'][0]['id']
    image_info = shop_init.file_upload('../data/123.jpg')['data']['realFileName']
    shop_update = {'shop_object': shop_init, 'shop_id': shop_id, 'image_info': image_info}
    yield shop_update


'''在使用pytest.mark.parametrize 对用例进行参数化的时候，传入的值包含中文，运行用例，控制台显示编码问题解决方法:在用例的根目录下，新建conftest.py文件，将下面的代码复制进去
defpytest_collection_modifyitems(items):'''

def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")








