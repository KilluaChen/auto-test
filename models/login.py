from selenium import webdriver
import time


class Login:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.get("http://127.0.0.1:8011/mgr/sign.html")

    # 登录操作
    def login(self, username, password):
        if username is not None:
            self.wd.find_element_by_id("username").send_keys(username)
        if password is not None:
            self.wd.find_element_by_id("password").send_keys(password)
        self.wd.find_element_by_css_selector("button[type=submit]").click()
        time.sleep(1)

    # 登录检查
    def loginCheck(self, username, password):
        self.login(username, password)
        return self.wd.switch_to.alert.text

    # 登录成功
    def loginOK(self, username, password):
        self.login(username, password)
        text = self.wd.title
        self.wd.quit()
        return text
