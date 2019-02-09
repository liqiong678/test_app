from selenium.webdriver.support.wait import WebDriverWait
class Base:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc, timeout = 50, poll = 0.5):

        """
        :param loc: 定位方式 By.XPATH
        :param loc_value: 定位的属性值 本身需要两个参数，作为原组进来在解包
        变为，loc:原组类型 定位方式+属性值 类似(By.XPATH,"XPATH语句")-》(By.ID,"id属性值")
        :return: return 一下就可以拿到定位对象
        self.driver.find_element(By.XPATH, "//*[contains(@text,'WLA')]").click()
         self.webDriverWait(self.driver,30,1).until(lambda x: x.find_elemen_by_id())
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def click_element(self, loc):
        # loc原组类型 self.find_element(loc) 调用def find_element(self, loc, timeout = 10, poll = 0.5)，
        # 不需要加* 号了,传个原组进来就可以啦
        self.find_element(loc).click()

    def input_element(self, loc, text):
        """

        :param loc: 原组类型（类似(By.XPATH,"XPATH语句")-》(By.ID,"id属性值")
        # 定位原组只管定位原组，text需要另外传
        :param text: 输入的内容值
        :return:
        """
        self.find_element(loc).send_keys(text)

    def teardown(self):
        self.driver.quit()



