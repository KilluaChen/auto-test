import pytest


class TestOrder:
    @pytest.mark.dependency(depends=["login"], scope="session")
    def test_order_list(self, drivers):
        print("\n\n****************")
        print(drivers.title)
        print("OrderList")
        assert True
