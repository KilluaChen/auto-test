from selenium import webdriver
import time


class Login:
    # 登录操作
    def login(self, wd, username, password):
        self.wd = wd
        wd.get("http://127.0.0.1:8011/mgr/sign.html")
        if username is not None:
            wd.find_element_by_id("username").send_keys(username)
        if password is not None:
            wd.find_element_by_id("password").send_keys(password)
        wd.find_element_by_css_selector("button[type=submit]").click()
        time.sleep(1)

    # 登录检查
    def login_check(self, wd, username, password):
        self.login(wd, username, password)
        return wd.switch_to.alert.text

    # 登录成功
    def login_success(self, wd, username, password):
        self.login(wd, username, password)
        text = wd.title
        wd.quit()
        return text
