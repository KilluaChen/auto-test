from selenium import webdriver
import time


class Login:
    # 登录操作
    def login(self, username, password):
        self.wd = webdriver.Chrome()
        self.wd.get("http://127.0.0.1:8011/mgr/sign.html")
        if username is not None:
            self.wd.find_element_by_id("username").send_keys(username)
        if password is not None:
            self.wd.find_element_by_id("password").send_keys(password)
        self.wd.find_element_by_css_selector("button[type=submit]").click()
        time.sleep(1)

    # 登录检查
    def login_check(self, username, password):
        self.login(username, password)
        return self.wd.switch_to.alert.text

    # 登录成功
    def login_success(self, username, password):
        self.login(username, password)
        text = self.wd.title
        self.wd.quit()
        return text
