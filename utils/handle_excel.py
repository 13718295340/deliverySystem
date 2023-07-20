# @Author  dongwukun
# @date  2023/7/7 8:42
# @version  1.0


import xlrd

# def get_excel(filename,sheet_name,case_name,*args):
#     num = []
#     work_book = xlrd.open_workbook(filename)
#     #全部的sheets
#     res = work_book.sheets()
#     work_sheet = work_book.sheet_by_name(sheet_name)
#     col_values = work_sheet.col_values(0)
#     # col_values1 = work_sheet.col_values(0)   #列
#     # print(col_values)
#     # print(col_values1)
#     row_values = work_sheet.row_values(0)
    # row_values1 = work_sheet.row_values(0)    #行
    # print(row_values)
    # print(row_values1)
    # print(res)
    # print(res1)
    # '''-------------获取对应的index值--------------'''
#     col_index = []
#     res = row_values
#     for i in args:
#         col_index.append(res.index(i))
#     print(col_index)
#
#     cc = 0
#     for i in col_values:
#         if case_name in i:
#             aalist = []
#             for j in col_index:
#                 res = work_sheet.cell(cc, j).value
#                 aalist.append(res)
#             num.append(tuple(aalist))
#         cc += 1
#     print(num)
#
#
#
#
#
#
# if __name__ == '__main__':
# #     # res = get_excel('../data/Delivery_System_V1.5.xls','我的订单')
#     res2 = get_excel('../data/Delivery_System_V1.5.xls','我的商铺','listshopping',*['优先级','URI','前置条件'])


def get_excel(filename,sheet_name,case_name,*args,run_case=None):
    num = []
    work_book = xlrd.open_workbook(filename)
    #全部的sheets
    res = work_book.sheets()
    work_sheet = work_book.sheet_by_name(sheet_name)
    col_values = work_sheet.col_values(0)
    # col_values1 = work_sheet.col_values(0)   #列
    # print(col_values)
    # print(col_values1)
    row_values = work_sheet.row_values(0)
    # row_values1 = work_sheet.row_values(0)    #行
    # print(row_values)
    # print(row_values1)
    # print(res)
    '''-------------获取对应的index值--------------'''
    col_index = []
    res = row_values
    for i in args:
        col_index.append(res.index(i))
    print(col_index)

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
                res = work_sheet.cell(cc, j).value
                aalist.append(res)
            num.append(tuple(aalist))
        cc += 1
    print(num)



if __name__ == '__main__':
#     # res = get_excel('../data/Delivery_System_V1.5.xls','我的订单')
    res2 = get_excel('../data/Delivery_System_V1.5.xls','登录模块','Login',*['优先级','标题','URL'],run_case=['all','001','003-004'])   #'all'或者'001'或者'004'任取其一

