
# # import unittest
# # class UserTestCase(unittest.TestCase):
# #     """setup()用于测试前的初始化工作；"""
# #     def setUp(self):
# #         print("===setup==")
# #         self.name = "小D课堂"
# #     """tearDown（）测试后的清除工作，在每个测试方法运行时被调用"""
# #     def tearDown(self):
# #         print("===tearDown===")
# #
# #     def test_name(self):
# #         print("===test_name===")
# #         self.assertEqual(self.name,"小D课堂",msg="名字不对")  #断言字符串是否一致
# #         self.assertTrue('xdclass'.isupper(),msg="不是大写")  #断言字符串是否为大写
# #
# # """注意
# #
# #
# #
# #
# #
# #
# # 1.所有类中方法的入参为self，定义方法的变量也要self.变量
# # 2.定义测试用例，以test开头命名的方法，方法的入参为self
# # 3.unittest.main()方法会搜索该模块下所有以test开头的测试用例方法，并自动执行他们
# # 4.自己写的py文件不能，用unittest.py命名，不然会找不到testcase
# # 成功是输入.失败是F
# # """
# #
# #
# # if __name__ == '__main__':
# #     unittest.main()




# TestSuit
#
# import unittest
#
# class Test_login(unittest.TestCase):
#     def setUp(self):
#         self.age = 32
#         self.name = "小D课堂"
#         print("setup  method")
#
#     def test_one(self):
#         print("test_one 二当家小D来了")
#         # 断言是否相等
#         self.assertEqual(self.name,"小D课堂",msg="名字不对")
#
#
#     def test_two(self):
#         print("test_two 前端来了")
#         # 断言是否为true，msg是断言错误的提示信息
#         self.assertFalse('XD'.isupper(),msg="不是大写")
#
#
#     def test_three(self):
#         print("test_three 后端来了")
#         self.assertEqual(self.age,32)
#
#
#     def test_four(self):
#         print("test_four 小D课堂官网上线啦 https://www.xdclass.net")
#         self.assertEqual(self.age,32)
#
#     def tearDown(self):
#         print("tearDown method")
#         # 判断是否相同
#         self.assertEqual('foo'.upper(),'FOO')
#
#
# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(XdclassTestCase('test_one'))
#     suite.addTest(XdclassTestCase('test_two'))
#     suite.addTest(XdclassTestCase('test_three'))
#     suite.addTest(XdclassTestCase('test_four'))
#     # verbosity参数可以控制执行结果的输出，0是简单报告，1是一般报告（默认），2是详细报告
#     runner = unittest.TextTestRunner(verbosity=2)
#     runner.run(suite)





# HTMLTestRunner


# import HTMLTestRunner


import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import os
import random
print(os.getcwd())

class Test_login(unittest.TestCase):
    def setUp(self):
        self.age = 32
        self.name = "小D课堂"
        print("setup  method")

    def test_one(self):
        u"test_one方法"
        print("test_one 二当家小D来了")
        # 断言是否相等
        self.assertEqual(self.name,"小D课堂",msg="名字不对")


    def test_two(self):
        "test_two方法"
        print("test_two 前端来了")
        # 断言是否为true，msg是断言错误的提示信息
        self.assertTrue('XD'.isupper(),msg="不是大写")


    def test_three(self):
        "test_three方法"
        print("test_three 后端来了")
        self.assertEqual(self.age,32)


    def test_four(self):
        "test_four方法"  #案例title说明
        print("test_four 小D课堂官网上线啦 https://www.xdclass.net")
        self.assertEqual(self.age,32)

    def tearDown(self):
        print("tearDown method")
        # 判断是否相同
        self.assertEqual('foo'.upper(),'FOO')



if __name__ == "__main__":
    suit = unittest.TestSuite()
    suit.addTest(Test_login('test_one'))
    suit.addTest(Test_login('test_two'))
    suit.addTest(Test_login('test_three'))
    suit.addTest(Test_login('test_four'))
    # verbosity参数可以控制执行结果的输出，0是简单报告，1是一般报告（默认），2是详细报告
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    # 创建测试报告，此时这个文件还是空文件
    # wb 以二进制格式打开一个文件，只用于写入，如果文件存在则覆盖，不存在则创建
    filename = "C:\\Users\\华硕\\PycharmProjects\\py_demo\\Ring\\result.html" + time.strftime("%Y-%m-%d %H-%M-%S") + "result.html"
    #filename=str(random.randint(1000,9999))+"result.html"
    print(filename)
    fp = open(filename,"wb")
    # stream  定义一个测试报告写入的文件，title就是标题，description就是描述
    runner = HTMLTestRunner(stream=fp,title="小D课堂 测试报告",description="c测试用例执行情况")
    runner.run(suit)
    fp.close()


