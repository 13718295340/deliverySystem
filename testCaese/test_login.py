# @Author  dongwukun
# @date  2023/7/11 8:43
# @version  1.0
# import os

import allure
import pytest

from common.apiAssert import ApiAssert
from libs.login import Login
from utils.handle_excel2 import get_excel





@allure.epic('订餐系统')
@allure.feature('登录模块')
#1-登录类
class TestLogin:
    test_data = get_excel('登录模块', 'Login', '标题', '请求参数', '响应预期结果')
    #2.登录的方法
    # @pytest.mark.parametrize('title,body,exp_date',get_excel('登录模块，"Login','标题','请求参数','响应项期结果'))
    @pytest.mark.parametrize('title,req_body,rexp_body',test_data) #[(请求参数,响应预期结果),(响应预期结果)]
    @allure.story('登录接口')
    @allure.title('{title}')
    def test_login(self, title, req_body, rexp_body):
        resp = Login().login(req_body)
        # assert resp['msg'] == rexp_body['msg']
        ApiAssert.api_assert(resp, '==', rexp_body, assert_info='msg', msg='登录接口断言')

# if __name__ == '__main__':
#     '''创建一个html网页'''
#     path = '../report/tmp'
#     pytest.main([__file__, '-sv', '--alluredir', f'{path}', '--clean-alluredir'])
#     # -v 详细的信息
#     os.system(rf'allure serve {path}')

if __name__ == '__main__':
    pytest.main([__file__, '-sv'])