# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 11:57:54 2017

@author: Chandan Adiga

This module is designed assuming:
1) first two rows are to be neglected as they contain 
meta data.(title, desc etc. in this case, heading and attributes name)
2) Attributes are seperated with tab('\t') and 5th item is class name.
To Start run: python Main.py
Note: Tested on Python 2.7.6 
"""
def parse() :
    data_set=[]
    items=[]
    line_count=0
    with open('data_set.txt') as source:
        for line in source:
            line_count+=1
            if(line_count>2) :
                items = line.strip().split('\t')
                if(len(items) == 5) :
                    data_set.append(items)
                    
#    for row in data_set:
#        print row
    return data_set;
    
