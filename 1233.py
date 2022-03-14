# coding=gbk
from appium import webdriver
import time

from selenium.webdriver.common import desired_capabilities

desired_caps = dict()
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "10"
desired_caps["deviceName"] = "127.0.0.1:4723"
desired_caps["appPackage"] = "com.eg.android.AlipayGphone"
desired_caps["appActivity"] = "com.eg.android.AlipayGphone.AlipayLogin"
desired_caps['noReset'] = "True"
desired_caps['fullReset'] = "False"
desired_caps["resetKeyboard"] = "True"
desired_caps["unicodeKeyboard"] = "True"
driver = webdriver.Remote('127.0.0.1:4723/wd/hub', desired_caps)
print('链接到安卓模拟器')
time.sleep(300)
driver.close_app()
driver.quit()