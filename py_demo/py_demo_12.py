from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

# alert与confirm弹窗处理
# # 弹窗常用方法（需要先切换窗口  switch_to_alert）
# accept()
# dismiss()
# sleep(1)
#
# driver.find_element_by_link_text("设置").click()
# sleep(2)
# # 点击单选框
# # driver.find_element_by_id("s1_2").click()
# sleep(1)
# driver.find_element_by_css_selector("#gxszButton > a.prefpanelgo").click()

driver = webdriver.Chrome()
# url = 'http://www.baidu.com'
url = "https://xdclass.net"
driver.get(url)
# print(driver.title)
#
# driver.find_element_by_link_text("设置").click()
# sleep(2)
# # 点击单选框
# driver.find_element_by_id("s1_2").click()
# sleep(1)
# driver.quit()

"""验证码处理常见解决方案
1.破解验证码
    OCR识别 
        test-orc  谷歌开元模块
    AI机器学习
        TensorFlow 
2.绕过
    让开发人员临时关闭验证码（安全性需要保密，一般在开发测试环境使用）

    提供一个万能的验证码（安全性需要保密，一般在开发测试环境使用）
    使用cookie（登录主要是为了那cookie，获取登录凭证）
    """

# 错误截图
login_ele = driver.find_element_by_css_selector(".login > span:nth-child(2)").click()
# username = driver.find_element_by_css_selector(".mobienum > input:nth-child(1)").send_keys("16621103980")
ActionChains(driver).click(login_ele).perform()

try:
    driver.find_element_by_id("xdclass").click()
except:
    driver.get_screenshot_as_file("D:/error.png")
