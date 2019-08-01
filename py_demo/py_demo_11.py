# #selenium 模拟事件点击
# # ActionChains模拟用户的行为
# # 执行原理：调用ActionChains的方法时不会立即执行，会将所有的操作按顺序存放在一个队列里，当调用perform（）方法时，队列中的事件会依次执行。
#
# # 鼠标和键盘方法列表
# # perform（）执行链中的所有动作
# # click(on_element=None) 单机鼠标左键
# # double_click(on_element=None) 双击鼠标左键
# # move_to_element(to_element)  鼠标移动到某个元素
# # ele.send_key(key_to_send)  发送某个词的当前焦点元素
#
# # 鼠标事件实战
#
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
# driver = webdriver.Firefox()
# driver.get("https://xdclass.net")
# sleep(3)
# # 鼠标事件实战
#
# # # 定位鼠标移动到上面的元素。
# # menu_ele = driver.find_element_by_css_selector("html body div#app div div.main div.banner.w div.l_course_list ul.list_item li")
# # ActionChains(driver).move_to_element(menu_ele).perform()
# # sleep(2)
# # # 选中子菜单
# # sub_menu_ele = driver.find_element_by_css_selector("#app > div > div.main > div.banner.w > div.innerbox > div.base > div.sort > a:nth-child(1)")
# # sleep(1)
# # sub_menu_ele.click()
#
# # 模拟用户登录
# # login_ele = driver.find_element_by_css_selector("html body div#app div div.header div.nav_container div.r_userinfo.f_r div.login span")
# #
# # # 触发点击事件
# # ActionChains(driver).click(login_ele).perform()
# #
# # driver.find_element_by_css_selector("#app > div > div.header > div.main > div.login > div > div.mobienum > input[type=text]").clear()
# # driver.find_element_by_css_selector("#app > div > div.header > div.main > div.login > div > div.mobienum > input[type=text]").send_keys("13189567425")

# #
# # login_btn_ele = driver.find_element_by_css_selector("#app > div > div.header > div.main > div.login > div > div.login_btn > button")
# # login_btn_ele.click()
# #
# #
# # # 判断登录成功.鼠标移动在上面，判断字符
# # user_info_ele = driver.find_element_by_css_selector("#app > div > div.header > div > div.r_userinfo.f_r > div.avatar.f_r > img")
# # sleep(1)
# # ActionChains(driver).click()
# #
# # user_name_ele = driver.find_element_by_css_selector("#app > div > div.header > div > div.userbox.f_r > div > div.user > p")
# #
# # print("----测试结果----")
# # print(user_name_ele.text)
# #
# # name = user_name_ele.text
# #
# # if name == u"963258741":
# #     print("login ok")
# # else:
# #     print("login fail")
# from telnetlib import EC
#
# from selenium import webdriver
# driver = webdriver.Firefox()
#
# # 等待时间
# # 强制等待 sleep
#
# # 隐形等待
# # driver.implicitly_wait(10)
#
#
# # 显性等待-需要导入模块
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
#
# driver.get("http://www.baidu.com")
# # 捕获异常
# try:
#     ele = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,"kw")))
#     print("资源加载成功")
#     print(driver.title)
# except:
#     print("资源加载失败")
# finally:
#     driver.quit()
#     print("不管成不成功退出，资源清理")
#
# # 隐形等待和显性等待可以同时用，取两者之间最大值