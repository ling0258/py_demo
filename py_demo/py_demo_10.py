# 页面元素定位
"""
八大元素定位方法
browser.find_element_by_id()
browser.find_element_by_class_name()
browser.find_element_by_css_selector()
browser.find_element_by_link_text()
browser.find_element_by_xpath()
browser.find_element_by_tag_name()
browser.find_element_by_partial_link_text()
browser.find_elements_by_name()
"""
from selenium import webdriver
from time import sleep


# 1.打开浏览器
driver = webdriver.Firefox()
# 打开网站
# driver.get("http://www.baidu.com")
# print(driver.title)

# 第一种元素定位方法
# driver.find_element_by_id("kw").send_keys("xiaoD课堂")
# driver.find_element_by_id("su").click() #点击事件

# 第二种元素定位方法
# driver.find_element_by_name("wd").send_keys("selenium")
# driver.find_element_by_id("su").click()
# driver.quit()

# 第三种
driver.find_element_by_class_name("s_ipt").send_keys("selenium")

driver.find_element_by_id("su").click()
print(driver.title)
sleep(2)
driver.quit()
# 定位到元素后的方法
"""clear()  清空
send_key()  输入
back（）      后退页面
maximize_window()  浏览器窗口最大化
click（）         点击事件
submit              提交表单 
"""

# browser.find_element_by_tag_name()   通过标签进行定位   不常用  标签通常不是唯一的



#find_element_by_link_text()    通过超链接


# driver.get("https://www.baidu.com")
# sleep(5)
# driver.find_element_by_link_text('新闻').click()
# # driver.find_element_by_partial_link_text("学习").click()
# sleep(2)
# driver.quit()


# CSS定位
# 根据css属性定位，一般class是用.标记， id是用#标记， 定位方式也会比Xpath快

# driver.get("http://xdclass.net")
#
# print(driver.title)
#
# sleep(5)
#
# driver.find_element_by_css_selector(".//*[@id='app']/div/div[2]/div[2]/div[3]/div/div[1]/div[4]/a/img").click()










# XPARH

# driver.get("http://xdclass.net")
# sleep(3)
# driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[4]/div[1]/span[2]").click()


