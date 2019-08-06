age=18
print(age)

score = 99.9
True
False
print(score)
#字符串  成对的双引号或成对的单引号括起来的内容叫字符串

a='hello'
b='bike'
#字符串的拼接+，不同类型的数据类型只能用逗号，
print(a,b)
print(a+b)

#字符串的切片

#单个字符串取值--->变量名[索引的位置]
print(a[-1])
#取一段值--->变量名[索引开始位置：索引结束位置]，切片是取左不取右,冒号前面要比后面小
print(a[0:4])
print(a[0:0])
print(a[:3])
print(a[:-1])
print(a[-2:])
print(a[-1:])
print(a[:])
#注释，代表这行代码不会被执行，快捷键：windows是control+/，mac是command+/

'''少时诵诗书'''#多行注释

#格式化输出
age=20
sex='boy'
print('mark今年%s岁'%age)
#多个变量的格式化输出
print("mark今年%s岁，是个%s"%(age,sex))
print("mark今年{0}岁，是个{1}".format(age,sex))#两种不同的用法

#元组
#关键字：tuple  关机键意味着不能用来做变量名,符合是()
#type(变量名)--->就可以获取数据的类型
#如果你的元组只有一个数据，必须在后面加上逗号
#元组里面的数据可以是任何类型
#元组切片之后还是元组
a=(1,)
print(type(a))

b=(1,'hello',(2,3,4),3.5)
print(b[1])
#输出4这个值，代码是什么
print(b[2][-1])
#赋值运算
#b[0]=2#元组里面的值一旦确定就就不能修改,元组不支持增删改
print(b)

#列表
#关键字：list  符合是[]
a1=[1,'hello',(1,2,3,4),3.5,['python','java']]
c=[1]
print(type(c))
print(len(a))
#列表里面的元素支持增删改，元组里的列表不能整体替换，但是列表里面的元素可以修改
#列表增加元素  列表名.append(你要增加的值)，一次只能增加一个值
#列表名.insert(索引位置,你要增加的值)
a1[-1].append('php')
a1[-1].insert(0,'c++')
print(a1)

#删除  pop()不传入位置默认删除最后一个元素，一次只能删除一个元素
a1.pop()
print(a1)

#字典
#关键字 dict 符号{}
#字典的数据组成 Key:value   字典只有一个数据也是字典
#字典无切片的用法，但是也支持增删改
#增加：字典名[key]=value  不存在的key就是新增
#修改：字典名[key]=value   已存在的key就是修改

a2={'name':'mark','age':18,'sex':'male'}
a2['name']='yyp'  #修改
a2['address']='shanghai'  #新增
print(a2)







