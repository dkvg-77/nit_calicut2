# -*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np
#from sklearn.model_selection import train_test_split

folderpath = str(os.getcwd())  
file1 = open(folderpath + '/parameter/initial_filename.txt','r')
filename = file1.read().split("\n")
initial_filename=filename[0]
print(initial_filename)
#test_filename=filename[1]

testing = folderpath + "/output_csv/" +"test_30_train" + ".csv"
#testing = folderpath + "/output_csv/" + "/test_sst.csv"
test = pd.read_csv(testing)

training = folderpath + "/output_csv/" +"train_70_train" + ".csv"
#training= folderpath + "/output_csv/" + "/train_sst.csv"
train = pd.read_csv(training)



test_id = []
train_id = []

for index,row in train.iterrows():
    row = row.values.tolist()
    #print("row",row)
    train_id.append(row[0])
for index,row in test.iterrows():
    row = row.values.tolist()
    #print()
    #print("row",row)
    test_id.append(row[0])

test_data = []
train_data = []

for index,row in train.iterrows():
    row = row.values.tolist()
    #ID = row[0]
    train_data.append(row)
print("Length of train data:",len(train_data))
    
for index,row in test.iterrows():
    row = row.values.tolist()
    #ID = row[0]
    test_data.append(row)        
print("Length of test data:",len(test_data)) 

p_true=0
final=[]
p_false=0  


file3 = folderpath + "/output_csv/" + "final_prediction1" + ".csv"
each = pd.read_csv(file3)
prediction=[]
train_loc=[]
for index,row in each.iterrows():
   row = row.values.tolist()
   prediction.append(row[1])

#print(prediction)

acc=0
result=0
y_test=[]
y_pred=[]
#print(test_data[i][20])
for i in range(0,len(test_data)):
    #print(test_data[i][20], prediction[i])
    a=test_data[i][20]
    y_test.append(a)
    b=prediction[i]
    y_pred.append(b)
    if (a==b):
        acc=acc+1
    else:
        result=result+1       

percentage =acc/(acc+result)
print("accuracy %:",percentage, "\nTrue predictions=",acc,"\nFalse predictions=",result)


from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
cm = confusion_matrix(y_test, y_pred)
print(cm)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Negative", "Postive"])
disp.plot()

from sklearn.metrics import accuracy_score
print("\naccuracy:",((accuracy_score(y_test, y_pred)) * 100))


pos=[]
neg=[]
pos=cm[1]
neg=cm[0]

tp=pos[1]
fp=pos[0]
fn=neg[1]

print("\ntp,fp,fn are:",tp,fp,fn)
def calculate_f_score(tp, fp, fn):
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f_score = 2 * (precision * recall) / (precision + recall)
    return f_score,precision,recall

f_score,precision,recall = calculate_f_score(tp, fp, fn)
print("\nprecision:", precision)
print("recall:", recall)
print("F-score:", f_score)



        