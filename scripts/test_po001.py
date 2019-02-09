import sys, os
sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By
from Base.Base import Base
from appium import webdriver


class Test_search:

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
        # unicodeKeyboard      unicode设置(允许中文输入)
        desired_caps['unicodeKeyboard'] = True
        # resetKeyboard        键盘设置(允许中文输入)
        desired_caps['resetKeyboard'] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        # 实例化
        self.base_obj = Base(self.driver)

    def test_po001(self):
        # 点击搜索按钮
        self.base_obj.click_element(By.ID, "com.android.settings:id/search")

        # 输入搜索框
        self.base_obj.input_element(By.ID, "com.android.settings:id/search", "123")

        # 点击返回按钮
        self.base_obj.click_element(By.CLASS_NAME, "android.widget.ImageButton")





