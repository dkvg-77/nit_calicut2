# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 16:36:44 2021

@author: user
"""

import os
import pandas as pd
import numpy as np

folderpath = str(os.getcwd())
file1 = open(folderpath + '/parameter/initial_filename.txt', 'r')
filename = file1.read().split("\n")

initial_filename = filename[0]
# test_filename=filename[1]
cl_train_data = pd.read_csv(folderpath + "/output_csv/" + "train_70_train.csv")
cl_test_data = pd.read_csv(folderpath + "/output_csv/" + "test_30_train.csv" )

sim = []
dist = []
counter = 1
"""
def cos_sim1(A,B):
    cos_sim=np.dot(A,B)/(np.linalg.norm(A)*np.linalg.norm(B))
    return cos_sim
"""
for index, row in cl_test_data.iterrows():
    row = row.values.tolist()
    temp = []
    temp2 = []
    # cos_sim = []
    cl_testsequence = row[1].split(',')
    print(row[0])
    print(index)
    # print(cl_testsequence)

    for i in range(0, len(cl_testsequence)):
        cl_testsequence[i] = int(cl_testsequence[i])

    testname = str(index)
    temp.append(testname)
    temp2.append(testname)
    # print(testname)

    for ind, row in cl_train_data.iterrows():
        row = row.values.tolist()
        name = row[0]
        # temp.append(name)
        # temp2.append(name)
        cl_sequence = row[1].split(',')

        for i in range(0, len(cl_sequence)):
            cl_sequence[i] = int(cl_sequence[i])

        cl_testsequence = np.array(cl_testsequence)
        cl_sequence = np.array(cl_sequence)
        ml = max(len(cl_testsequence), len(cl_sequence))
        A = np.concatenate((cl_testsequence, np.zeros(ml - len(cl_testsequence))))
        B = np.concatenate((cl_sequence, np.zeros(ml - len(cl_sequence))))

        # cosine similarity
        cos_sim = np.dot(A, B) / (np.linalg.norm(A) * np.linalg.norm(B))
        # cos_sim=cos_sim1(A,B)
        temp.append(cos_sim)

        # Euclidean distance
        distance = np.linalg.norm(A - B)
        temp2.append(distance)
        """
        temp3 = A - B
        sum_sq = np.dot(temp3.T, temp3)
        temp2=np.sqrt(sum_sq)
        """
    sim.append(temp)
    dist.append(temp2)
    # print("Similarity:",dist)

dest = folderpath + "/output_csv/" + "similarity" + ".csv"
params_df = pd.DataFrame(sim)
params_df.to_csv(dest, index=False)

dest2 = folderpath + "/output_csv/" + "distance" + ".csv"
df = pd.DataFrame(dist)
df.to_csv(dest2, index=False)

