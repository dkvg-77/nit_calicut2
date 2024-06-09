
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

testing = folderpath + "/output_csv/" +"parameters_test.csv"
#testing = folderpath + "/output_csv/" + "/test_sst.csv"
test = pd.read_csv(testing)

training = folderpath + "/output_csv/" +"parameters_trai.csv"
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
label=0
p_true=0
final=[]
p_false=0


df= folderpath + "/output_csv/" +"R_value.csv"
rvalue_df = pd.read_csv(df)
rvalue=[]
print(rvalue_df.shape)
for index,row in rvalue_df.iterrows():
    row = row.values.tolist()
    rvalue.append(row)


df= folderpath + "/output_csv/" +"similarity.csv"
sim_value_df = pd.read_csv(df)
sim_value=[]
print(sim_value_df.shape)
for index,row in sim_value_df.iterrows():
    row = row.values.tolist()
    sim_value.append(row)

df= folderpath + "/output_csv/" +"distance.csv"
dist_df = pd.read_csv(df)
dist_value=[]
print(dist_df.shape)
for index,row in dist_df.iterrows():
    row = row.values.tolist()
    dist_value.append(row)
    
    
def compare1(check_array):
    count1=0
    count2=0
    #print(len(check_array))
    for i in range(0, len(check_array)):
        #train_id=check_array[0][i]
        if check_array[i][20]==1:
            count1=count1+1
        else:
            count2=count2+1
    return (count1,count2) 

def compare(test_id,check_array):
    count1=0
    count2=0
    #print(test_id)
    list1=rvalue[test_id]
    list1.remove(list1[0])
    #print(list1)
    list2=sim_value[test_id]
    list2.remove(list2[0])
    #print(list2, "Len:",len(list2), list2[0], list2[3751])
    list3=dist_value[test_id]
    list3.remove(list3[0])
    #print(list1[0])
    check_r=[]
    sim=[]
    dist=[]
    #print(check_array)
    for i in range(0, len(check_array)):
        pos=check_array[i][0]
        #print("pos:",pos)
        #print(list2[pos])
        #if list1[pos]>1:
        check_r.append(list1[pos])
        #if list2[pos]>0.20:
        sim.append(list2[pos])
        if list3[pos]<100:
            dist.append(list3[pos])
    #list1.sort()
    #print(check_r)
    max_r=max(check_r)
    #print(max_r)
    max_sim=max(sim)
    min_dist=min(dist)
    
    index_max_r=check_r.index(max_r)
    #print(index_max_r)
    index_sim=sim.index(max_sim)
    index_dist=dist.index(min_dist)
    #print(check_r, max_r,index_max_r)
    #label12=check_array[index_max_r][20]
    index_sim=index_sim-1
    index_dist=index_dist-1
    index_max_r=index_max_r-1
    label_sim=check_array[index_sim][20]
    label_dist=check_array[index_dist][20]
    label_r=check_array[index_max_r][20]
    #print(check_array[index_max_r])
    #return (label12)
    return (label_sim, label_dist, label_r)
    


