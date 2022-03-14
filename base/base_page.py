from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from base.base_util import BaseUtil


class BasePage:

    def __init__(self, dr):
        self.dr = dr

    # 定位元素关键字
    def locator_element(self, loc):
        return self.dr.find_element(*loc)

    # 设置值关键字
    def set_keys(self, loc, value):
        self.locator_element(loc).send_keys(value)

    # 单击关键字
    def click(self, loc):
        self.locator_element(loc).click()

    # 下拉框关键字
    def choice_select(self, loc, value):
        """
        下拉选择元素
        :param loc: 下拉框的元素
        :param value: 列表索引数
        :return: 点击下拉框下索引元素
        """
        sel = Select(self.locator_element(loc))
        sel.select_by_value(value)

    # 模拟鼠标悬停选择关键字
    def hover_choice(self, loc1, loc):
        """
        鼠标悬停事件选择元素
        :param loc1: 鼠标悬停元素
        :param loc: 悬停后选择的元素
        :return: 单击操作
        """
        ActionChains(self.dr).move_to_element(loc1).perform()
        self.locator_element(loc).click()

    # 进框架
    def goto_frame(self, frame_name):
        """
        进入框架
        :param frame_name: 框架name
        :return: 进入框架操作
        """
        self.dr.switch_to.frame(frame_name)

    # 出框架
    def quit_frame(self):
        self.dr.switch_to.delattr_content()
