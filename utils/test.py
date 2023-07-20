# @Author  dongwukun
# @date  2023/7/18 16:24
# @version  1.0
import time

# def show_time(func):
#     def inner():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#         print(f'执行自动化测试用例使用了{end_time-start_time}')
#     return inner
#
# @show_time
# def test():
#     print('测试用例开始')
#     time.sleep(1)
#     print('测试用例结束')

# def test2():
#     print('小红开始')
#     time.sleep(1)
#     print('小明结束')


# test()
# test2()
# res = show_time(test)
# test()
# res1 = show_time(test2)
# test2()

def show_time(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print(f'执行自动化测试用例使用了{end_time-start_time}')
        return res
    return inner