pred_final=[]
flag=0
for count in range(0,len(test_data)):
#for count in range(22, 23):
    test_id=test_data[count][0] 
    temp1=[]
    pred=[]
    print("\n")
    print("id:",test_id) 
    pred.append(test_id)
    label = test_data[count][20]
    #print("Label of test_",count+1, ":  ",label)
    test_mcl_value = test_data[count][3] 
    test_mcl_count = test_data[count][4]
    test_cl_minus = test_data[count][5]   
    test_group = test_data[count][12]
    test_mclgroup = test_data[count][13]
    test_range = test_data[count][14]
    test_lsf= test_data[count][15]
    test_rsf = test_data[count][16]
    test_lss = test_data[count][17]
    test_rss = test_data[count][18]
    test_cl_size = test_data[count][19]

    p=q=0
    arr=[]
    array=[]
    train_index=[]
    cl_data=test_data[count][1]
    result=len(set((cl_data).split (",")))
    #print(set(cl_data),result)
    if (result) == 1:
        for index in range(0, len(train_data)):
            length=len(set((train_data[index][1]).split (",")))
            if (length) == 1:
                array.append(train_data[index][20])
        #print(array)
        c=d=0
        for i in range(0, len(array)):
            if array[i]==0:
                c=c+1
            else:
                d=d+1
        if c>d:
            label_1=0
        else:
            label_1=1
            
    elif (test_cl_size<=10 and test_cl_size>=450) or (test_cl_size<40 and test_cl_size>=30):
        label1=0
           
        """   
    #elif test_mcl_value>=27 and test_mcl_value!=30:
        #label1=0
        
    #elif test_mcl_value==20 and (test_unique_cl_count>9 and test_unique_cl_count<=13):
        #label1=1
        
    #elif test_mcl_value==20 and test_group==2:
        #label1=0 
        
    #elif test_mcl_value==6 and test_group==1:
        #label1=0
        
    #elif test_mcl_value==6 and test_group==2 and (test_range>=10 and test_range<=16):
        #label1=0
        
    #elif (test_unique_cl_count==12 or test_unique_cl_count==13):
        #label1=1
        
    #elif test_mcl_value==7 and test_group==1 and test_comp<0:
        #label1=0
        
    #elif test_mcl_value==30 and (test_comp<(-0.2)):
        #label1=1
        
    #elif test_mcl_value==17 and (test_comp<0):
        #label1=1
        
    #elif test_mcl_value==18 and test_group==0 and (test_comp>=-0.06 and test_comp<0):
        #label1=1
        
    elif test_mcl_value==18 and test_lsf==1 and (test_sub>=0.5):
        label1=1 
    elif (test_unique_cl_count>=8 or test_unique_cl_count<=10) and test_cl_size>175:
        label1=1  
        """
    else:
        check_array=[]
        print("...........")

        for index in range(0, len(train_data)):
            if (test_group==train_data[index][12]) and (test_mclgroup == train_data[index][13]):
                if (test_range == train_data[index][14]):
                    arr.append(train_data[index])
        if (len(arr))>=50:
            arr2=[]
            print("Hi..")
            for ro in arr: 
                if ro[3]==test_mcl_value:
                    arr2.append(ro)
            if len(arr2)>30:
                arr3=[]
                print("Hihoo..")
                for ro in arr2: 
                    if (ro[15]==test_lsf and ro[16]==test_rsf) or (ro[17]==test_lss and ro[18]==test_rss):
                        arr3.append(ro)
                
                if len(arr3)<=30:
                    check_array=arr3
                else:
                    print("me toooooo") 
                    arr4=[]
                    for ro in arr3:
                        if (ro[5] == test_cl_minus):
                            arr4.append(ro)
                    if len(arr4)<=30 or len(arr4)>30:
                        check_array=arr4
                    else:
                        arr5=[]
                        print("finally I am here")
                        for ro in arr4:
                            if (ro[19] ==(test_cl_size)):
                                arr5.append(ro)
                            if len(arr5)==0:
                                if (ro[19] >=(test_cl_size-30)and ro[19]<=(test_cl_size+30)):
                                    arr5.append(ro) 
                            if len(arr5)==0:
                                if (ro[19] >=(test_cl_size-150)and ro[19]<=(test_cl_size+150)):
                                    arr5.append(ro)  
                        check_array=arr5
                        
            else:
                print("meeee...")
                check_array=arr
                
        elif (len(arr))>10 and (len(arr))<50:
            print("Hihi..")
            check_array=arr
            
        else:
            print("Hihihi...")
            arr6=[]
            for index in range(0, len(train_data)):
                if (train_data[index][14]==(test_range) or train_data[index][3]==test_mcl_value):
                    arr6.append(train_data[index])
                if len(arr6)<10:
                    arr7=[]
                    if train_data[index][3]==test_mcl_value:
                        arr7.append(train_data[index])
                    check_array=arr7
                else:
                    check_array=arr6
 
        print("Length of check_array",len(check_array))
        #label_sim, label_dist, label_r,label_c_score =compare(count,check_array)
        label_sim, label_dist, label_r = compare(count,check_array)
        
        #print(label_sim,label_dist, label_r)
        if (label_sim==label_dist==label_r==1):
        #if (label_sim==label_dist==label_r==1)or (label_sim==label_r==1) or (label_dist==label_r==1)or (label_sim==label_dist==1):
            label1=1
        elif (label_sim==label_dist==label_r==0):
        #elif (label_sim==label_dist==label_r==0)or (label_sim==label_r==0) or (label_dist==label_r==0)or (label_sim==label_dist==0):
            label1=0
        else:
            label1=label_r

    pred.append(label1)
    pred_final.append(pred)            
#print(check_array[0][0])            

