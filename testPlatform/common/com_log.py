'''
@Author: joker.zhang
@LastEditors: joker.zhang
@Description: For Automation
@Date: 2019-03-10 21:52:18
@LastEditTime: 2020-07-20 17:07:33
'''
import os
import logging
from common.com_utils import get_now_time, get_folder_path


def get_logger():
    # 创建一个logger
    logger = logging.getLogger(__name__)
    log_path = get_folder_path("testResult\\Log")
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    logfile = log_path + "\\" + get_now_time() + ".log"
    if not logger.handlers:
        # log等级总开关
        logger.setLevel(logging.INFO)
        # 创建一个file_handler,指定utf-8
        fh = logging.FileHandler(logfile, mode='a', encoding='utf-8')
        # 输出到file的log等级开关
        fh.setLevel(logging.DEBUG)
        # 定义file_handler的输出格式
        formatter = logging.Formatter(
            '%(asctime)s %(levelname)s %(message)s %(filename)s[line:%(lineno)d] %(funcName)s ')
        fh.setFormatter(formatter)
        # 将file_handler添加到logger
        logger.addHandler(fh)
    return logger


# if __name__ == '__main__':
#    print("")
