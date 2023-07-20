# @Author  dongwukun
# @date  2023/7/18 9:52
# @version  1.0
HOST = 'http://127.0.0.1:9999'
import requests



'''------1.提交申请接口------'''
def commit_orser(data):
    url = f'{HOST}/api/order/create/'
    payload = data
    resp = requests.post(url, json=payload)
    return resp.json()

'''-----查询接口------'''
import time
def get_order_result(order_id,interval=5, time_out = 30):
    start_time = time.time()
    end_time = start_time + time_out
    url = f'{HOST}/api/order/get_result__x/'
    # url = f'{HOST}/api/order/get_result/'
    payload = {'order_id': order_id}
    num = 1
    while time.time() <end_time:
        resp = requests.get(url, params=payload)
        if resp.text:
            print('第{cnt}查询，已返回结果，查询结束！--', {resp.text})
            return
        else:
            print(f'第{num}查询，没有返回结果，请稍后查询！')
        time.sleep(interval)
        num += 1
    print('查询超时，请联系平台管理员')
import threading
if __name__ == '__main__':
    start_time = time.time()
    order_date = {
        'user_id': 'sq123456',
        'goods_id': '20200815',
        'num': 1,
        'amount': 200.6
    }
    order_id = commit_orser(order_date)['order_id']
    t1 = threading.Thread(target=get_order_result, args=(order_id,)) #多线程
    t1.daemon = True
    t1.start()
    for i in range(20):
        print(f'{i}---我正在执行主线程的自动化测试用例')
        time.sleep(1)

    end_time = time.time()
    print('自动化执行耗时--->', end_time-start_time)