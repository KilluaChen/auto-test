import time


class Order:
    driver = None

    def list(self):
        self.driver.get("http://127.0.0.1:8011/mgr/index.html#/")
        self.driver.find_element_by_css_selector('#root > aside > section > ul > li:nth-child(4) > a').click()
        time.sleep(1)
