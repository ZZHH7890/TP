'''
@Author: joker.zhang
@LastEditors: joker.zhang
@Description: For Automation
@Date: 2019-03-11 17:24:17
@LastEditTime: 2020-07-20 16:19:21
'''

from common.com_log import get_logger


def assert_equals(expect_value, actual_value):
    """
    EQ:判断预期值是否等于实际值
    """
    if isinstance(actual_value, list):
        if expect_value == str(actual_value[0]):
            return True
        else:
            return False

    # 判断实际请求中无某个参数返回的场景
    elif isinstance(actual_value, str):
        if expect_value == str(actual_value):
            return True
        else:
            return False


def assert_length_of_str(expect_value, actual_value):
    """
    LOS: 判断预期值是否等于实际值的长度
    实际值返回的是字符串或者数组
    """
    if isinstance(actual_value[0], str):
        if expect_value == len(actual_value[0]):
            return True
        else:
            return False
    elif isinstance(actual_value[0], list):
        if expect_value == len(str(actual_value[0][0])):
            return True
        else:
            return False


def assert_length_of_list(expect_value, actual_value):
    """
    LOL:判断预期值是否等于实际值的长度
    实际值返回的是数组
    """
    if isinstance(actual_value[0], list):
        if expect_value == str(len(actual_value[0])):
            return True
        else:
            return False


def assert_number(expect_value, actual_value):
    """
    NUM: 判断预期值是否等于实际值的个数

    """
    if isinstance(actual_value, list):

        if expect_value == str(len(actual_value)):
            return True
        else:
            return False


def assert_not_in_list(expect_value, actual_value):
    """
    LEN: 判断预期值不在实际值中
    """
    if isinstance(actual_value, list):
        if expect_value in actual_value:
            get_logger().info("=============expect_value in actual_value==============")
            return False
        else:
            get_logger().info(
                "=============expect_value not in actual_value==============")
            return True


def assert_in_list(expect_value, actual_value):
    """
    IL: 判断预期值在实际值中
    """
    if expect_value in actual_value:
        get_logger().info("=============expect_value in actual_value==============")
        return True
    else:
        get_logger().info(
            "=============expect_value not in actual_value==============")
        return False


def assert_api(expect_value, actual_value, compare_type):
    if compare_type == 'NUM':
        return assert_number(expect_value, actual_value)
    elif compare_type == 'LOS':
        return assert_length_of_str(expect_value, actual_value)
    elif compare_type == 'LOL':
        return assert_length_of_list(expect_value, actual_value)
    elif compare_type == 'EQ':
        return assert_equals(expect_value, actual_value)
    elif compare_type == 'NIL':
        return assert_not_in_list(expect_value, actual_value)
    elif compare_type == 'IL':
        return assert_in_list(expect_value, actual_value)
