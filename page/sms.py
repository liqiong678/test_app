from selenium.webdriver.common.by import By
from Base.Base1 import Base   # 提供定位方法的

class Send_Sms:
    def __init__(self,driver):
        # 实例化Base类
        self.base_obj = Base(driver)
        # 添加信息按钮
        self.addsms=(By.ID,"com.android.messaging:id/start_new_conversation_button")
        # 接收者的按钮
        self.accept_user=(By.ID,"com.android.messaging:id/recipient_text_view")
        # 输入信息
        self.input_sms=(By.ID,"com.android.messaging:id/compose_message_text")
        # 发送按钮
        self.send_button=(By.ID,"com.android.messaging:id/self_send_icon")

    def add_sms_button(self):
        # 添加信息按钮
        self.base_obj.click_element(self.addsms)

    def accept_user_input(self,phone):
        # 输入接收人
        self.base_obj.input_element(self.accept_user,phone)

    def input_sms_text(self,text):
        # 输入发送内容
        self.base_obj.input_element(self.input_sms,text)
        # 点击发送按钮
        self.base_obj.click_element(self.send_button)







