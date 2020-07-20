'''
@Author: joker.zhang
@Date: 2020-07-20 14:31:25
@LastEditors: joker.zhang
@LastEditTime: 2020-07-20 23:50:35
@Description: For Automation
'''
import os
from tpTest.models import TestCaseInfo
from common.com_log import get_logger


def change_list_to_str():
    test_case_id = None
    temp = os.environ.get('test_case_id')
    if ',' in temp:
        test_case_id = temp.split(',')
    else:
        test_case_id = temp
    return test_case_id


# def get_test_data():
#     test_case = TestCaseInfo.objects.get(id=TEST_CASE_ID)
#     get_logger().info("TEST_CASE:%s", test_case)
#     data_list = []
#     data_tuple = (test_case.url, test_case.method, test_case.params)
#     data_list.append(data_tuple)
#    return data_list

def get_test_data():
    data_list = []
    tc_id = change_list_to_str()
    test_case = None
    get_logger().info("需要执行的用例为:%s %s", tc_id, type(tc_id))
    if isinstance(tc_id, str):
        test_case = TestCaseInfo.objects.get(id=tc_id)
        data_tuple = (test_case.url, test_case.method, test_case.params)
        data_list.append(data_tuple)
    elif isinstance(tc_id, list):
        for i in tc_id:
            data_tuple = ()
            if i != '':
                test_case = TestCaseInfo.objects.get(id=i)
                data_tuple = (test_case.url, test_case.method,
                              test_case.params)
                data_list.append(data_tuple)
        get_logger().info("测试数据为:%s", data_list)

    else:
        get_logger().info("获取数据conftest.py出错")
    return data_list
