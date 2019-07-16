#字符串的使用
str="hello world !"
print(str)
print(str[0])
print(str[1:5])
print(str[1:])
print(str[-1])
print(str*2)
print(str+"test")

#列表的常用操作
list=['like',50,49.5,'have']
list2=['hello',88,['jack','rose']]
print(list)
print(list[0])
print(list[-1])
print(list[1:])
print(list*3)
print(list+list2)
print(list[::-1])
print(list[:])
list.reverse()
list3=[]
list3.append("baidu")
list3.append("tengxun")

#元祖的使用
tuple=('qing',12,12.5,'lou')
tuple2=('jack',55,(25,'haha'))
print(tuple)
print(tuple[0])
print(tuple[-1])
print(tuple[1:])
print(tuple*3)
print(tuple+tuple2)
print(tuple[::-1])
print(tuple[:])


#集合常用操作
# var={'zhangsan','lisi','xiaoming'}
# print{var,type(var)}


#字典的常用操作
dict={'name':'john',12:50.5,'C':12}
print(dict)
print(dict['name'])
print(dict[12])
print(dict.keys())
print(dict.values())

dict2={}
dict2["1"]="jack"
dict2[13]=44
dict2[55.5]=45.2


#切片：通过下标的方式来获取某一个元素