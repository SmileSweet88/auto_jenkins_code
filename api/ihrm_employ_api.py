# encoding = utf-8
from constant import constant
from constant.constant import iHrm_user


class IhrmEmploy:

    def get_token(self):
        return {"Authorization": "Bearer " + constant.GrobleToken}

    def add_employ(self, session, data):
        return session.post(iHrm_user, json=data, headers=self.get_token())

    def modify_employ(self, session, empId, data):
        return session.put(iHrm_user + empId, json=data, headers=self.get_token())

    def find_employ(self, session, empId):
        return session.get(iHrm_user + empId, headers=self.get_token())

    def del_employ(self, session, empId):
        return session.delete(iHrm_user + empId, headers=self.get_token())
