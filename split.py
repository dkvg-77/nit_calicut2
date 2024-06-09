# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 13:34:51 2022

@author: libiy
"""


import os

folderpath = str(os.getcwd())
import pandas as pd
from sklearn.model_selection import train_test_split

file1 = open(folderpath + '/parameter/initial_filename.txt','r')
initial_filename = file1.read()

file2 = folderpath + "/output_csv/" + "parameters_" + initial_filename
df = pd.read_csv(file2)

train, test = train_test_split(df, test_size=0.3)
print(train.shape)
print(test.shape)

train_df = pd.DataFrame(train)
train_df.to_csv(folderpath + "/output_csv/" +"train" + "_70_" + initial_filename, index = False) 


test_df = pd.DataFrame(test)
test_df.to_csv(folderpath + "/output_csv/" +"test" + "_30_" + initial_filename, index = False) 
 
"""
import random

with open("parameters_sst_binary.csv") as file:
    with open("train_sst_param.csv", "w") as f1, open("test_sst_param.csv", "w") as f2:
        for line in file:
            f = random.choice([f1, f2])
            f.write(line)
            """