'''
@Author: joker.zhang
@LastEditors: joker.zhang
@Description: For Automation
@Date: 2019-02-15 11:44:36
@LastEditTime: 2020-07-16 23:07:51
'''

import time
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath('.')))


def get_now_time():
    """ 获取当前日期
    """
    now_time = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    return now_time


def get_current_path():
    """ 获取当前路径
    """
    current_path = os.path.abspath('.')
    return current_path


def get_folder_path(folder_name):
    """ 获取指定文件夹路径
    """
    folder_path = get_current_path() + "\\" + folder_name
    return folder_path
