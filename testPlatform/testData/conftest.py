'''
@Author: joker.zhang
@Date: 2020-07-20 14:31:25
@LastEditors: joker.zhang
@LastEditTime: 2020-07-20 19:38:55
@Description: For Automation
'''
import os
from tpTest.models import TestCaseInfo
from common.com_log import get_logger

TEST_CASE_ID = os.environ.get('test_case_id')
get_logger().info("需要执行的用例为:%s", TEST_CASE_ID)


# def get_test_data():
#     test_case = TestCaseInfo.objects.get(id=TEST_CASE_ID)
#     get_logger().info("TEST_CASE:%s", test_case)
#     data_list = []
#     data_tuple = (test_case.url, test_case.method, test_case.params)
#     data_list.append(data_tuple)
#    return data_list

def get_test_data():
    data_list = []
    data_tuple = ()
    if isinstance(TEST_CASE_ID, str):
        test_case = TestCaseInfo.objects.get(id=TEST_CASE_ID)
        get_logger().info("TEST_CASE:%s", test_case)
        data_tuple = (test_case.url, test_case.method, test_case.params)
        data_list.append(data_tuple)
    elif isinstance(TEST_CASE_ID, list):
        for i in TEST_CASE_ID:
            if i != '':
                TestCaseInfo.objects.get(id=i)
                data_tuple = (test_case.url, test_case.method, test_case.params)
                data_list.append(data_tuple)
    else:
        get_logger().info("获取数据conftest.py出错")
    return data_list
