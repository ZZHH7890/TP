'''
@Author: joker.zhang
@LastEditors: joker.zhang
@Description: For Automation
@Date: 2019-04-15 16:03:35
@LastEditTime: 2020-07-20 16:13:36
'''


class OperateDict(object):
    @classmethod
    def update_value_in_dict(cls, target_dict, data_dict):
        """
        :target_dict:需要修改的字典
        :data_dict:需要塞入 target_dict的值
        :return:修改后的 target_dict
        """
        if not isinstance(target_dict, dict) and not isinstance(data_dict, dict):  # 对传入数据进行格式校验
            return 'get_value_in_dict: parameter error'

        for data_key in data_dict.keys():
            for target_key in target_dict.keys():
                if data_key == target_key:
                    target_dict[target_key] = data_dict[data_key]
                else:
                    for value in target_dict.values():
                        if isinstance(value, dict):
                            cls.update_value_in_dict(value, data_dict)
                        elif isinstance(value, (list, tuple)):
                            cls._update_value(value, data_dict)
        return target_dict

    @classmethod
    def _update_value(cls, val, data_dict):
        for val_ in val:
            if isinstance(val_, dict):
                cls.update_value_in_dict(val_, data_dict)
            elif isinstance(val_, (list, tuple)):
                cls._update_value(val_, data_dict)  # 传入数据的val_值是列表或者元组，则调用自身

    @classmethod
    def get_value_in_dict(cls, key, dic, tmp_list):
        """
        :key: 目标key值
        :dic: JSON数据
        :tmp_list: 用于存储获取的数据
        :return: list
        """
        if not isinstance(dic, dict) or not isinstance(tmp_list, list):  # 对传入数据进行格式校验
            return 'get_value_in_dict: parameter error'

        if key in dic.keys():
            tmp_list.append(dic[key])  # 传入数据存在则存入tmp_list
        else:
            for value in dic.values():  # 传入数据不符合则对其value值进行遍历
                if isinstance(value, dict):
                    # 传入数据的value值是字典，则直接调用自身
                    cls.get_value_in_dict(key, value, tmp_list)
                elif isinstance(value, (list, tuple)):
                    # 传入数据的value值是列表或者元组，则调用_get_value
                    cls._get_value(key, value, tmp_list)
        if len(tmp_list) > 0:
            return tmp_list
        else:
            return "Cannot find the key value"

    @classmethod
    def _get_value(cls, key, val, tmp_list):
        for val_ in val:
            if isinstance(val_, dict):
                # 传入数据的value值是字典，则调用get_target_value
                cls.get_value_in_dict(key, val_, tmp_list)
            elif isinstance(val_, (list, tuple)):
                cls._get_value(key, val_, tmp_list)  # 传入数据的value值是列表或者元组，则调用自身

# if __name__ == '__main__':
#     a_dict ={"version":"1.0","method":"deltrackno","param":{"isa":0,"Items":[{"no":"","tid":""}]},"sourcetype":0,"timeZoneOffset":-480}
#     b_dict = {"sourcetype":"1111111111","tid":"22222222"}
#     print(OperateDict.update_value_in_dict(a_dict, b_dict))
#     print(OperateDict.get_value_in_dict("tid",a_dict,[]))
