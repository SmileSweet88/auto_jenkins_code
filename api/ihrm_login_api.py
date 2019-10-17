import requests

from constant import constant
from constant.constant import iHrm_BaseUrl


class IhrmLogin:
    """登录"""

    def ihm_login(self, session, mobile, password):
        data_json = {"mobile": mobile, "password": password}
        response = session.post(iHrm_BaseUrl + "/api/sys/login", json=data_json)
        constant.GrobleToken = response.json().get("data")
        print("登录成功之后保存了token: ",constant.GrobleToken)
        return response
