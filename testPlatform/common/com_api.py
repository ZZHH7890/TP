
import json
import time
import requests
from common.com_log import get_logger
from common.com_dict import OperateDict
from common.com_assert import assert_api


class API(object):

    @classmethod
    def request_method(cls, url, method, param=None, **kwargs):
        """
        方法作用：封装不同类型的请求方法
        url: 接口请求地址url
        method: 请求的方法
        param: 请求参数
        kwargs: 其他需要的kwargs
        ret: 请求返回数据
        """
        get_logger().info("Request URL:%s", url)
        get_logger().info("Request METHOD:%s", method)
        ret = None
        if method == "POST" or method == "post":
            ret = requests.post(url, param, **kwargs)
        elif method == "GET" or method == "get":
            ret = requests.get(url, param, **kwargs)
        elif method == "DELETE" or method == "delete":
            ret = requests.delete(url, **kwargs)
        elif method == "PUT" or method == "put":
            ret = requests.put(url, param, **kwargs)

        if ret.status_code == 500:
            get_logger().info("Server Internal Error 500")
            return "Server Internal Error 500"
        elif ret.status_code == 404:
            get_logger().info("Cannot find the page 404")
            return "Cannot find the page 404"
        else:
            get_logger().info("Response data:%s", json.dumps(
                json.loads(ret.text), sort_keys=True, indent=2))
            return json.loads(ret.text)

    @classmethod
    def get_api_response_data(cls, url, method, params=None, cookies=None, headers=None, files=None):
        """
        url: 接口请求地址url
        method: 请求的方法
        param: 请求参数
        kwargs: 其他需要的kwargs
        ret: 请求返回数据
        """
        get_logger().info("Request PARAM:%s", params)
        if cookies:
            get_logger().info("Request COOKIES:%s", cookies)
        if headers:
            get_logger().info("Request HEADERS:%s", headers)
        ret = None
        if method == "POST" or method == "post":
            # 上传文件操作，提交数据参数方式不同处理；content={请求参数格式}
            if files:
                get_logger().info("Request FILES:%s", files)
                datas = {}
                datas['content'] = params
                ret = cls.request_method(url, method, datas, cookies=json.loads(
                    cookies), headers=headers, files=files)
            else:
                if cookies:
                    ret = cls.request_method(url, method, json=json.loads(
                        params), cookies=json.loads(cookies), headers=headers)
                else:
                    ret = cls.request_method(
                        url, method, json=json.loads(params), headers=headers)
            return ret

    @classmethod
    def get_next_step_value(cls, api_response, set_up):
        """
        for api multi-business get next step test data 
        """
        next_step_dict = {}
        temp_dict = json.loads(set_up)["next_step"]
        for key in temp_dict.keys():
            k_v = temp_dict[key]
            v = OperateDict.get_value_in_dict(key, api_response, [])[0]
            if isinstance(k_v, list):
                k_v_v = k_v[0]
                next_step_dict[k_v_v] = [v]
            else:
                next_step_dict[k_v] = v
        get_logger().info("next_step_value:(%s)", next_step_dict)
        return json.dumps(next_step_dict)

    @classmethod
    def set_last_step_value(cls, dic, target_dic):
        """
        For update post json from last step, set last step test data into current step
        """
        target_dic = OperateDict.update_value_in_dict(target_dic, dic)
        return json.dumps(target_dic)

    @classmethod
    def update_param(cls, dic, target_dic):
        """
        For update post json from set_up:update_params, for example: Compare current date test case
        """
        now_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        for key in dic.keys():
            if dic[key] == "now_date":
                dic[key] = now_date
        target_dic = OperateDict.update_value_in_dict(target_dic, dic)
        return json.dumps(target_dic)

    @classmethod
    def checker_api(cls, api_response, checkers):
        """
        For api assert
        """
        flag = True
        checkers_list = list(json.loads(checkers)["checkers"])
        for checker in checkers_list:
            expect_key = checker["k"]
            expect_value = checker["v"]
            compare_type = checker["ct"]
            actual_value = OperateDict.get_value_in_dict(
                expect_key, api_response, [])
            get_logger().info("actual_value:(%s:%s:%s)", expect_key,
                              actual_value, type(actual_value[0]))
            get_logger().info("expect_value:(%s:%s:%s)",
                              expect_key, expect_value, type(expect_value))
            flag = assert_api(expect_value, actual_value, compare_type)
            if flag == False:
                get_logger().info("Fail:<%s>", checker)
                break
        return flag

    @classmethod
    def get_user_cookies(cls, user_email, user_password):
        """ get user cookies
        """
        url = "https://user.17track.net/userapi/call"
        data = {"Version": "1.0", "Method": "Signin", "Param": {
            "Email": user_email, "Password": user_password}}
        r = requests.post(url, json=data)
        cookies = r.cookies.get_dict()
        return str(json.dumps(cookies))

# if __name__ == '__main__':

#     param = {"version":"1.0", "method":"SearchChannel", "param":{"w":"1", "s":"10"}}
#     API.get_value_by_key('version',param)
#     ret = API.get_api_response_data("https://freight.17track.net/searchapi/call", "post", param)
#     print(ret)
