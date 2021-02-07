import time

import pytest

from models.login import Login


# 登录功能
class TestLogin:
    usernameEmpty = "请输入用户名"
    pwdEmpty = "请输入密码"
    loginFail = "登录失败 : 用户名或者密码错误"

    correctUsername = "byhy"
    correctPwd = "88888888"

    def setup_method(self):
        print("\n前置前置前置前置前置前置前置前置前置前置前置前置前置前置前置前置前置前置\n")
        self.aaa = Login()

    def teardown_method(self):
        print(self.aaa.wd.title)
        print("\n后置后置后置后置后置后置后置后置后置后置后置后置后置后置后置后置后置后置\n")
        self.aaa.wd.quit()

    # # 登录失败
    # @pytest.mark.parametrize('username,password,text', [
    #     [None, None, usernameEmpty],
    #     [None, correctPwd, usernameEmpty],
    #     [None, "123", usernameEmpty],
    #     ["123", None, pwdEmpty],
    #     [correctUsername, None, pwdEmpty],
    #     [correctUsername, "12341234", loginFail],
    #     ["1234", correctPwd, loginFail],
    #     ["12345678910123456789101234567891012345678910", correctPwd, loginFail],
    #     [correctUsername, "12345678910123456789101234567891012345678910", loginFail],
    #     ["12345678910123456789101234567891012345678910", "12345678910123456789101234567891012345678910", loginFail],
    # ])
    # def test_login_fail(self, wd, username, password, text):
    #     rst = self.login.login_check(wd, username, password)
    #     assert rst == text

    # 登录成功
    @pytest.mark.dependency(name="login")
    def test_login_ok(self, drivers):
        self.aaa.login(drivers, self.correctUsername, self.correctPwd)
        assert drivers.title == "白月销售管理系统"
