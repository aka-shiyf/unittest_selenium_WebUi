import time
import unittest
from selenium import webdriver


class BaseUtil(unittest.TestCase):
    # 前置
    def setUpC(self) -> None:
        self.dr = webdriver.Firefox()
        dr = self.dr
        self.dr.get("https://user.flashchainsign.com/#/login")

    # 后置
    def tearDown(self) -> None:
        pass
        time.sleep(5)
        self.dr.quit()
