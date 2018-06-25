# -*- coding: utf-8 -*-
"""
Created on Tue May 22 10:06:16 2018

@author: lenovo
"""
import re
str1=input("enter the number: ")
regex = re.compile(r'[+-.]?[0-9]*[.][0-9]+')
response = regex.search(str1)
if response:
    # The groups contain the matched values.
    # It always returns the fully matched string
    rs=response.group()
    print(rs)
    print("True")
else:
    print("False")
    