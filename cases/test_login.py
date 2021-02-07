from models.login import *


class TestLogin:

    # 不输入用户名和密码
    def test_LoginFail001(self):
        text = loginCheck(None, None)
        assert text == "请输入用户名"

    # 不输入用户名,错误密码
    def test_LoginFail002(self):
        text = loginCheck(None, "123")
        assert text == "请输入用户名"

    # 不输入用户名,正确密码
    def test_LoginFail003(self):
        text = loginCheck(None, "88888888")
        assert text == "请输入用户名"

    # 错误用户名,不输入密码
    def test_LoginFail004(self):
        text = loginCheck("123", None)
        assert text == "请输入密码"

    # 正确用户名,不输入密码
    def test_LoginFail005(self):
        text = loginCheck("byhy", None)
        assert text == "请输入密码"

    # 错误用户名,正确密码
    def test_LoginFail006(self):
        text = loginCheck("1234", "88888888")
        assert text == "登录失败 : 用户名或者密码错误"

    # 正确用户名,错误密码
    def test_LoginFail007(self):
        text = loginCheck("byhy", "12341234")
        assert text == "登录失败 : 用户名或者密码错误"

    # 超长用户名,正常密码
    def test_LoginFail008(self):
        text = loginCheck("12345678910123456789101234567891012345678910", "12341234")
        assert text == "登录失败 : 用户名或者密码错误"

    # 正常用户名,超长密码
    def test_LoginFail009(self):
        text = loginCheck("byhy", "12345678910123456789101234567891012345678910")
        assert text == "登录失败 : 用户名或者密码错误"

    # 超长用户名,超长密码
    def test_LoginFail010(self):
        text = loginCheck("12345678910123456789101234567891012345678910",
                          "12345678910123456789101234567891012345678910")
        assert text == "登录失败 : 用户名或者密码错误"

    # 正确用户名,正确密码
    def test_LoginOk001(self):
        text = loginOK("byhy", "88888888")
        print(text)
        assert text == "白月销售管理系统"
