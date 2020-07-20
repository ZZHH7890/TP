'''
@Author: joker.zhang
@LastEditors: joker.zhang
@Description: For Automation
@Date: 2019-03-10 22:42:49
@LastEditTime: 2020-07-20 17:49:33
'''

import json
import os
import pytest
import requests
from common.com_log import get_logger
from testData.conftest import get_test_data


# @pytest.mark.skip("skip by pytest.mark.skip!")
@pytest.mark.parametrize('url, method, params', get_test_data())
# def test_api_main(test_case_id, name, url, method, email, pw, project, iteration, su_env, params, checker, next_step, td_env, owner, remark):
def test_api_main(url, method, params):
    test_case_id = os.environ.get('test_case_id')
    # test_case_name = os.environ.get('test_case_name')
    get_logger().info("test_case_id为:%s", test_case_id)
    get_logger().info("url为:%s", url)
    get_logger().info("method为:%s", method)
    get_logger().info("params为:%s", params)
    get_logger().info("params type为:%s", type(json.loads(params)))
    ret = None
    if method == "post":
        ret = requests.post(url, json=json.loads(params))
    get_logger().info("ret为:%s", json.loads(ret.text))
    assert ret
