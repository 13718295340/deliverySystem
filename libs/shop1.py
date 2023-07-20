# @Author  dongwukun
# @date  2023/7/12 19:05
# @version  1.0

from common.baseAPI import BaseApi
from libs.login import Login


class Shop(BaseApi):
    def update(self, data, shop_id, image_info):
        if data['id'] != '0000':
            data['id'] = shop_id

        data['image_path'] = image_info
        data['image'] = f'/file/getImgStream?fileName={image_info}'

        return super(Shop, self).update(data)

'''编辑商铺'''
if __name__ == '__main__':
    #先是登录
    test_data = {
        'username': 'ct0958',
        'password': '14443'
    }
    token = Login().login(test_data, get_token=True)
    #然后是店铺实例
    shop = Shop(token)
    #再是列出商铺
    data = {
        'page': 1,
        'limit': 20
    }
    shop_res = shop.query(test_data)
    print('列出商铺信息----->', shop_res)
    #然后获取店铺id
    shop_id = shop_res['data']['records'][0]['id']
    print('店铺id----->', shop_id)
    #文件上传接口
    image_info = shop.file_upload('../data/123.jpg')
    print('列出图片信息------>', image_info)
    image_infos = image_info['data']['realFileName']
    print('列出图片详细信息------>', image_infos)
    #店铺更新
    update_data = {
        "name": "星巴克新建店",
                "address": "上海市静安区秣陵路303号",
                "id": "id",
                "Phone": "13176876632",
                "rating": "6.0",
                "recent_order_num": 100,
                "category": "快餐便当/简餐",
                "description": "满30减5，满60减8",
                "image_path": "b8be9abc-a85f-4b5b-ab13-52f48538f96c.png",
                "image": "http://121.41.14.39:8082/file/getImgStream?fileName=b8be9abc-a85f-4b5b-ab13-52f48538f96c.png"
    }
    Edit = shop.update(update_data, shop_id, image_infos)
    print(Edit)