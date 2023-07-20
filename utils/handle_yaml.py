# @Author  dongwukun
# @date  2023/7/6 10:05
# @version  1.0

import yaml
def get_yaml_data():
    path = '../conflgs/apiPathConfig.yml'
    with open(path, encoding='utf-8') as f:
        res = yaml.safe_load(f.read())

    return res

if __name__ == '__main__':
    # path = '../conflgs/apiPathConfig.yml'
    res = get_yaml_data()
    print(res)

# def get_yaml_data1():
#     numm = '../conflgs/apiPathConfig.yml'
#     with open(numm, encoding='utf-8') as m:
#         res = yaml.safe_load(m.read())
#
#     return res
#
# if __name__ == '__main__':
#     ress = get_yaml_data1()
#     print(ress)