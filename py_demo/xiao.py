#冒泡排序：
list=[14,5,8,9,1,2,16]
i=1
while i <=len(list)-1:
    j=0
    while j<len(list)-1:
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
        j=j+1
    i=i+1
print(list)

#1.判断输入的年份是否为闰年
year=int(input("请输入判断年份:"))
if year%4==0 and year%100!=0 or year%400==0:
        print("是闰年")
else:
        print("不是闰年")

#2.输入温度
a=float(input("请输入摄氏温度："))
b=float(input("请输入华氏温度："))
#转换温度
c=a*9/5+32
d=5/9*(b-32)

#输出结果
print("摄氏温度{}转化为华氏温度为:{}".format(a,c))
print("华氏温度{}转换为摄氏温度为:{}".format(b,d))

#3.输入圆的半径计算周长和面积