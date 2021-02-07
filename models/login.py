from selenium import webdriver
import time


# 登录操作
def login(username, password):
    wd = webdriver.Chrome()
    wd.get("http://127.0.0.1:8011/mgr/sign.html")
    if username is not None:
        wd.find_element_by_id("username").send_keys(username)
    if password is not None:
        wd.find_element_by_id("password").send_keys(password)
    wd.find_element_by_css_selector("button[type=submit]").click()
    time.sleep(1)
    return wd


# 登录检查
def loginCheck(username, password):
    wd = login(username, password)
    text = wd.switch_to.alert.text
    wd.quit()
    return text


# 登录成功
def loginOK(username, password):
    wd = login(username, password)
    text = wd.title
    wd.quit()
    return text
