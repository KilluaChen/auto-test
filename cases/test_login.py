import time

import pytest
from selenium import webdriver

from models.login import Login


# 登录功能
class TestLogin:
    model = None

    usernameEmpty = "请输入用户名"
    pwdEmpty = "请输入密码"
    loginFail = "登录失败 : 用户名或者密码错误"

    correctUsername = "byhy"
    correctPwd = "88888888"

    @classmethod
    def setup_class(cls):
        cls.model = Login()
        cls.model.driver = webdriver.Chrome()
        cls.model.driver.maximize_window()
        cls.model.driver.implicitly_wait(5)

    @classmethod
    def teardown_class(cls):
        cls.model.driver.quit()

    # 登录失败
    @pytest.mark.parametrize('username,password,expect_text', [
        [None, None, usernameEmpty],
        [None, correctPwd, usernameEmpty],
        [None, "123", usernameEmpty],
        ["123", None, pwdEmpty],
        [correctUsername, None, pwdEmpty],
        [correctUsername, "12341234", loginFail],
        ["1234", correctPwd, loginFail],
        ["12345678910123456789101234567891012345678910", correctPwd, loginFail],
        [correctUsername, "12345678910123456789101234567891012345678910", loginFail],
        ["12345678910123456789101234567891012345678910", "12345678910123456789101234567891012345678910", loginFail],
    ])
    def test_login_fail(self, username, password, expect_text):
        text = self.model.login_check(username, password)
        assert text == expect_text

    # 登录成功
    def test_login_success(self):
        text = self.model.login_success(self.correctUsername, self.correctPwd)
        assert text == "白月销售管理系统"

    # 退出登录
    def test_logout(self):
        self.test_login_success()
        text = self.model.logout()
        assert text == "白月SMS系统 | 登录"
