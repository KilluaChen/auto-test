import time


class Order:
    driver = None

    def list(self):
        self.driver.get("http://127.0.0.1:8011/mgr/index.html#/")
        self.driver.find_element_by_css_selector('#root > aside > section > ul > li:nth-child(4) > a').click()
        time.sleep(1)

    # 创建订单
    def add(self, name, custom, drug):
        self.driver.find_element_by_css_selector(".content button[type=button]").click()
        prefix = '//*[@id="root"]/div/section[2]/div[1]/'
        self.driver.find_element_by_xpath(prefix + 'div[1]/div[1]/input').send_keys(name)
        self.driver.find_element_by_xpath(prefix + 'div[1]/div[2]/input').send_keys(custom + "\n")
        self.driver.find_element_by_xpath(prefix + 'div[1]/div[3]/input').send_keys(drug + "\n")

        self.driver.find_element_by_xpath(prefix + 'div[1]/div[2]/select/option[1]').click()
        self.driver.find_element_by_xpath(prefix + 'div[1]/div[3]/select/option[1]').click()

        self.driver.find_element_by_xpath(prefix + 'div[1]/div[3]/div/input').send_keys(2)
        self.driver.find_element_by_xpath(prefix + 'div[2]/button[1]').click()
        pass
