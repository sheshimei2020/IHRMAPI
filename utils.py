import json
import os

# 编写读取测试数据的函数
def read_login_data():
    login_data_path = os.path.dirname(os.path.abspath(__file__)) + "/data/login_data.json"
    # 打开数据
    with open (login_data_path,'r',encoding='utf-8') as f:
        # 将文件转化为json格式文件
        jsonData = json.load(f)
        # 定义临时存放数据的空列表
        result_list = list()
        # 用for循环遍历jsonData,取出登录数据
        for login_data in jsonData:
            result_list.append(tuple(login_data.values()))

    print(result_list)
    return result_list

if __name__ == '__main__':
    read_login_data()
