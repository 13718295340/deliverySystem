# -*- coding: utf-8 -*-
# @Author  zhaojiaoyang
# @date  2023/7/16 21:26
# @version  1.0


HOST = 'http://127.0.0.1:9999'
import requests


#---------1,提交申请接口----------
def commit_order(data):
    url = f'{HOST}/api/order/create/'
    payload = data
    resp = requests.post(url, json=payload)
    return resp.json()


#-------2,查询接口-----------------
'''
场景特性：
    - 不是你想查里面就有结果的，可能需要一段时间
方案：
    -主动通知
    -定时轮询去查
        - 使用id
        - 频率
        - 超时机制   
'''
import time
def get_order_result(order_id,interval = 5,time_out = 30):
    '''
    :param order_id: 申请的id
    :param interval: 间隔时间-s
    :param time_out: 超时时间-s
    :return:
    '''


    start_time = time.time()
    end_time = start_time + time_out
    url = f'{HOST}/api/order/get_result/'   #(可改对错)
    # url = f'{HOST}/api/order/get_result__x/'  #(可改对错)
    payload = {'order_id': order_id}
    cnt = 1
    while time.time() < end_time:
        resp = requests.get(url, params=payload)
        if resp.text:
            print('查询成功,查询结果为：'+resp.text)
            return
        else:
            print(f'第{cnt}次查询，没有返回结果，请稍后查询！')
        time.sleep(interval)
        cnt += 1

    print('查询超时，请联系平台管理员')



import threading
if __name__ == '__main__':
    # 主线程计时
    start_time = time.time()
    order_data = {
        'user_id': 'sq123456',
        'goods_id': '20200815',
        'num': 1,
        'amount': 200.6
    }
    # 获取响应数据
    order_id = commit_order(order_data)['order_id']
    # print(order_id)
    # ----------创建子线程--查询接口-----
    t1 = threading.Thread(target=get_order_result, args=(order_id,)) #多线程
    # 设置线程模式：如果主线程结束，或者异常退出，子线程直接退出
    # t1.setDaemon(True)      # 守护模式
    t1.daemon = True
    t1.start()
    # ---------
    # 2-查询接口
    # res = get_order_result(order_id)
    # print(res)
    # ------------模拟一个主线程用例执行------------
    for one in range(20):
        print(f'{one}---我正在执行主线程的自动化测试用例---')
        time.sleep(1)




    end_time = time.time()
    print('自动化执行耗时--->', end_time-start_time)
'''
当前版本
    - 功能实现了
    问题：执行效率问题--资源浪费  如果这个接口30s内都没有结果，自动化执行会等待这个30s
    新需求：提升自动化执行效率
测试人员：分析新需求
    现象：效率低
    本质：while+time.sleep(5)
解决本质问题：
    发散：
        - 是否可以减少等待时间
        - 一旦sleep(5) cpu 不干活
    根本：
        - cpu资源使用 
        - 了解cpu
            IO阻塞----*
                - sleep()
                - request()-- 同步
            cpu密集型
        
技术方案：
    技术瓶颈：cpu IO阻塞
    实施方案：
        - 多进程--使用cpu的多核优势
        - 多线程--充分使用一个核
        - 协程--比多线程优秀
        - 比较高效率：进程+协程

    选定方案：
        多线程技术
        - 主线程：自动化测试运行
        - 子线程：查询结果的接口
        
扩展：
    pytest 框架有自己的分布式运行
    pip install pytest-xdist

'''
# if __name__ == '__main__':
#     order_data = {
#         'user_id': 'sq123456',
#         'goods_id': '20200815',
#         'num': 1,
#         'amount': 200.6
#     }
#     #获取响应数据
#     order_id = commit_order(order_data)['order_id']
#     print(order_id)
#     res = get_order_result(order_id,5,30)
    # print(res)