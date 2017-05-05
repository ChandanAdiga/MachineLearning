# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 12:37:00 2017

@author: Chandan Adiga
ID: 2016HT12329
Email: 2016HT12329@wilp.bits-pilani.ac.in
BITS Pilani. WILP Division.

Either you can import CSVConverter or design your own which provides API parse() 
which inturn returns a two dimensional array of input data where each row is an array(size 5, 4 columns of attributes and 5th column is class name) of attributes of type float/int.
Module CSVConverter.py kept seperate to reduce dependency on storage structure of data set.
"""
import CSVConverter as source
import numpy
import math

training_set = []
testing_set = []
classes = ["I. setosa","I. versicolor","I. virginica"]
attribute_size = 4
class_size = 3;
X = []
Y = []
mean_and_varience_array = []

def loadData() :    
    print("\n------------------------[loadData()-------------------------");
    data_set = source.parse()    
    print("\nSource data set size:{0}".format(len(data_set)))
        
    index = 0
    for row in data_set:
        index+=1
        #Every 3rd row is a testing set...    
        if(index%3==0):
            testing_set.append(row);
        #Rest are training set..
        else:
            training_set.append(row);
        
    print("\nTesting set size:{0}".format(len(testing_set)))
    print("Training set size:{0}".format(len(training_set)))
    print("------------------------loadData()]-------------------------\n\n");

def model() :
    print("\n------------------------[Model-------------------------");
    global X
    global Y
    global mean_and_varience_array
    for row in training_set:
        X.append(row[:-1])
        Y.append(row[-1])
    X = numpy.asarray(X)
    Y = numpy.asarray(Y)
    X = X.astype(numpy.float)
    [m, n] = X.shape
#Mannually classifying:
    class1 = X[0:34]
    class2 = X[34:67]
    class3 = X[67:100]
    
    classes = [class1,class2,class3]
    print("Training set size m:{0}".format(len(training_set)))
    print("Training set attribute_size:{0}".format(attribute_size))
#    calculate Mean & Varience:
    for classIndex in range(0,class_size) :
        mean_and_varience_array.append([])
        for sample in range(0,n) :
            mean = numpy.mean(classes[classIndex][:,sample])
            varience = numpy.var(classes[classIndex][:,sample])
            mean_and_varience_array[classIndex].append([mean, varience])
        print("\nmean & varience for class-{0}'s attributes:\n{1}".format(classIndex,mean_and_varience_array[classIndex]))
        
    print("------------------------Model]-------------------------\n");

def computeProb(mean,varience,attribute) :
    exponent = math.exp(-(math.pow(attribute-mean,2)/(2*varience)))
    return (1.0 / (math.sqrt((2.0*math.pi) * varience))) * exponent
            
def classify() :
    print("\n\n------------------------[Classify-------------------------");
    test_set_size = len(testing_set) 
    correct_prediction_count = 0   
    probabilityOfEachClass = 1/float(class_size)
    for testItem in testing_set:
        class_probability_of_item = []
        for classIndex in range(0,class_size) :
            #Attribute-1
            probAttribute1 = computeProb(mean_and_varience_array[classIndex][0][0],mean_and_varience_array[classIndex][0][1],numpy.float(testItem[0]))        
            #Attribute-2            
            probAttribute2 = computeProb(mean_and_varience_array[classIndex][1][0],mean_and_varience_array[classIndex][1][1],numpy.float(testItem[1]))
            #Attribute-3
            probAttribute3 = computeProb(mean_and_varience_array[classIndex][2][0],mean_and_varience_array[classIndex][2][1],numpy.float(testItem[2]))            
            #Attribute-4
            probAttribute4 = computeProb(mean_and_varience_array[classIndex][3][0],mean_and_varience_array[classIndex][3][1],numpy.float(testItem[3]))                        
            #Total proability of class - classIndex:
            classProbability = probAttribute1 * probAttribute2 * probAttribute3 * probAttribute4 * probabilityOfEachClass
            
            class_probability_of_item.append(classProbability)
        #Now, get most probable class index..
        maxProbValue = max(class_probability_of_item)
        maxProbClassIndex = class_probability_of_item.index(maxProbValue)
#        print("{0} vs {1}".format(classes[maxProbClassIndex],testItem[4]))
        if(classes[maxProbClassIndex] == testItem[4]) :
            correct_prediction_count += 1
    
    #Calculate percentage of right classifications..
    correctnessPercentage = correct_prediction_count/float(test_set_size) * 100
    print('\nCorrectness of classifying testing set : {0}%'.format(correctnessPercentage))
            
    print("------------------------Classify]-------------------------\n");
    
def predict(predictItemAttributes) :
    print("\n\n------------------------[predict-------------------------");
    print("\npredictItemAttributes: {0}".format(predictItemAttributes))
    if(len(predictItemAttributes) == attribute_size):
        probabilityOfEachClass = 1/float(class_size)
        class_probability_of_item = []
        for classIndex in range(0,class_size) :
            #Attribute-1
            probAttribute1 = computeProb(mean_and_varience_array[classIndex][0][0],mean_and_varience_array[classIndex][0][1],numpy.float(predictItemAttributes[0]))        
            #Attribute-2            
            probAttribute2 = computeProb(mean_and_varience_array[classIndex][1][0],mean_and_varience_array[classIndex][1][1],numpy.float(predictItemAttributes[1]))
            #Attribute-3
            probAttribute3 = computeProb(mean_and_varience_array[classIndex][2][0],mean_and_varience_array[classIndex][2][1],numpy.float(predictItemAttributes[2]))            
            #Attribute-4
            probAttribute4 = computeProb(mean_and_varience_array[classIndex][3][0],mean_and_varience_array[classIndex][3][1],numpy.float(predictItemAttributes[3]))                        
            #Total proability of class - classIndex:
            classProbability = probAttribute1 * probAttribute2 * probAttribute3 * probAttribute4 * probabilityOfEachClass
            
            class_probability_of_item.append([classProbability])
        #Now, get most probable class index..
        maxProbValue = max(class_probability_of_item)
        maxProbClassIndex = class_probability_of_item.index(maxProbValue)
        print("\nGiven attributes are Classified to be : {0}".format(classes[maxProbClassIndex]))
    else :              
        print("\n Predicting parameters should be of size 4")
    print("------------------------predict]-------------------------\n");
