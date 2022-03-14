import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

dr = webdriver.Firefox()
dr.get("https://www.baidu.com/")
xuanting = dr.find_element(By.XPATH, "//span[text()='设置']")
# 模拟鼠标悬停
ActionChains(dr).move_to_element(xuanting).perform()
# 找到元素后再点击
dr.find_element(By.XPATH, "//a[text()='搜索设置']").click()
time.sleep(60)
# dr.quit()

#鼠标悬停
# chain = ActionChains(driver)
# implement = driver.find_element_by_link_text()
# chain.move_to_element(implement).perform()
# 下拉框定位
# select_by_index(index) ——通过选项的顺序，第一个为 0
# select_by_value(value) ——通过value属性
# select_by_visible_text(text) ——通过选项可见文本
sel = Select(dr.find_element(By.XPATH, "//span[text()='设置']"))
sel.select_by_index('搜索设置')

# 删除一组数据集中的一条
# 方法名称后加S，定位一组数据 如driver.find_elements(定位方法,定位元素)
del_button_list = dr.find_elements(By.XPATH, "//a[text()='搜索设置']")
if len(del_button_list)>0:
    del_button_list.click()
else:
    print("没有可删除数据")
# 处理弹窗 ：alert（只有确定），confirm（有确定有取消），prompt（有确定有取消还可以输入值）
# access点击确认，dismiss点击取消，text获得文本，send_keys输入值
ale = dr.switch_to.alert
ale.accept()
# git init  初始化仓库
# git commit -m "描述"
# git remote add origin git@
# git push -u origin master -f
