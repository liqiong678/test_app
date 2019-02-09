from selenium.webdriver.common.by import By
from Base.Base1 import Base   # 提供定位方法的

class Search_page:

    def __init__(self, driver):
        # 搜索按钮
        self.s_b = (By.ID, "com.android.settings:id/search")
        # 搜索框
        self.s_s = (By.ID, "android:id/search_src_text")
        # 返回按钮
        self.s_back = (By.CLASS_NAME, "android.widget.ImageButton")
        # 实例化对象->这样可以调用定位方法啦
        self.base_object = Base(driver)

    # 点击搜索框，输入123
    # 传入一个原组，s_b = (By.ID, "com.android.settings:id/search")，加一个self

    def search_text(self, text):
        # 点击搜索按钮
        self.base_object.click_element(self.s_b)
        # 输入内容
        self.base_object.input_element(self.s_s,text)
        # 点击返回按钮
        self.base_object.click_element(self.s_back)





