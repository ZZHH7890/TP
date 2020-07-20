'''
@Author: joker.zhang
@Date: 2020-07-17 11:25:03
@LastEditors: joker.zhang
@LastEditTime: 2020-07-20 17:07:16
@Description: For Automation
'''
import os
from common.com_utils import get_folder_path


class OperateTestRunner():
    """测试执行相关
    """
    @classmethod
    def get_report(cls):
        """ 获取测试报告,用于pytest cmd
        """
        report_path = get_folder_path("\\testResult\\Report")
        if not os.path.exists(report_path):
            os.makedirs(report_path)
        report_name = "Report" + ".html"
        return report_path + "\\" + report_name

    @classmethod
    def get_test_case(cls, folder_name):
        """生成需要运行的用例文件夹
        """
        test_case_folder = get_folder_path("testCases") + "\\" + folder_name
        return test_case_folder

    @classmethod
    def get_pytest_cmd(cls):
        """ 获取pytest命令行
        """
        pytest_cmd = []
        pytest_cmd.append(cls.get_test_case('API'))
        pytest_cmd.append('-q')
        report_path = '--html=' + cls.get_report()
        pytest_cmd.append(report_path)
        return pytest_cmd
