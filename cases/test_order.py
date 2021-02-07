import pytest


class TestOrder:
    @pytest.mark.dependency(depends=["login"], scope="session")
    def test_OrderList(self):
        print("OrderList")
        assert True
