# @Author  dongwukun
# @date  2023/7/13 19:21
# @version  1.0
import traceback
from utils.handle_loguru import log


class ApiAssert:

    @classmethod
    def api_assert(cls, result, condition, exp_result, assert_info, msg='断言操作'):
        #断言结果描述
        pass_msg = "验证通过，预期结果:{0},实际结果:{1}"
        try:
            #断言类型
            result, exp_result = str(result[assert_info]), str(exp_result[assert_info])
            assert_type = {
                '==': result == exp_result,
                '!=': result != exp_result,
                '>': result > exp_result,
                '<': result < exp_result,
                'in': result in exp_result,
                # 'in': str(result[assert_info]) in str(exp_result[assert_info]),

                'not in': result not in exp_result
                # 'not in': str(result[assert_info]) not in str(exp_result[assert_info])
            }
            #使用断言类型
            if condition in assert_type: #断言类是存在的
                assert assert_type[condition]  #操作断言
            else:
                raise AssertionError('请输入正确的断言情况')
            log.info(f'{msg},断言类型:{condition},断言结果:{pass_msg.format(exp_result,result)}')
        except Exception as error:
            log.error(traceback.format_exc())
            raise error