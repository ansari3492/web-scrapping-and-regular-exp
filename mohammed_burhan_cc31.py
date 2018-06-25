# -*- coding: utf-8 -*-
"""
Created on Tue May 22 13:43:03 2018

@author: Lenovo
"""

import re
str1=input("enter the email id: ")
x=re.compile(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-z]{1,3}$')
list=[]
response = x.search(str1)
if response:
    # The groups contain the matched values.
    # It always returns the fully matched string
    rs=response.group()
    print(rs)
    print("True")
else:
    print("False")
