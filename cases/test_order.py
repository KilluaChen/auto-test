import pytest

from models.order import Order


class TestOrder:
    model = None

    @classmethod
    def setup_class(cls):
        """
        先登录
        :return:
        """
        from cases.test_login import TestLogin
        tl = TestLogin()
        tl.setup_class()
        tl.test_login_success()

        """
        初始化订单
        """
        cls.model = Order()
        cls.model.driver = tl.model.driver

    @classmethod
    def teardown_class(cls):
        cls.model.driver.quit()

    @pytest.mark.dependency(depends=["login"], scope="session")
    def test_order_list(self):
        self.model.list()
        print(self.model.driver.title)
        print("OrderList")
        assert True
