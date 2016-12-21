# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 11:27:03 2016

@author: uidw7238
"""

import pickle
import matplotlib.pyplot as plt


def getData():
    data  = pickle.load(open("./train.p","rb"))
    
    return data['features'], data['labels']

    

img, labels = getData()
label_list = labels.tolist()
class_count = []
for n in range(labels.max() + 1):
    print("Class: " + str(n) + "  Num of items: " + str(label_list.count(n)))
    class_count.append(label_list.count(n))
        

plt.bar(range(len(class_count)), class_count)

plt.show()

