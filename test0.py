# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 14:03:20 2018

@author: Jiang
"""
"""测试字符串的find函数"""
#s='hello'
#print(s.find('h'))
#print(2**31)
#-2147483648
#t=range(2147483647,1,-3)

#t1=range(1021989372,1,-82778243)
#print(len(t1))
#for i in range(len(t1)):
#    print(t1[i])
#print(len(t))
#print(-1021989372-12*(-82778243))
#print(1021989372-12*82778243)

"""测试range功能，以第一个参数开头，不超过第二个参数，间距为最后一个参数"""
#t=3
#t<<=2
#print(t)
#t=[ i for i in range(1021989372,1,-82778243)]
#t=[i for i in range(9,0,-3)]
#for i in range(len(t)):
#    print(t[i])

"""测试词典的update功能，其实只要用defaultdict就好了，不用管有没有"""
#t={"abc":2,"efg":3,"hij":6}
#print(t.get("abc"))
#for i in t.keys():
#    print(t.get(i))
#t.update({"abc":10})
#print(t.get("aabe"))
#t1=t.copy()
#t.popitem()
#print(t.get("abc"))

#from collections import defaultdict
#map_dict=defaultdict(int)

"""测试词典的pop功能"""
#D= {'name': 'Bob', 'age': 14, 'sex': 'male'}
#pop_obj=D.pop('name','age')
#print(pop_obj)