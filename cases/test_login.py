from selenium import webdriver
import time


class TestLogin:

    # 初始化
    def setup_method(self):
        self.wd = webdriver.Chrome()
        self.wd.get("http://127.0.0.1:8011/mgr/sign.html")
        # self.wd.maximize_window()

    # 释放资源
    def teardown_method(self):
        self.wd.quit()

    # 不输入用户名
    def test_UI0001(self):
        self.wd.find_element_by_id("password").send_keys("88888888")
        self.wd.find_element_by_css_selector("button[type=submit]").click()
        time.sleep(1)
        text = self.wd.switch_to.alert.text
        print(text)
        assert text == "请输入用户名"

    # 不输入密码
    def test_UI0002(self):
        self.wd.find_element_by_id("username").send_keys("byhy")
        self.wd.find_element_by_css_selector("button[type=submit]").click()
        time.sleep(1)
        text = self.wd.switch_to.alert.text
        print(text)
        assert text == "请输入密码"

    # 错误的账号
    def test_UI0003(self):
        self.wd.find_element_by_id("username").send_keys("byh")
        self.wd.find_element_by_id("password").send_keys("88888888")
        self.wd.find_element_by_css_selector("button[type=submit]").click()
        time.sleep(1)
        text = self.wd.switch_to.alert.text
        print(text)
        assert text == "登录失败 : 用户名或者密码错误"

    # 错误的密码
    def test_UI0004(self):
        self.wd.find_element_by_id("username").send_keys("byhy")
        self.wd.find_element_by_id("password").send_keys("666666")
        self.wd.find_element_by_css_selector("button[type=submit]").click()
        time.sleep(1)
        text = self.wd.switch_to.alert.text
        print(text)
        assert text == "登录失败 : 用户名或者密码错误"

    # 登录逻辑
    def login(self):
        self.wd.find_element_by_id("username").send_keys("byhy")
        self.wd.find_element_by_id("password").send_keys("88888888")
        self.wd.find_element_by_css_selector("button[type=submit]").click()
        time.sleep(1)
        return self.wd.title

    # 正确的账号密码登录
    def test_UI0005(self):
        text = self.login()
        print(text)
        assert text == "白月销售管理系统a"

    # 退出登录
    def test_UI0006(self):
        text = self.login()
        if text != "白月销售管理系统":
            assert False
        self.wd.find_element_by_css_selector('.user-image').click()
        self.wd.find_element_by_css_selector('.pull-right > .btn-flat').click()
        time.sleep(1)
        text = self.wd.title
        print(text)
        assert text == "白月SMS系统 | 登录"
