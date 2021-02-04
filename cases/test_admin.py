from test_login import TestLogin
import time


# 测试管理员账号增删改查
class TestAdmin:

    # 正确的账号密码登录
    def test_AdminCheck(self):
        login = TestLogin()
        login.setup_method()
        login.login()

        login.wd.find_element_by_css_selector(".add-one-area button").click()
        els = login.wd.find_elements_by_css_selector(".add-one-area > .col-sm-8 div")
        for k, el in enumerate(els):
            if k == 0:
                assert el.text == "客户名"
            elif k == 1:
                assert el.text == "联系电话"
            elif k == 2:
                assert el.text == "地址"
        login.teardown_method()
        assert True

    # 编辑账号
    def test_AdminEdit(self):
        login = TestLogin()
        login.setup_method()
        login.login()

        login.wd.find_element_by_css_selector("[placeholder=请输入关键词搜索]").send_keys("南京中医院")
        login.wd.find_element_by_css_selector("#btn_search_exams").click()

        assert len(login.wd.find_elements_by_css_selector(".content .search-result-item")) > 0

        time.sleep(3)
        login.teardown_method()
        assert True
