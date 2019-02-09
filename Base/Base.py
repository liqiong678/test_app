from selenium.webdriver.support.wait import WebDriverWait


class Base:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc, loc_value, timeout = 10, poll = 0.5):

        """
        :param loc: 定位方式 By.XPATH
        :param loc_value: 定位的属性值
        :return: return 一下就可以拿到定位对象
        self.driver.find_element(By.XPATH, "//*[contains(@text,'WLA')]").click()
         self.webDriverWait(self.driver,30,1).untill(lambda x: x.find_elemen_by_id())
        """
        return WebDriverWait(self.driver, timeout, poll).untill(lambda x: x.find_element(loc, loc_value))

    def click_element(self, loc, loc_value):
        self.find_element(loc, loc_value).click()

    def input_element(self, loc, loc_value, text):
        """

        :param loc:
        :param loc_value:
        :param text: 输入的内容值
        :return:
        """
        self.find_element(loc, loc_value).send_keys(text)

    def teardown(self):
        self.driver.quit()



