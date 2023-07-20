# @Author  dongwukun
# @date  2023/7/10 14:28
# @version  1.0
import json
import yaml
import xlrd
import yaml



def get_excel(sheet_name,case_name,*args,run_case=None):
    num = []

    if run_case is None:
        run_case = ['all']
    filename = '../data/Delivery_System_V1.5.xls'
    #调用yaml文件读取数据
    work_book = xlrd.open_workbook(filename)
    #全部的sheets
    # res = work_book.sheets()
    work_sheet = work_book.sheet_by_name(sheet_name)
    # col_values = work_sheet.col_values(0) #列
    row_values = work_sheet.row_values(0) #行
    '''-----获取对应的index值-----'''
    col_index = []
    res = row_values
    for i in args:
        col_index.append(res.index(i))
    # print(col_index)

    run_case_list = []
    if 'all' in run_case:
        run_case_list = work_sheet.col_values(0)
    else:
        for one in run_case:
            if '-' in one:
                start, end = one.split('-')
                for k in range(int(start), int(end)+1):
                    run_case_list.append(case_name+f'{k:0>3}')
            else:
                run_case_list.append(case_name+f'{one:0>3}')



    cc = 0
    for d in work_sheet.col_values(0):
        if case_name in d and d in run_case_list:
            aalist = []
            for j in col_index:
                res = is_json(work_sheet.cell(cc, j).value)
                aalist.append(res)
            num.append(tuple(aalist))
        cc += 1

    return num


def is_json(in_str):
    try:
        return json.loads(in_str)
    except:
        return in_str



if __name__ == '__main__':
    # res1 = get_excel('../data/Delivery_System_V1.5.xls','登录模块','Login',*['用例编号','优先级','标题','URL'],run_case=['all'])  #这几个任意取其一
    # res2 = get_excel('../data/Delivery_System_V1.5.xls','我的商铺','listshopping',*['优先级','标题','URI','请求参数'],run_case=['all'])  #这几个任意取其一
    res3 = get_excel('登录模块', 'Login', '请求参数', '响应预期结果')
    print(res3)