header = ['Id', 'Prediction']
#print("zero valued checkarray",flag)
dest2 = folderpath + "/output_csv/" + "final_prediction1" + ".csv"   
params_df = pd.DataFrame(pred_final, columns=header)
params_df.to_csv(dest2, index = False) 

#print(rvalue_df)

    


#print(rvalue_df)

    
"""            
            
    elif test_mclgroup==1:
        arr2=[]
        for ro in array:
            range1=test_range
            if ro[13]==1:
                if (ro[14] >=(range1-3)and ro[14]<=(range1+3)) or ro[20]>0.60:
                    arr2.append(ro)
        if len(arr2)!=0:
            check_array=arr2
        else:
            check_array=array
            
    elif test_mclgroup==2:    
        if test_group==4:
            arr2=[]
            for ro in array:
                if ro[13]==2:
                    if ro[4] == test_mcl_count and ro[15] == test_lsf and ro[16]==test_rsf:
                        arr2.append(ro)
                
        elif test_group==2:      
            arr2=[]
            for ro in array:
                if ro[13]==2:
                    if ro[4] == test_mcl_count and ro[15] == test_lsf and ro[16]==test_rsf:
                        arr2.append(ro)
                
        else:
            arr2=[]
            for ro in array:
                if ro[13]==2:
                    if (ro[14] >=(test_range-3)and ro[14]<=(test_range+3)) or ro[20]>0.60:
                        arr2.append(ro)  
                
        if len(arr2)!=0:
            check_array=arr2
        else:
            check_array=array        
            
    elif test_mclgroup==3: 
        if test_group==4:
            arr2=[]
            for ro in array:
                if ro[13]==3: 
                    if ro[4] == test_mcl_count and ro[15] == test_lsf and ro[16]==test_rsf:
                        arr2.append(ro)
                
        elif test_group==2:      
            arr2=[]
            for ro in array:
                if ro[13]==3:                
                    if ro[4] == test_mcl_count and ro[15] == test_lsf and ro[16]==test_rsf:
                        arr2.append(ro)
                
        else:
            arr2=[]
            for ro in array:
                if ro[13]==3:
                    if (ro[14] >=(test_range-3)and ro[14]<=(test_range+3)) or ro[20]>0.60:
                        arr2.append(ro)  
                
        if len(arr2)!=0:
            check_array=arr2
        else:
            check_array=array

    elif test_mclgroup==4:    
        for ro in array:
            arr2=[]
            range1=test_range
            if ro[13]==4:
                if (ro[14] >=(range1-3)and ro[14]<=(range1+3)) or ro[20]>0.60:
                    arr2.append(ro)
        if len(arr2)!=0:
            check_array=arr2
        else:
            check_array=array 

    elif test_mclgroup==5: 
        arr2=[]
        for ro in array:
            range1=test_range
            if ro[13]==5:
                if (ro[14] >=(range1-3)and ro[14]<=(range1+3)) or ro[20]>0.60:
                    arr2.append(ro)
        if len(arr2)!=0:
            check_array=arr2
        else:
            check_array=array 

    elif test_mclgroup==6: 
        if test_group==4:
            arr2=[]
            for ro in array:
                if ro[13]==6:
                    if ro[4] == test_mcl_count and ro[15] == test_lsf and ro[16]==test_rsf:
                        arr2.append(ro)
                
        elif test_group==2:      
            arr2=[]
            for ro in array:
                if ro[13]==6:
                    if ro[4] == test_mcl_count and ro[15] == test_lsf and ro[16]==test_rsf:
                        arr2.append(ro)
                
        else:
            arr2=[]
            for ro in array:
                if ro[13]==6:
                    if (ro[14] >=(test_range-3)and ro[14]<=(test_range+3)) or ro[20]>0.60:
                        arr2.append(ro)  
                
        if len(arr2)!=0:
            check_array=arr2
        else:
            check_array=array 
          
          
    temp1,label_Predicted=sdv_comp(check_array)    
    final.append(temp1)
    
    
    if label_Predicted==label:
        p_true=p_true+1
    else:
        p_false=p_false+1
print("Correctly Predicted",p_true)
print("Predicted wrong:",p_false)
#print(len(final))

dest2 = folderpath + "/output_csv/" + "final_prediction1" + ".csv"   
params_df = pd.DataFrame(final)
params_df.to_csv(dest2, index = False)     
"""

