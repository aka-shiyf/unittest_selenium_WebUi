from selenium.webdriver.common.by import By

from base.base_page import BasePage


class LoginPage(BasePage):
    # 页面元素
    cut_loc = (By.XPATH, "//div[@class='switchBtn']")
    username_loc = (By.XPATH, "//input[@placeholder='请输入手机号']")
    password_loc = (By.XPATH, "//input[@placeholder='请输入密码']")
    send_code_loc = (By.XPATH, "//span[text()='发送验证码']")
    code_loc = (By.XPATH, "//input[@placeholder='请输入验证码']")
    input_code_loc = (By.XPATH, "//input[@placeholder='请输入验证码']")
    login_loc = (By.XPATH, "//span[text()='登 录']")

    # 页面动作
    def login_ecshop(self, username, password, code):
        self.click(LoginPage.cut_loc)
        self.set_keys(LoginPage.username_loc, username)
        self.set_keys(LoginPage.password_loc, password)
        # self.click(LoginPage.input_code_loc)
        self.set_keys(LoginPage.input_code_loc, code)
        # self.click(LoginPage.login_loc)
# @ddt 装饰类，作用是用于申明当前类使用ddt数据驱动
# @data 装饰函数，作用是给函数传值
# @unpack 装饰函数，作用是数据解包
# @file_date 装饰函数，作用是直接读取yaml、json文件
