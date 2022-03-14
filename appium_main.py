# coding=gbk
from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common import desired_capabilities
from selenium.webdriver.common.by import By

desired_caps = dict()
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "11"
desired_caps["deviceName"] = "127.0.0.1:4723"
desired_caps["appPackage"] = "com.eg.android.AlipayGphone"
desired_caps["appActivity"] = ".AlipayLogin"
desired_caps['noReset'] = "True"
desired_caps['fullReset'] = "False"
desired_caps["resetKeyboard"] = "True"
desired_caps["unicodeKeyboard"] = "True"
driver = webdriver.Remote('127.0.0.1:4723/wd/hub', desired_caps)
print('链接到安卓模拟器')
time.sleep(2)
driver.find_element(By.XPATH, "//*[@text='忽略']").click()
time.sleep(2)
driver.find_elements(By.ID, "com.alipay.android.phone.openplatform:id/home_app_view")[11].click()
time.sleep(2)
TouchAction(driver).tap(x=175, y=452).perform()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@text='我的记录']").click()
time.sleep(2)
driver.find_elements(By.XPATH,"//*[@text='预览']")[0].click()
time.sleep(300)
driver.close_app()
driver.quit()
driver.find_element(By.CLASS_NAME,"NAME")