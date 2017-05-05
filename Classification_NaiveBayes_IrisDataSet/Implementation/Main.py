# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 15:55:57 2017

@author: Chandan Adiga


This file is the entry point.
Which 
1) Loads the data
2) Buidls the model 
3) Classify testing data(Could be modified to check testing/training data as well)
4) Also, added an API to predict given parameters to one of the class.

To Start run in terminal: python Main.py
Note: Requires Python 2.7.6 to be accessible in terminal.
"""
import Classifier_NB as classifier

#Clear screen..
print(chr(27) + "[2J")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Load entire data in to memory.
classifier.loadData() 

#Build model using trianing set..
classifier.model() 

#Calculate prediction percentage..
classifier.classify()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#Predict with some new inputs..
#setosa
#classifier.predict([4.2,3.0,5.1,0.2])

#virginica
#classifier.predict([6.2,3.0,5.4,2.1])

#versicolor
classifier.predict([6.4,3.0,5.4,1.1])
