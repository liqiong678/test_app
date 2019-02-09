import sys, os,pytest

sys.path.append(os.getcwd())
from page.sms import Send_Sms
from appium import webdriver


class Test_Sendsms:
      # 【1】初始化，生成driver
    def setup_class(self):
        desired_caps = {}
        # 设备信息
        # 平台的名称
        desired_caps['platformName'] = 'Android'
        # 设备系统版本号
        desired_caps['platformVersion'] = '6.0'
        #  设备号 Android: adb devices
        desired_caps['deviceName'] = '192.168.17.101:5555'
        # app信息 启动的Activity
        desired_caps['appPackage'] = 'com.android.messaging'
        # appPackage启动的包
        desired_caps['appActivity'] = '.ui.conversationlist.ConversationListActivity'
        # unicodeKeyboard   unicode设置(允许中文输入)
        desired_caps['unicodeKeyboard'] = True
        # resetKeyboard   键盘设置(允许中文输入)
        desired_caps['resetKeyboard'] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        # 实例化page类,要driver给base用
        self.sms_obj = Send_Sms(self.driver)

    # 【3】写测试用例
    @pytest.mark.run(order=1)
    def test_add_input_phone(self):
        # 点击添加信息
        self.sms_obj.add_sms_button()
        # 输入手机号,需要传值
        self.sms_obj.accept_user_input("1867889999")

    def test_input_sms(self):
        # 输入信息并发送
        self.sms_obj.input_sms_text("jhdjhdjkhjdks")
        # 点击按钮发送
        self.sms_obj.send_button


    # 【2】清理工作
    def teardown_class(self):
        self.driver.quit()