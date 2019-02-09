import sys, os
sys.path.append(os.getcwd())
from page.search import Search_page
from appium import webdriver
from Base.Base1 import Base

class Test_search2:
      # 【1】初始化，生成driver
    def setup(self):
        desired_caps = {}
        # 设备信息
        # 平台的名称
        desired_caps['platformName'] = 'Android'
        # 设备系统版本号
        desired_caps['platformVersion'] = '6.0'
        #  设备号 Android: adb devices
        desired_caps['deviceName'] = '192.168.17.101:5555'
        # app信息 启动的Activity
        desired_caps['appPackage'] = 'com.android.settings'
        # appPackage启动的包
        desired_caps['appActivity'] = '.Settings'
        # unicodeKeyboard   unicode设置(允许中文输入)
        desired_caps['unicodeKeyboard'] = True
        # resetKeyboard   键盘设置(允许中文输入)
        desired_caps['resetKeyboard'] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        # 实例化page类,要driver给base用
        self.search_obj=Search_page(self.driver)

    # 【3】写测试用例
    def test_search(self):
        # 进入page，直接调方法
        self.search_obj.search_text("123")

    # 【2】清理工作
    def teardown(self):
        self.driver.quit()