import time


class Login:
    driver = None

    # 登录操作
    def login(self, username, password):
        self.driver.get("http://127.0.0.1:8011/mgr/sign.html")
        if username is not None:
            self.driver.find_element_by_id("username").send_keys(username)
        if password is not None:
            self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_css_selector("button[type=submit]").click()
        time.sleep(1)

    # 登录失败
    def login_check(self, username, password):
        self.login(username, password)
        text = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        return text

    # 登录成功
    def login_success(self, username, password):
        self.login(username, password)
        return self.driver.title

    # 退出登录
    def logout(self):
        self.driver.find_element_by_css_selector(".user-image").click()
        self.driver.find_element_by_css_selector(".user-footer > .pull-right a").click()
        time.sleep(1)
        return self.driver.title
