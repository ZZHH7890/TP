'''
@Author: joker.zhang
@LastEditors: joker.zhang
@Description: For Automation
@Date: 2019-03-10 22:42:49
@LastEditTime: 2020-07-18 23:20:53
'''

import json
import os
from common.log import get_logger


# @pytest.mark.skip("skip by pytest.mark.skip!")
def test_api_main():
    test_case_id = os.environ.get('test_case_id')
    # test_case_name = os.environ.get('test_case_name')
    test_case_set_up = os.environ.get('test_case_set_up')
    # test_case_params = os.environ.get('test_case_params')
    # test_case_checkers = os.environ.get('test_case_checkers')
    # test_case_next_step = os.environ.get('test_case_next_step')
    # test_case_project = os.environ.get('test_case_project')
    # test_case_version = os.environ.get('test_case_version')
    # test_case_owner = os.environ.get('test_case_owner')
    # test_case_remark = os.environ.get('test_case_remark')
    # test_case_set_up_dict = json.loads(test_case_set_up)
    test_case_set_up_dict = json.loads(test_case_set_up)
    get_logger().info("test_case_id为:%s", test_case_id)
    url = test_case_set_up_dict["config"]["url"]
    get_logger().info("url为:%s", url)