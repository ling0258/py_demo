# 文件的基本操作
# 三个步骤：打开文件，读取文件。写入文件。关闭文件

"""
1. open   打开文件，并且返回文件操作对象
2.read    将文件内容读取到内存
3 write   将指定内容写入文件
4 close   关闭文件

"""
# 实例
# # 1.打开文件
# file = open("C:/test.txt")
# print(file)
# # 2.读取,显示行数
# text = file.read()
# print(text)
# print(len(text))
# print(" - " * 10) #打印分割线
# # 3.关闭文件
# file.close()

# 写入文件

# 打开
# file = open("C:/test.txt","w")# w写入会覆盖原有内容。a是追加在原有内容后面
# # 写入
# file.write("more")
#
# # 关闭
# file.close()

# readline 方法.查看单行
#
# file = open("C:/test.txt")
# text = file.readline()
# print(text) #查看单行
#
# file.close()

# 多行读取
#  readline 方法.查看单行
# # #
# file = open("C:/test.txt")
# while True:
#
#     text = file.readline()
#     if not text:
#         break
#     print(text) #查看单行
# file.close()

# 文件复制

# # 小文件复制
# # 打开
# file1 = open("C:/test.txt")#源文件
# file2 = open("C:/test01.txt","w")#目标文件
#
# # 2.读写
# text = file1.read()
# file2.write(text)
# # 3关闭文件
#
# file1.close()
# file2.close()

# 文件目录的常用管理操作
# os 模块中的方法
"""
1.rename    重命名
2.remove    删除
3.listdir      查看目录下文件
4.mkdir         创建目录
5.rmdir            删除目录
6.getcwd            获取当前目录
7.chdir             修改当前目录
8.path.isdir        判断是否为文件

"""

# 异常的概念:如果python遇到一个错误,会停止程序的执行,并提示一些错误信息
# 程序停止执行并提示错误信息,我们称之为:抛出异常


# 捕获异常
# try:
#     # 尝试执行的代码
# except:
#     # 出现错误的处理

# try:
#     # 实例  提示用户书如一个整数
#     num = int(input("请输入整数:"))
#     # 使用 10 除以用户输入的整数并且输出
#     result = 10/ num
#
#     print(result)
# except ZeroDivisionError:
#     print("除零错误")
# except ValueError:
#     print("请输入正确的整数!")

# 异常捕获完整语法
# else   只要尝试成功就执行else
# finally  无论是否尝试成功.都执行

# try:
#     # 实例  提示用户书如一个整数
#     num = int(input("请输入整数:"))
#     # 使用 10除以用户输入的整数并且输出
#     result = 10 / num
#
#     print(result)
# except ValueError:
#     print("请输入正确的整数!")
# except Exception as result:
#     print("未知错误 %s" % result)
# else:
#     print("尝试成功")
# finally:
#     print("无论是否出现错误都会执行的代码")
#
# print("- "* 50)



# 主动抛出raise异常
# 创建异常对象
# 抛出异常对象

# def input_password():
#     # 提示用户输入密码
#     pwd = input("请输入密码:")
#     # 判断密码长度>=8,返回用户输入的密码
#     if len(pwd) >= 8:
#         return pwd
#     # 如果<=8主动抛出异常
#     print("主动抛出异常")
#
#     ex = Exception("密码长度不够")
# #     抛出异常
#     raise ex
# # 提示用户输入密码
# try:
#     print(input_password())
# except Exception as result:
#     print(result)

# csv是Comma-Separated Values的缩写，是用文本文件形式储存的表格数据

import csv
# with open("test.csv","r",encoding="utf-8")as f:
#     reader = csv.reader(f)
#     rows = [row for row in reader]
# print(rows)

# 要提取其中某一列，可以用下面的代码
# with open("test.csv", "r", encoding = "utf-8") as f:
#     reader = csv.reader(f)
#     column = [row[1] for row in reader]
#
# print(column)

# 写文件
# 追加

# row = ['5','hanmeimei','23','81']
# out = open("test.csv","a",newline="")
# csv_writer = csv.writer(out,dialect="excel")
# csv_writer.writerow(row)


# python 中的json
#JSON 的全称是 JavaScript Object Notation，即 JavaScript 对象符号，它是一种轻量级的数据交换格式。JSON 的数据格式既适合人来读写，也适合计算机本身解析和生成。
"""
JSON 类型	Python 类型
对象（object）	字典（dict）
数组（array）	列表（list）
字符串（string）	字符串（str）
整数（number(int)） 	整数（int）
实数（number(real)）	浮点数（float）
true	True
false	False
null 	None
"""
# import json
# test_dict = {'a':1, 'b':2}
#
# #把字典转成json字符串
# json_text = json.dumps(test_dict)

# import json
# import codecs
#
# # 从文件中读取内容
# with codecs.open('1.json', 'r', 'utf-8') as f:
#     json_text = f.read()
#
# # 把字符串转成字典
# json_dict = json.loads(json_text)

# 1、dumps：把字典转成json字符串import json
# import json
# import codecs
# text_dict = {'a':1,'b':2}
# #把字典转成json字符串并写入到文件
# with codecs.open("1.json",'w','utf-8')as f:
#     json.dump(text_dict,f)
